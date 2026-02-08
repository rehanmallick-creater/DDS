# DDS — Mission State Machine

DDS missions are controlled using an explicit **state machine**.
This ensures predictable behavior, safe transitions, and easy debugging.

---

## Why a State Machine?

Autonomous flight is not a linear script.
A state machine allows:

- Clear mission phases
- Safe transitions between modes
- Priority handling (failsafe vs mission)
- Deterministic behavior

---

## Mission States

### IDLE
- Initial state
- System waits for PX4 and MAVROS readiness
- Starts publishing neutral setpoints
- Switches to OFFBOARD when ready

---

### TAKEOFF (implicit via OFFBOARD)
- OFFBOARD mode enabled
- Vehicle armed
- Position setpoint sent at target altitude
- Takeoff handled smoothly by PX4 position control

---

### WAYPOINTS
- Drone follows predefined waypoints
- Waypoint switching is **distance-based**, not time-based
- Ensures feedback-driven navigation

Waypoint progression logic:
- Compute distance to target
- If distance < threshold → advance to next waypoint

---

### RTL (Return-to-Launch)
- Triggered after final waypoint
- DDS intentionally exits OFFBOARD
- PX4 AUTO.RTL mode is activated
- PX4 handles return, descent, landing, and disarm

---

### LAND (Failsafe)
- Triggered only on **unexpected OFFBOARD loss**
- Ensures safe landing if mission control is lost
- Never interferes with intentional RTL

---

## State Transition Diagram



IDLE
↓
OFFBOARD / TAKEOFF
↓
WAYPOINTS ──┐
↓ │ (OFFBOARD loss)
RTL └──→ LAND (failsafe)
↓
LAND & DISARM


---

## Failsafe Priority Rules

- OFFBOARD loss is monitored continuously
- OFFBOARD loss is ignored during RTL (intentional mode change)
- Failsafe triggers only during active waypoint execution

This prevents conflicts between mission logic and safety logic.

---

## Design Decisions

- OFFBOARD used only when necessary
- PX4 native RTL preferred over custom logic
- Distance-based navigation chosen over timing
- Explicit phase tracking to avoid race conditions

---

## Result

The state machine guarantees:
- Predictable mission flow
- Robust handling of edge cases
- Safe termination in all scenarios

