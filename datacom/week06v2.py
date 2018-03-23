import time
from RPi import GPIO


# GEWIJZIGDE VERSIE: In SevenSegment is de methode show_number opgesplitst in show_segments en show_digit om
# de klasse beter uitbreidbaar te maken (nodig voor de opdracht over de paasvakantie)

# default pin numbers (BCM) - pas aan indien nodig
DS = 5  # serial data
OE = 6  # output enable (active low)
STCP = 13  # storage register clock pulse
SHCP = 19  # shift register clock pulse
MR = 26  # master reset (active low)

# timing - pas aan indien nodig
FREQ = 1e7  # 10 MHz
PERIOD = 1 / FREQ
DELAY = PERIOD / 2  # T_low, T_high = 1/2 periode


# 1) Testapplicatie
class ShiftRegister:
    def __init__(self, ds_pin=DS, shcp_pin=SHCP, stcp_pin=STCP, mr_pin=MR, oe_pin=OE):
        """
        Initialize pins and shift register
        :param ds_pin: DS pin number
        :param shcp_pin: SHCP pin number
        :param stcp_pin: STCP pin number
        :param mr_pin: MR pin number
        :param oe_pin: OE pin number
        """
        self.ds_pin = ds_pin
        self.shcp_pin = shcp_pin
        self.stcp_pin = stcp_pin
        self.mr_pin = mr_pin
        self.oe_pin = oe_pin
        ...

    def write_bit(self, value):
        """
        Write a single bit to the shift register
        :param value: 0 or 1
        :return: None
        """
        ...

    def copy_to_storage_register(self):
        """
        Copy contents of shift register to storage register
        :return: None
        """
        ...

    def write_byte(self, value):
        """
        Write 8 bits from <value> to shift register, MSB first
        :param value: byte (0-255)
        :return: None
        """
        ...

    # De rest v/d klasse is afwerking voor achteraf
    def reset_shift_register(self):
        """
        Reset the shift register (leaves storage register intact)
        :return: None
        """
        ...

    def reset_storage_register(self):
        """
        Reset both shift and storage registers
        :return: None
        """
        ...

    @property
    def output_enabled(self):
        return ...

    @output_enabled.setter
    def output_enabled(self, value):
        ...


def shiftreg_demo():
    """
    Light each display segment one by one in 1 sec intervals
    :return: None
    """
    shreg = ShiftRegister()
    value = 1
    while value < 0xff:
        shreg.write_byte(value)
        shreg.copy_to_storage_register()
        time.sleep(1)
        value <<= 1


# Juiste bit voor elk segment: vul/pas aan
A = 1 << 0
B = 1 << 1
C = 1 << 2
...
DP = 1 << 7

# Juist segment voor elk (hex) cijfer: vul/pas aan
SEGMENTS = {

    0x1: B | C,

    0x7: A | B | C,

    0xF: ...
}


class SevenSegment:
    def __init__(self, shreg: ShiftRegister):
        self.shreg = shreg

    def show_segments(self, value):
        """
        Light segments on the display
        :param value: byte where bits correspond to segments
        :return: None
        """
        ...

    def show_digit(self, value, with_dp=False):
        """
        Show dec/hex number on the display
        :param value: digit(int) (0-0xF)
        :param with_dp: (boolean) show decimal point
        :return: None
        """
        ...


def seven_segment_demo():
    """
    Show each number (0-0xF) one by one in 1 sec intervals
    :return: None
    """
    shreg = ShiftRegister()
    display = SevenSegment(shreg)
    for i in range(17):
        display.show_digit(i)
        time.sleep(1)


class SevenSegmentCascade(SevenSegment):
    def show_list(self, values):
        """
        Show a list of bytes on any number of displays
        """
        ...

    def show_hex_digits(self, value):
        """
        Show <value> as hexadecimal number on any number of displays
        :param value: integer
        :return: None
        """
        ...

    def show_dec_digits(self, value):
        """
        Show <value> in base 10 on any number of displays
        :param value: integer
        :return: None
        """
        ...

    def show_float(self, value):
        """
        Show <value> with one decimal digit (eg. 4.2)
        :param value: float
        :return: None
        """
        ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je jouw functies/klassen oproepen om ze te testen
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
