import time
from spidev import SpiDev

from RPi import GPIO
from datacom.week05 import MCP3008

MAX7219_REG_NOOP = 0x0
MAX7219_REG_DECODE_MODE = 0x9
MAX7219_REG_INTENSITY = 0xA
MAX7219_REG_SCAN_LIMIT = 0xB
MAX7219_REG_SHUTDOWN = 0xC
MAX7219_REG_DISPLAY_TEST = 0xF

DOG = [0x42, 0x66, 0xFF, 0xDB, 0x7E, 0x7E, 0x3C, 0x18]
QUESTION_MARK = [0xC3, 0x99, 0xF9, 0xF3, 0xE7, 0xFF, 0xE7, 0xFF]
BLANK = [0] * 8
CIRCLE = [0x00, 0x3C, 0x7E, 0x66, 0x66, 0x7E, 0x3C, 0x00]
ARROW_UP = [0x00, 0x18, 0x3C, 0x7E, 0x18, 0x18, 0x18, 0x18]
ARROW_RIGHT = [0x00, 0x08, 0x0C, 0xFE, 0xFE, 0x0C, 0x08, 0x00]
ARROW_DOWN = [0x18, 0x18, 0x18, 0x18, 0x7E, 0x3C, 0x18, 0x00]
ARROW_LEFT = [0x00, 0x10, 0x30, 0x7F, 0x7F, 0x30, 0x10, 0x00]
ARROW_DOWN_LEFT = [0x00, 0x00, 0x0C, 0x1C, 0xB8, 0xF0, 0xE0, 0xF0]
ARROW_UP_LEFT = [0xF0, 0xE0, 0xF0, 0xB8, 0x1C, 0x0C, 0x00, 0x00]
ARROW_UP_RIGHT = [0x0F, 0x07, 0x0F, 0x1D, 0x38, 0x30, 0x00, 0x00]
ARROW_DOWN_RIGHT = [0x00, 0x00, 0x30, 0x38, 0x1D, 0x0F, 0x07, 0x0F]


# STAPPENPLAN: ZIE SYLLABUS!

class MAX7219:
    """Class representing a MAX7219 BCD decoder & LED driver"""

    def __init__(self, bus=0, device=0):
        """
        Initialize SPI device
        :param bus: SPI bus (usually 0)
        :param device: SPI slave (SS/CS/CE)
        """
        self.spi = SpiDev()
        ...

    def set_test_mode(self, value: bool = True):
        ...

    def set_intensity(self, value):
        ...

    def set_decode_mode(self, value):
        ...

    def set_scan_limit(self, value):
        ...

    def set_shutdown(self, value: bool):
        ...

    def initialize_led_matrix(self):
        ...

    def write_row(self, row, value):
        ...

    def write_matrix(self, data):
        ...

    def blank(self):
        ...


class AnalogJoystick:
    def __init__(self, mcp: MCP3008, ch_x=0, ch_y=1, sw_pin=17):
        self.mcp = mcp
        self.ch_x = ch_x
        self.ch_y = ch_y
        self.sw_pin = sw_pin

    @property
    def x(self):
        return ...

    @property
    def y(self):
        return ...

    def on_press(self, callback):
        ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je jouw functies/klassen oproepen om ze te testen
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.setwarnings(False)  # get rid of warning when no GPIO pins set up
        GPIO.cleanup()


if __name__ == '__main__':
    main()
