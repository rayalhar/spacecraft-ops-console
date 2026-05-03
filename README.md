# Spacecraft Ops Console

A Python-based spacecraft telemetry and command project using Kerbal Space Program as a simulation backend, interfaced through kRPC.

## Overview

This project connects to a simulated spacecraft in orbit using kRPC and provides a command-line interface for monitoring telemetry and issuing commands in real time.

The goal is to explore how spacecraft telemetry and command systems work, with the potential to expand into a more complete mission operations-style interface.

## Current Features

- Live telemetry (altitude, orbit, power, fuel)
- Command-line interface for spacecraft control
- SAS, RCS, orientation, and deployment commands
- Real-time interaction via kRPC

## Planned Features

- Graphical dashboard
- Automated warning system
- Event logging
- Telemetry history/trending
- Command validation
- OpenC3 COSMOS integration

## Tech

- Python
- kRPC (https://github.com/krpc/krpc)
- Kerbal Space Program (can be purchased on Steam, https://store.steampowered.com/app/220200/Kerbal_Space_Program/ )