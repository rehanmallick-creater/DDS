# DDS — System Overview

DDS (Drone Delivery System) is an autonomous flight control stack designed to
execute missions reliably using PX4 and ROS 2.

The project focuses on **mission logic, safety, and autonomy**, not just basic simulation.

---

## High-Level Goal

Enable a drone to:
- Take off autonomously
- Execute a predefined mission
- Handle failures safely
- Return and land without human intervention

---

## Core Components

### 1. DDS Mission Node (ROS 2)
- Written in Python using `rclpy`
- Implements a **state machine**
- Publishes position setpoints
- Monitors vehicle state and safety conditions

### 2. MAVROS
- Acts as a bridge between ROS 2 and PX4
- Converts ROS topics/services into MAVLink messages
- Handles arming, mode switching, telemetry

### 3. PX4 Autopilot
- Handles low-level flight control
- Executes OFFBOARD commands
- Manages RTL and LAND behaviors
- Provides safety mechanisms

### 4. Gazebo Simulation
- Simulates drone physics
- Allows safe testing of missions
- Mirrors real PX4 behavior closely

---

## Control Flow


---

## Mission Execution Summary

1. System initializes and waits
2. OFFBOARD mode is enabled
3. Drone takes off to target altitude
4. Waypoints are executed using distance-based logic
5. Mission completion triggers RTL
6. PX4 handles return and landing
7. Failsafe monitors OFFBOARD health at all times

---

## Design Philosophy

- Prefer PX4 native features (RTL, LAND) where possible
- Keep mission logic explicit and readable
- Avoid timing-based behavior; use feedback instead
- Prioritize safety over mission completion

---

## Current Status

- Core autonomous mission stack: ✅ complete
- Safety and failsafes: ✅ implemented
- Documentation and extensions: 🟡 in progress
