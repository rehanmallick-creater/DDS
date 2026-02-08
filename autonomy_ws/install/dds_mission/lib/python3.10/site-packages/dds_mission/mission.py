from rclpy.qos import QoSProfile, ReliabilityPolicy
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from mavros_msgs.srv import CommandBool, SetMode
from mavros_msgs.msg import State
import math

class Mission(Node):
    def __init__(self):
        super().__init__('dds_mission')

        # Publishers / Subscribers
        self.setpoint_pub = self.create_publisher(
            PoseStamped,
            '/mavros/setpoint_position/local',
            10
        )
        self.state_sub = self.create_subscription(
            State,
            '/mavros/state',
            self.state_cb,
            10
        )
        qos = QoSProfile(depth=10)
        qos.reliability = ReliabilityPolicy.BEST_EFFORT

        self.pose_sub = self.create_subscription(
             PoseStamped,
             '/mavros/local_position/pose',
             self.pose_cb,
             qos
        )

        # Services
        self.arm = self.create_client(CommandBool, '/mavros/cmd/arming')
        self.mode = self.create_client(SetMode, '/mavros/set_mode')

        # State
        self.current_state = None
        self.current_pose = None
        self.phase = 'IDLE'
        self.intentional_mode_change = False
        self.wp_index = 0
        self.counter = 0

        # Square waypoints (10m square @ 10m altitude)
        self.waypoints = [
            (0.0, 0.0, 10.0),
            (10.0, 0.0, 10.0),
            (10.0, 10.0, 10.0),
            (0.0, 10.0, 10.0),
        ]

        self.reach_thresh = 0.7  # meters
        self.timer = self.create_timer(0.1, self.loop)

    def state_cb(self, msg):
        self.current_state = msg

    def pose_cb(self, msg):
        self.current_pose = msg

    def distance_to_target(self, target):
        dx = self.current_pose.pose.position.x - target[0]
        dy = self.current_pose.pose.position.y - target[1]
        dz = self.current_pose.pose.position.z - target[2]
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    def offboard_lost(self):
        return (
            self.current_state is not None and
            self.current_state.mode != 'OFFBOARD' and
            self.phase == 'WAYPOINTS' and
            not self.intentional_mode_change
        )

    def loop(self):
        # FAILSAFE: OFFBOARD lost → LAND
        if self.offboard_lost():
            self.get_logger().warn('OFFBOARD lost! Landing.')
            self.phase = 'LAND'

        msg = PoseStamped()
        msg.header.stamp = self.get_clock().now().to_msg()

        # Default hold
        target = (0.0, 0.0, 10.0)

        if self.phase == 'IDLE':
            target = (0.0, 0.0, 10.0)
            self.counter += 1
            if self.counter == 30:
                self.mode.call_async(SetMode.Request(custom_mode='OFFBOARD'))
                self.arm.call_async(CommandBool.Request(value=True))
                self.phase = 'WAYPOINTS'

        elif self.phase == 'WAYPOINTS' and self.current_pose is not None:
            target = self.waypoints[self.wp_index]

            if self.distance_to_target(target) < self.reach_thresh:
                self.wp_index += 1
                if self.wp_index >= len(self.waypoints):
                    self.phase = 'RTL'
        elif self.phase == 'RTL':
            self.intentional_mode_change = True
            self.get_logger().info('RTL triggered')
            self.mode.call_async(SetMode.Request(custom_mode='AUTO.RTL'))

        elif self.phase == 'LAND':
            target = (0.0, 0.0, 0.0)

        msg.pose.position.x = target[0]
        msg.pose.position.y = target[1]
        msg.pose.position.z = target[2]

        if self.phase != 'RTL':
            self.setpoint_pub.publish(msg)

def main():
    rclpy.init()
    rclpy.spin(Mission())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
