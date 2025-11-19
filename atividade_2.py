import pandas as pd

# 1. Carregar CSV
url = "https://raw.githubusercontent.com/Malekai/Downloading-Data/master/sitka_weather_2014.csv"
df = pd.read_csv(url)

print("Colunas disponíveis:")
print(df.columns)

tmax = df["Max TemperatureF"]
tmin = df["Min TemperatureF"]

print("\nEstatísticas - Temperatura Máxima:")
print(tmax.describe()[["min", "max", "mean"]])

print("\nEstatísticas - Temperatura Mínima:")
print(tmin.describe()[["min", "max", "mean"]])
