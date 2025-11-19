import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/Malekai/Downloading-Data/master/sitka_weather_2014.csv"
df = pd.read_csv(url)

datas = df["AKST"]
tmax = df["Max TemperatureF"]
tmin = df["Min TemperatureF"]

plt.figure(figsize=(12, 6))
plt.plot(datas, tmax, label="Temperatura Máxima")
plt.plot(datas, tmin, label="Temperatura Mínima")

plt.title("Temperaturas Máximas e Mínimas - Sitka (2014)")
plt.xlabel("Data")
plt.ylabel("Temperatura (F)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
