from rocketpy import Environment, SolidMotor, Rocket, Flight

env = Environment(latitude= 40.3692414, longitude= -4.1222381, elevation= 667)

import datetime
tomorrow = datetime.date.today()
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 10))
env.set_atmospheric_model(type='Forecast', file="GFS")

CessaroniH125 = SolidMotor(
    thrust_source=[],
    dry_mass= 0.293,
    dry_inertia=(0.00383, 0.13456, 0.13456),
    nozzle_radius=19/1000,
    grain_number=2,
    grain_density=1815,
    grain_outer_radius=19/1000,
    grain_initial_inner_radius=0.0065,
    grain_separation=5/1000,
    grains_center_of_mass_position=0.151,
    center_of_dry_mass_position=0.95,
    grain_initial_height=0.1,
    nozzle_position=0.015,
    burn_time= (0.01, 2.15),
    throat_radius=0.0075,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

Satus = Rocket(
    radius=0.0796,
    mass=1.21,
    inertia=(0.13456, 0.13456, 0.00383),
    power_off_drag=[],

    power_on_drag=[],
    center_of_mass_without_motor= ,
    coordinate_system_orientation="tail_to_nose"
)

Satus.add_motor(CessaroniH125, position=0.0)

#adding Aerodynamic surfaces

nose_cone = Satus.add_nose(length=0.255, kind="vonKarman", position=0)

fin_set = Satus.add_trapezoidal_fins(
    n=4,
    span=0.1,
    root_chord=0.11,
    tip_chord=0.065,
    cant_angle=37,
    position=1,
)

Main = Satus.add_parachute(
    "Main",
    cd_s=0.8,
    trigger=1000,
    sampling_rate=105,
    lag=3,
)
test_flight = Flight(rocket=Satus, inclination=84.15, heading=0, environment=env, rail_length = 3)

test_flight.all_info()

test_flight.export.kml(
    file_name="trajectory_satus.kml",
    extrude = True,
    altitude_mode="relative_To_Ground",
)