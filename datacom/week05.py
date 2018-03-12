from RPi import GPIO
from spidev import SpiDev

# STAPPENPLAN: ZIE SYLLABUS!

from datacom.week03v3 import PwmPin


# 3) Testapplicatie
def read_trimmer(device=0):
    """Read a value from CH0 on MCP3008 slave <device> and print it to console.
    :param device: SPI slave (SS/CE/CS: 0 or 1 for standard RPi 3)
    """
    ...


# 4) meetwaarde omzetten
def value_to_volts(value):
    """Convert a 10-bit measurement to an analog voltage
    :param value: ADC measurement (0-1023)
    :return: Analog voltage (0 - 3.3)
    """
    return ...


def value_to_percent(value):
    """Convert a 10-bit measurement to a percentage
    :param value: ADC measurement (0-1023)
    :return: Percentage with 1 decimal (0.0 - 100.0)
    """
    return ...


# 5) Klasse voor de ADC
class MCP3008:
    """Class representing an MCP3008 ADC"""
    def __init__(self, bus=0, device=0):
        """
        Initialize SPI device for MCP3008
        :param bus: SPI bus (usually 0)
        :param device: SPI slave (SS/CS/CE)
        """
        ...

    def read_channel(self, ch):
        """
        Perform measurement on an ADC channel
        :param ch: ADC channel (0-7)
        :return: 10-bit integer measurement (0-1023)
        """
        ...


# 6) Servomotor
class ServoMotor(PwmPin):
    def __init__(self, pin):
        """Initialize PWM pin for servo motor
        :param pin: GPIO pin for servo control signal
        """
        ...

    def set_angle(self, value):
        """Set servo motor angle
        :param value: angle (-90 -> 90 deg.)
        """
        if not -90 <= value <= 90:
            raise ValueError('Servo angle must be between -90 and 90 degrees')
        self.duty_cycle = ...


def value_to_angle(value):
    """Convert a 10-bit measurement to a servo angle
    :param value: ADC measurement (0-1023)
    :return: Servo angle (-90 -> 90 deg.)
    """
    return ...


# Hier kan je jouw functies/klassen oproepen om ze te testen
def main():
    GPIO.setmode(GPIO.BCM)
    try:
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.setwarnings(False)     # get rid of warning when no GPIO pins set up
        GPIO.cleanup()


if __name__ == '__main__':
    main()
