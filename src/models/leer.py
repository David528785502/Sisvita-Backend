import pandas as pd

# Especifica la ruta completa del archivo si está en el mismo directorio que leer.py
archivo_excel = 'C:/Users/David/OneDrive/Escritorio/back/src/models/geodir-ubigeo-reniec.xlsx'

df = pd.read_excel(archivo_excel)

# Ahora puedes trabajar con el dataframe df
print(df.head())