# Importante: todos los parámetros que se definen en el código estarán en el Sistema Internacional de Unidades (SI)
from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime

# Definimos las condiciones del entorno: latitud, longitud y elevación (en metros)
env = Environment(latitude=20, longitude=30, elevation=0)

# Establecemos la fecha y hora para la simulación
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12, 0))

# Modelo atmosférico estándar (también puedes usar modelos personalizados o reales)
env.set_atmospheric_model(type="standard_atmosphere")

# Definimos las condiciones del motor: empuje, masa, geometría del grano, etc.
Motor = SolidMotor(
    thrust_source=[
(0.006, 4485.5),

(0.022, 4479.455),

(0.035, 4485.5),

(0.057, 4261.83),

(0.076, 4068.385),

(0.088, 3929.346),

(0.114, 3747.992),

(0.196, 3282.516),

(0.281, 2877.491),

(0.341, 2762.633),

(0.414, 2708.226),

(0.483, 2671.956),

(0.629, 2611.504),

(0.752, 2575.233),

(0.837, 2551.053),

(0.932, 2532.917),

(0.983, 2514.782),

(1.043, 2478.511),

(1.242, 2369.698),

(1.412, 2279.021),

(1.539, 2224.615),

(1.709, 2091.621),

(1.826, 2085.576),

(1.959, 2031.17),

(2.098, 1946.538),

(2.215, 1934.447),

(2.294, 1867.951),

(2.351, 1861.906),

(2.439, 1861.906),

(2.487, 1813.545),

(2.61, 1795.409),

(2.793, 1728.912),

(2.894, 1662.416),

(3.008, 1505.242),

(3.065, 1408.52),

(3.175, 1245.301),

(3.188, 1620.1),

(3.21, 1432.7),

(3.232, 1269.481),

(3.254, 1184.849),

(3.286, 1130.443),

(3.308, 1069.991),

(3.355, 1027.675),

(3.412, 930.953),

(3.45, 870.501),

(3.479, 1094.172),

(3.491, 912.817),

(3.507, 852.366),

(3.529, 797.96),

(3.532, 701.237),

(3.555, 719.373),

(3.577, 677.057),

(3.649, 646.831),

(3.754, 525.928),

(3.893, 398.98),

(4.025, 235.761),

(4.231, 187.4),

(4.335, 145.084),

(4.566, 48.361),

(4.711, 48.361),

(4.717, 0.0)
     ],  # <-- COMPLETAR: Lista con valores de empuje (N)
    burn_time=(0, 42),  # <-- COMPLETAR: Tiempo de encendido y apagado del motor (s)
    dry_mass=1.91,  # <-- COMPLETAR: Masa sin combustible (kg)
    dry_inertia=(0.128, 0.128, 0.0013),  # <-- COMPLETAR: Inercia (kg*m^2)
    nozzle_radius=0.0762,  # <-- COMPLETAR: Radio de la tobera (m)
    grain_number= 6,  # <-- COMPLETAR: Número de granos
    grain_density=1815,  # <-- COMPLETAR: Densidad del grano (kg/m^3)
    grain_outer_radius=0.035,  # <-- COMPLETAR: Radio exterior del grano (m)
    grain_initial_inner_radius=0.0075,  # <-- COMPLETAR: Radio interior del grano (m)
    grain_initial_height=0.08,  # <-- COMPLETAR: Altura del grano (m)
    grain_separation=0,  # <-- COMPLETAR: Separación entre granos (m)
    grains_center_of_mass_position=0.1,  # <-- COMPLETAR: Posición del centro de masa de los granos (m)
    center_of_dry_mass_position=0.1,  # <-- COMPLETAR: Centro de masa sin combustible (m)
    nozzle_position=0,  # <-- COMPLETAR: Posición de la tobera (m)
    throat_radius=0.008,  # <-- COMPLETAR: Radio del cuello de la tobera (m)
    coordinate_system_orientation="nozzle_to_combustion_chamber"
)

# Definimos las características del cohete
LightningTraveller = Rocket(
    radius=6.55,  # <-- COMPLETAR: Radio del cohete (m)
    mass=18.26,  # <-- COMPLETAR: Masa total sin motor (kg)
    inertia=(0.1, 0.1, 0.1),  # <-- COMPLETAR: Inercia (kg*m^2)
    power_off_drag=[],  # <-- COMPLETAR: Curva de arrastre sin motor
    power_on_drag=[],  # <-- COMPLETAR: Curva de arrastre con motor encendido
    center_of_mass_without_motor=0.3,  # <-- COMPLETAR: Posición del centro de masa sin motor (m)
    coordinate_system_orientation="tail_to_nose"
)

# Añadimos el motor al cohete
LightningTraveller.add_motor(Motor, position=0.0)

# Añadimos cono de nariz tipo von Karman
nose_cone = LightningTraveller.add_nose(length=0.635, kind="vonKarman", position=0)

# Añadimos aletas trapezoidales
fin_set = LightningTraveller.add_trapezoidal_fins(
    n=4,  # <-- COMPLETAR: Número de aletas
    span = 0.1339,  # <-- COMPLETAR: Envergadura (m)  
    root_chord = 0.33,  # <-- COMPLETAR: Cuerda en la base (m)
    tip_chord = 0.101,  # <-- COMPLETAR: Cuerda en la punta (m)
    cant_angle = 27.5,  # <-- COMPLETAR: Ángulo de inclinación (grados)
    position=-0.0562  # <-- COMPLETAR: Posición respecto al centro del cohete (m)
)

# Definimos la función trigger para el paracaídas
def main_chute_trigger(p, y):
    return y < 2000 and p < 20  # Se despliega a menos de 300 m y en descenso

# Añadimos el paracaídas principal
Main = LightningTraveller.add_parachute(
    name = "Main",
    cd_s=0.8,  # <-- COMPLETAR: Coeficiente de arrastre por superficie (m²)
    trigger= 2000, # <-- COMPLETAR: Altura de despliegue (m)
    sampling_rate=105,  # <-- COMPLETAR: Frecuencia de muestreo (Hz)
    lag = 1  # <-- COMPLETAR: Retardo de despliegue (s)
)

#añadir drogue
drogue_chute = LightningTraveller.add_parachute(
    name = "drogue",
    cd_s = 0.8,                  
    trigger = 2000,         
    sampling_rate = 105,         
    lag = 3.0,                   
    noise=(0, 8.3, 0.5)
)

# Creamos una simulación de vuelo
test_flight = Flight(
    rocket=LightningTraveller,
    inclination = 85,
    heading = 0,
    environment = env,
    rail_length=1.0  # <-- COMPLETAR: Longitud de la rampa de lanzamiento (m)
)

# Mostramos toda la información del vuelo
test_flight.all_info()

# Exportamos la trayectoria a un archivo KML (para Google Earth, etc.)
test_flight.export.kml(
    file_name="trajectory_LightningTraveller.kml",
    extrude=True,
    altitude_mode="relative_to_ground"
)
