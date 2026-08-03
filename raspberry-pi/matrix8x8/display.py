from time import sleep

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas

from .font import FONT


class Matrix8x8:

    WIDTH = 8
    HEIGHT = 8

    def __init__(
        self,
        port=0,
        device=0,
        brightness=5,
        rotate=0,
        block_orientation=0,
    ):

        serial = spi(
            port=port,
            device=device,
            gpio=noop(),
        )

        self.device = max7219(
            serial,
            cascaded=1,
            block_orientation=block_orientation,
            rotate=rotate,
        )

        self.device.contrast(brightness)

    def clear(self):
        self.device.clear()

    def brightness(self, value):
        """
        Brillo entre 0 y 15.
        """
        if not 0 <= value <= 15:
            raise ValueError("brightness debe estar entre 0 y 15")

        self.device.contrast(value)

    def pixel(self, x, y, state=True):
        """
        Enciende o apaga un pixel.
        """

        if not (0 <= x < self.WIDTH):
            raise ValueError("x debe estar entre 0 y 7")

        if not (0 <= y < self.HEIGHT):
            raise ValueError("y debe estar entre 0 y 7")

        with canvas(self.device) as draw:

            if state:
                draw.point((x, y), fill="white")

    def show_char(self, char):
        """
        Muestra un solo carácter.
        """

        char = char.upper()

        if char not in FONT:
            raise ValueError(
                f"El carácter '{char}' no está definido"
            )

        pattern = FONT[char]

        with canvas(self.device) as draw:

            for y, row in enumerate(pattern):

                for x, pixel in enumerate(row):

                    if pixel == "1":
                        draw.point(
                            (x + 1, y),
                            fill="white"
                        )

    def text(self, text):
        """
        Muestra texto estático.

        Actualmente solo muestra los caracteres
        que caben en la matriz.
        """

        text = text.upper()

        with canvas(self.device) as draw:

            x_offset = 0

            for char in text:

                if char not in FONT:
                    continue

                pattern = FONT[char]

                for y, row in enumerate(pattern):

                    for x, pixel in enumerate(row):

                        x_pos = x + x_offset

                        if (
                            pixel == "1"
                            and 0 <= x_pos < self.WIDTH
                        ):
                            draw.point(
                                (x_pos, y),
                                fill="white"
                            )

                x_offset += 6

                if x_offset >= self.WIDTH:
                    break

    def number(self, number):
        """
        Muestra un número.
        """

        self.text(str(number))

    def scroll(self, text, delay=0.1):
        """
        Desplaza un texto horizontalmente.
        """

        text = text.upper()

        # Crear un bitmap suficientemente ancho
        width = len(text) * 6

        bitmap = [
            [False for _ in range(width)]
            for _ in range(self.HEIGHT)
        ]

        x_offset = 0

        for char in text:

            if char not in FONT:
                x_offset += 6
                continue

            pattern = FONT[char]

            for y, row in enumerate(pattern):

                for x, pixel in enumerate(row):

                    if pixel == "1":

                        bitmap[
                            y
                        ][
                            x + x_offset
                        ] = True

            x_offset += 6

        # Scroll
        for offset in range(width + self.WIDTH):

            with canvas(self.device) as draw:

                for y in range(self.HEIGHT):

                    for x in range(self.WIDTH):

                        source_x = x + offset

                        if (
                            0 <= source_x < width
                            and bitmap[y][source_x]
                        ):
                            draw.point(
                                (x, y),
                                fill="white"
                            )

            sleep(delay)
