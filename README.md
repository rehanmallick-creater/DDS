# DDS — Drone Delivery System (Autonomous Flight Stack)

DDS is an autonomous drone flight system built using **PX4**, **ROS 2**, **MAVROS**, and **Gazebo**.  
The project focuses on **reliable autonomous mission execution**, not just simulation demos.

---

## 🚀 Features

- PX4 SITL + Gazebo Classic simulation
- ROS 2 Humble integration
- MAVROS bridge
- OFFBOARD position control
- Autonomous takeoff
- Distance-based waypoint navigation
- State-machine–driven missions
- OFFBOARD loss failsafe (auto-land)
- Return-to-Launch (RTL)

---

## 🧠 System Architecture


DDS Mission Node (ROS 2)
↓
MAVROS
↓
PX4
↓
Gazebo Simulation


---

## 📂 Repository Structure

DDS/
├── autonomy_ws/
│ └── src/
│ └── dds_mission/ # Autonomous mission logic
├── docs/ # Design & planning (added later)
└── README.md


---

## 🛠️ Tech Stack

- PX4 Autopilot (SITL)
- Gazebo Classic
- ROS 2 Humble
- MAVROS
- Python (rclpy)

---

## 🧪 Mission Flow

1. System initialization
2. OFFBOARD mode activation
3. Autonomous takeoff
4. Square waypoint mission (distance-based switching)
5. Return-to-Launch (RTL)
6. Auto landing & disarm
7. Failsafe landing on OFFBOARD loss

---

## ⚠️ Safety & Failsafes

- Continuous OFFBOARD monitoring
- Automatic landing on OFFBOARD loss
- RTL handled by PX4 for reliability

---

## 📌 Status

✅ Autonomous mission stack complete  
🟡 Documentation & extensions in progress

---

## 🔮 Future Work

- Obstacle avoidance
- Vision-based navigation
- Multi-drone coordination
- Real hardware deployment

---

## 👤 Author

**Rehan Alam**  
B.Tech CSE  
Autonomous Systems & Robotics

