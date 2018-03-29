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
    ...


def int2bcd(value):
    ...


def bcd2int(value):
    ...


class DS1307:
    def __init__(self, address=DS1307_DEFAULT_ADDRESS):
        ...

    @property
    def clock_enabled(self):
        return ...

    @clock_enabled.setter
    def clock_enabled(self, value):
        ...

    def get_time(self):
        ...

    def set_time(self):
        ...

    def get_date(self):
        ...

    def set_date(self):
        ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je jouw functies/klassen oproepen om ze te testen
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.setwarnings(False)     # get rid of warning when no GPIO pins set up
        GPIO.cleanup()


if __name__ == '__main__':
    main()
