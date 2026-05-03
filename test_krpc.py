import krpc
import math

# Connect to the KRPC server and get the active vessel
conn = krpc.connect(name='KSP Telemetry Test')
vessel = conn.space_center.active_vessel

# Reference frame setup
body = vessel.orbit.body # setting kerbin as the reference body
ref_frame = body.non_rotating_reference_frame # sets ref frame for velocity
# reminder: frame is set on Kerbin but does not rotate with it
# so velocity is relative to the center of Kerbin, not the surface

# establishing velocity of vessel and magnitude conversion to orbital speed (x,y,z comp)
velocity = vessel.velocity(ref_frame)
orbital_speed = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)

# Charge onboard
electric = vessel.resources.amount("ElectricCharge")
electric_max = vessel.resources.max("ElectricCharge")
battery_percent = (electric / electric_max) * 100

# how much fuel is onboard (liquid fuel for engines)
fuel = vessel.resources.amount("LiquidFuel")

# monoprop (for RCS)
monoprop = vessel.resources.amount("MonoPropellant")

# temperature (average across all parts)
temps = [part.temperature for part in vessel.parts.all]
avg_temp = sum(temps) / len(temps)

# current angular velocity (rotation)
angular = vessel.angular_velocity(body.reference_frame)


# Printing out telemetry data
print("vessel:", vessel.name)

print("\n--- ORBIT ---")
print(f"altitude: {vessel.flight().mean_altitude / 1000:.2f} km")
print(f"orbital speed: {orbital_speed:.2f} m/s")
print(f"apoapsis: {vessel.orbit.apoapsis_altitude / 1000:.2f} km")
print(f"periapsis: {vessel.orbit.periapsis_altitude / 1000:.2f} km")

print("\n--- POWER ---")
print(f"electric charge: {electric:.2f} / {electric_max:.2f} EC")
print(f"battery: {battery_percent:.2f} %")

print("\n--- PROPULSION ---")
print(f"liquid fuel: {fuel:.2f} units")
print(f"monopropellant: {monoprop:.2f} units")

print("\n--- THERMAL ---")
print(f"avg temp: {avg_temp:.2f} K")

print("\n--- ATTITUDE ---")
print(f"angular velocity: [{angular[0]:.3f}, {angular[1]:.3f}, {angular[2]:.3f}] rad/s")