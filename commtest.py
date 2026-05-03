## Live Command Test
import krpc
import math

conn = krpc.connect(name='KSP Command Console')
vessel = conn.space_center.active_vessel

body = vessel.orbit.body
ref_frame = body.non_rotating_reference_frame

def print_telemetry():
    velocity = vessel.velocity(ref_frame)
    orbital_speed = math.sqrt(velocity[0]**2 + velocity[1]**2 + velocity[2]**2)

    electric = vessel.resources.amount("ElectricCharge")
    electric_max = vessel.resources.max("ElectricCharge")
    fuel = vessel.resources.amount("LiquidFuel")
    monoprop = vessel.resources.amount("MonoPropellant")

    print("\n--- TELEMETRY ---")
    print(f"vessel: {vessel.name}")
    print(f"altitude: {vessel.flight().mean_altitude / 1000:.2f} km")
    print(f"orbital speed: {orbital_speed:.2f} m/s")
    print(f"apoapsis: {vessel.orbit.apoapsis_altitude / 1000:.2f} km")
    print(f"periapsis: {vessel.orbit.periapsis_altitude / 1000:.2f} km")
    print(f"electric charge: {electric:.2f} / {electric_max:.2f} EC")
    print(f"battery: {(electric / electric_max) * 100:.2f} %")
    print(f"liquid fuel: {fuel:.2f} units")
    print(f"monopropellant: {monoprop:.2f} units")


while True:
    command = input("\nKSP_CMD> ").lower()

    if command == "telemetry":
        print_telemetry()

    # --- BASIC CONTROL ---
    elif command == "sas on":
        vessel.control.sas = True
        print("SAS enabled")

    elif command == "sas off":
        vessel.control.sas = False
        print("SAS disabled")

    elif command == "rcs on":
        vessel.control.rcs = True
        print("RCS enabled")

    elif command == "rcs off":
        vessel.control.rcs = False
        print("RCS disabled")

    elif command == "lights on":
        vessel.control.lights = True
        print("lights enabled")

    elif command == "lights off":
        vessel.control.lights = False
        print("lights disabled")

    # --- ORIENTATION ---
    elif command == "point prograde":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.prograde
        print("Pointing prograde")

    elif command == "point retrograde":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.retrograde
        print("Pointing retrograde")

    elif command == "point normal":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.normal
        print("Pointing normal")

    elif command == "point antinormal":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.anti_normal
        print("Pointing anti-normal")

    elif command == "point radial":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.radial
        print("Pointing radial out")

    elif command == "point antiradial":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.anti_radial
        print("Pointing radial in")

    elif command == "point stability":
        vessel.control.sas = True
        vessel.control.sas_mode = conn.space_center.SASMode.stability_assist
        print("Stability assist mode")

    # --- DEPLOY / RETRACT ---
    elif command == "solar deploy":
        vessel.control.solar_panels = True
        print("Solar panels deployed")

    elif command == "solar retract":
        vessel.control.solar_panels = False
        print("Solar panels retracted")

    elif command == "antenna deploy":
        vessel.control.antennas = True
        print("Antennas deployed")

    elif command == "antenna retract":
        vessel.control.antennas = False
        print("Antennas retracted")

    elif command == "radiator deploy":
        vessel.control.radiators = True
        print("Radiators deployed")

    elif command == "radiator retract":
        vessel.control.radiators = False
        print("Radiators retracted")

    # --- HELP ---
    elif command == "help":
        print("""
commands:

telemetry

sas on / sas off
rcs on / rcs off
lights on / lights off

point prograde
point retrograde
point normal
point antinormal
point radial
point antiradial
point stability

solar deploy / solar retract
antenna deploy / antenna retract
radiator deploy / radiator retract

help
exit
""")

    elif command == "exit":
        print("closing command console")
        break

    else:
        print("unknown command. type help")