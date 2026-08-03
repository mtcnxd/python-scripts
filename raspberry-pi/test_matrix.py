from time import sleep

from matrix8x8 import Matrix8x8


matrix = Matrix8x8(
    brightness=5
)


# Mostrar una letra
matrix.show_char("A")
sleep(2)


# Limpiar
matrix.clear()
sleep(1)


# Mostrar un número
matrix.number(5)
sleep(2)


# Mostrar texto
matrix.text("A")
sleep(2)


# Scroll
matrix.scroll(
    "HELLO",
    delay=0.1
)


matrix.clear()
