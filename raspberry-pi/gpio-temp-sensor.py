import time
from services.AHT10Service import AHT10Service

sensor = AHT10Service()

try:
	while True:
		temp, hum = sensor.read()

		print(f"Temperatura: {temp:.2f} °C")
		print(f"Humedad:     {hum:.2f} %")
		print("-" * 30)

		time.sleep(2)

except Exception as error:
	print(error)


finally:
	sensor.close()


if __name__ == "__main__":
    pass
