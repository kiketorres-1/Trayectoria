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
    thrust_source=[],  # <-- COMPLETAR: Lista con valores de empuje (N)
    burn_time=(0, 3),  # <-- COMPLETAR: Tiempo de encendido y apagado del motor (s)
    dry_mass=0.5,  # <-- COMPLETAR: Masa sin combustible (kg)
    dry_inertia=(0.1, 0.1, 0.1),  # <-- COMPLETAR: Inercia (kg*m^2)
    nozzle_radius=0.02,  # <-- COMPLETAR: Radio de la tobera (m)
    grain_number=1,  # <-- COMPLETAR: Número de granos
    grain_density=1815,  # <-- COMPLETAR: Densidad del grano (kg/m^3)
    grain_outer_radius=0.02,  # <-- COMPLETAR: Radio exterior del grano (m)
    grain_initial_inner_radius=0.005,  # <-- COMPLETAR: Radio interior del grano (m)
    grain_initial_height=0.08,  # <-- COMPLETAR: Altura del grano (m)
    grain_separation=0,  # <-- COMPLETAR: Separación entre granos (m)
    grains_center_of_mass_position=0.1,  # <-- COMPLETAR: Posición del centro de masa de los granos (m)
    center_of_dry_mass_position=0.1,  # <-- COMPLETAR: Centro de masa sin combustible (m)
    nozzle_position=0,  # <-- COMPLETAR: Posición de la tobera (m)
    throat_radius=0.005,  # <-- COMPLETAR: Radio del cuello de la tobera (m)
    coordinate_system_orientation="nozzle_to_combustion_chamber"
)

# Definimos las características del cohete
LightningTraveller = Rocket(
    radius=0.0395,  # <-- COMPLETAR: Radio del cohete (m)
    mass=1.0,  # <-- COMPLETAR: Masa total sin motor (kg)
    inertia=(0.1, 0.1, 0.1),  # <-- COMPLETAR: Inercia (kg*m^2)
    power_off_drag=[],  # <-- COMPLETAR: Curva de arrastre sin motor
    power_on_drag=[],  # <-- COMPLETAR: Curva de arrastre con motor encendido
    center_of_mass_without_motor=0.3,  # <-- COMPLETAR: Posición del centro de masa sin motor (m)
    coordinate_system_orientation="tail_to_nose"
)

# Añadimos el motor al cohete
LightningTraveller.add_motor(Motor, position=0.0)

# Añadimos cono de nariz tipo von Karman
nose_cone = LightningTraveller.add_nose(length=0.1, kind="vonKarman", position=0)

# Añadimos aletas trapezoidales
fin_set = LightningTraveller.add_trapezoidal_fins(
    n=3,  # <-- COMPLETAR: Número de aletas
    span=0.05,  # <-- COMPLETAR: Envergadura (m)
    root_chord=0.08,  # <-- COMPLETAR: Cuerda en la base (m)
    tip_chord=0.03,  # <-- COMPLETAR: Cuerda en la punta (m)
    cant_angle=0,  # <-- COMPLETAR: Ángulo de inclinación (grados)
    position=-0.2  # <-- COMPLETAR: Posición respecto al centro del cohete (m)
)

# Definimos la función trigger para el paracaídas
def main_chute_trigger(p, y):
    return y < 300 and p < 0  # Se despliega a menos de 300 m y en descenso

# Añadimos el paracaídas principal
Main = LightningTraveller.add_parachute(
    "Main",
    cd_s=1.5,  # <-- COMPLETAR: Coeficiente de arrastre por superficie (m²)
    trigger=main_chute_trigger,
    sampling_rate=105,  # <-- COMPLETAR: Frecuencia de muestreo (Hz)
    lag=1.5  # <-- COMPLETAR: Retardo de despliegue (s)
)

# añadir Payload desplegable


# Creamos una simulación de vuelo
test_flight = Flight(
    rocket=LightningTraveller,
    inclination=85,
    heading=0,
    environment=env,
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