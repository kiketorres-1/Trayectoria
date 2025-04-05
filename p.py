import pandas as pd
import csv  # Para acceder a constantes como csv.QUOTE_NONE

# Ruta del archivo original
input_path = "Cesaroni_266H125-12Acsx.csv"

# Ruta del archivo de salida
output_path = "Cesaroni 266H125-12Acomma.txt"

# Cargar el archivo CSV
df = pd.read_csv(input_path, header=None)

# Dar formato a cada fila como [valor1, valor2],
formatted_rows = df.apply(lambda row: f"[{row.iloc[0]}, {row.iloc[1]}],", axis=1)

# Guardar el resultado sin comillas, sin encabezado y sin escapado
formatted_rows.to_csv(
    output_path,
    index=False,
    header=False,
    quoting=csv.QUOTE_NONE,
    escapechar="\\"
)

print(f"✅ Archivo guardado como: {output_path}")
