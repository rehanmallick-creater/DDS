# DDS — Failsafe Logic

Autonomous flight systems must prioritize **safety over mission success**.
DDS implements a focused failsafe strategy centered on OFFBOARD health.

---

## Failure Scenario Considered

The primary critical failure addressed is:

- **Unexpected OFFBOARD mode loss**

This can occur due to:
- MAVROS crash
- ROS node failure
- Communication drop
- Timing violations in OFFBOARD setpoints

---

## Failsafe Detection

DDS continuously monitors vehicle state via MAVROS.

Failsafe condition:
- Vehicle mode is no longer `OFFBOARD`
- DDS is actively executing waypoints
- Mode change was **not intentional**

This ensures false triggers are avoided.

---

## Intent Awareness

DDS differentiates between:
- **Intentional OFFBOARD exit** (e.g., RTL)
- **Unintentional OFFBOARD loss** (failure)

A dedicated flag is used to mark intentional mode changes.
Failsafe logic is disabled during these transitions.

---

## Failsafe Action

When an unintentional OFFBOARD loss is detected:

1. Mission execution stops
2. DDS switches to LAND phase
3. Drone descends vertically
4. Vehicle disarms after landing

This behavior ensures:
- Minimal horizontal drift
- Controlled descent
- Safe termination

---

## Why LAND Instead of RTL?

For failsafe scenarios:
- Landing immediately is safer than returning
- Reduces risk in unknown environments
- Avoids extended autonomous behavior during failure

RTL is reserved for **planned mission completion**.

---

## Design Principles

- Failsafe logic must be simple
- Avoid multiple competing recovery paths
- Safety decisions must be deterministic
- Explicit intent tracking prevents race conditions

---

## Result

DDS failsafe logic ensures:
- No uncontrolled flight
- No mission logic conflicts
- Predictable behavior during failures
