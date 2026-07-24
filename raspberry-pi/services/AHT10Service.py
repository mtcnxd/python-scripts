#!/usr/bin/env python3

import time
from smbus2 import SMBus

AHT10_ADDRESS = 0x38

CMD_INIT = [0xE1, 0x08, 0x00]
CMD_MEASURE = [0xAC, 0x33, 0x00]


class AHT10Service:

    def __init__(self, bus=1):
        self.bus = SMBus(bus)
        self.initialize()

    def initialize(self):
        """
        Inicializa el sensor.
        """
        self.bus.write_i2c_block_data(AHT10_ADDRESS, CMD_INIT[0], CMD_INIT[1:])
        time.sleep(0.05)

    def read(self):
        """
        Devuelve:
            (temperatura, humedad)
        """

        # Iniciar medición
        self.bus.write_i2c_block_data(
            AHT10_ADDRESS,
            CMD_MEASURE[0],
            CMD_MEASURE[1:]
        )

        # Esperar conversión
        time.sleep(0.08)

        # Leer 6 bytes
        data = self.bus.read_i2c_block_data(AHT10_ADDRESS, 0x00, 6)

        # Bit 7 = Busy
        if data[0] & 0x80:
            raise RuntimeError("El sensor sigue ocupado.")

        raw_humidity = (
            (data[1] << 12) |
            (data[2] << 4) |
            (data[3] >> 4)
        )

        raw_temperature = (
            ((data[3] & 0x0F) << 16) |
            (data[4] << 8) |
            data[5]
        )

        humidity = raw_humidity * 100 / 1048576

        temperature = raw_temperature * 200 / 1048576 - 50

        return temperature, humidity

    def close(self):
        self.bus.close()
