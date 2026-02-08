# DDS — Future Extensions

DDS is designed as a **scalable autonomous flight stack**.
The current implementation focuses on reliability and safety,
while leaving clear paths for future expansion.

---

## 1. Obstacle Avoidance

Integrate real-time obstacle avoidance using:
- LiDAR or depth camera
- PX4 obstacle avoidance interface
- Local re-planning around obstacles

This would allow:
- Safer low-altitude flight
- Operation in cluttered environments

---

## 2. Vision-Based Navigation

Extend DDS with computer vision:
- Visual odometry
- Marker-based landing
- Object detection for delivery zones

Possible tools:
- OpenCV
- ROS 2 vision pipelines
- Depth cameras (RealSense, ZED)

---

## 3. Dynamic Mission Planning

Replace static waypoints with:
- Runtime mission generation
- Conditional mission branching
- Geo-fence–aware routing

This enables:
- Adaptive delivery routes
- Smarter decision-making

---

## 4. Multi-Drone Coordination

Scale DDS to support:
- Multiple drones
- Swarm coordination
- Task allocation

Potential approaches:
- ROS 2 namespaces
- Central mission planner
- Decentralized coordination logic

---

## 5. Real Hardware Deployment

Transition from simulation to real drone:
- PX4 on real flight controller
- Companion computer (Jetson / Raspberry Pi)
- Real sensors and telemetry

Simulation-first design ensures minimal code changes.

---

## Design Philosophy Going Forward

- Keep mission logic hardware-agnostic
- Prefer PX4-native capabilities
- Validate extensively in simulation before flight
- Maintain safety as the highest priority

---

## Conclusion

DDS provides a solid foundation for advanced autonomous drone systems.
The architecture supports incremental upgrades without redesigning the core.
