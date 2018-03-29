from datetime import time, date

from RPi import GPIO
from smbus import SMBus

DS1307_DEFAULT_ADDRESS = 0x68

DS1307_REG_SECONDS = 0x0
DS1307_REG_MINUTES = 0x1
DS1307_REG_HOURS = 0x2
DS1307_REG_DAY = 0x3
DS1307_REG_DATE = 0x4
DS1307_REG_MONTH = 0x5
DS1307_REG_YEAR = 0x6
DS1307_REG_CONTROL = 0x7


def read_seconds_register():
    """
    Read the contents of the DS1307 SECONDS register, print the value in binary format, and return it
    :return: contents of the register (int)
    """
    ...


def bcd2int(value):
    """
    Convert 2-digit BCD to integer value
    :param value: BCD to convert (int)
    :return: BCD encoded number (int)
    """
    ...


def int2bcd(value):
    """
    Convert 2-digit value to BCD encoded byte
    :param value: number to convert (int)
    :return: BCD encoded number (int)
    """
    ...


def set_seconds_register(value):
    """
    Set the contents of the DS1307 SECONDS register
    :param value: new register value (int)
    :return: None
    """
    ...


class DS1307:
    def __init__(self, address=DS1307_DEFAULT_ADDRESS):
        self.i2c = SMBus(1)
        self.address = address

    @property
    def clock_enabled(self):
        """
        Check if the clock is enabled (Clock Halt bit is 0)
        :return: Clock status (boolean)
        """
        return ...

    @clock_enabled.setter
    def clock_enabled(self, value):
        """
        Set the value of the Clock Halt bit, leaving the other bits unchanged
        :param value: inverted clock halt bit (boolean)
        :return: None
        """
        ...

    def get_time(self) -> time:
        """
        Get the current time of the RTC
        :return: time object
        """
        return ...

    def set_time(self, value: time):
        """
        Set the current time of the RTC
        :param value: time object
        :return: None
        """
        ...

    def get_date(self) -> date:
        """
        SGt the current date of the RTC
        :return: date object
        """
        return ...

    def set_date(self, value: date):
        """
        Set the current date of the RTC
        :param value: date object
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
        GPIO.setwarnings(False)  # get rid of warning when no GPIO pins set up
        GPIO.cleanup()


if __name__ == '__main__':
    main()
