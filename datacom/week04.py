from RPi import GPIO
from serial import Serial


# STAPPENPLAN: ZIE SYLLABUS!

# 3) Testapplicatie
def serial_read(device, baud=9600):
    ...


# 5) Sensordata
def analog_print(device, baud=9600):
    ...


# 6) Een eenvoudig protocol
def analog_read(device, baud, pin):
    ...


# 7) klasse ArduinoSerial
class ArduinoSerial:
    def __init__(self, device, baud):
        ...

    def analog_read(self, pin):
        ...

    # CHALLENGE
    def analog_write(self, pin, value):
        ...

    def digital_read(self, pin):
        ...

    def digital_write(self, pin, value):
        ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je jouw functies/klassen oproepen om ze te testen
        for i in range(10):
            serial_read('/dev/serial1', 9600)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
