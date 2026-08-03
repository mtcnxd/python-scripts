from time import sleep

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas


# SPI0 / CE0
serial = spi(
    port=0,
    device=0,
    gpio=noop()
)

# Una matriz 8x8
device = max7219(
    serial,
    cascaded=1,
    block_orientation=0,
    rotate=0
)

# Brillo: 0-15
device.contrast(5)


# ==========================================
# Prueba 1: encender todos los LEDs
# ==========================================

print("Prueba 1: todos los LEDs")

with canvas(device) as draw:
    for x in range(8):
        for y in range(8):
            draw.point((x, y), fill="white")

sleep(3)


# ==========================================
# Prueba 2: apagar todo
# ==========================================

print("Prueba 2: apagar")

device.clear()

sleep(2)


# ==========================================
# Prueba 3: dibujar una X
# ==========================================

print("Prueba 3: X")

with canvas(device) as draw:
    for i in range(8):
        draw.point((i, i), fill="white")
        draw.point((7 - i, i), fill="white")

sleep(3)


# ==========================================
# Prueba 4: dibujar un cuadrado
# ==========================================

print("Prueba 4: cuadrado")

with canvas(device) as draw:
    for x in range(8):
        draw.point((x, 0), fill="white")
        draw.point((x, 7), fill="white")

    for y in range(8):
        draw.point((0, y), fill="white")
        draw.point((7, y), fill="white")

sleep(3)


# ==========================================
# Apagar al terminar
# ==========================================

device.clear()

print("Prueba terminada")
