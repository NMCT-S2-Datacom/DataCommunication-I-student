import time
from RPi import GPIO

from datacom.week02 import RGBLED


def get_temperature(slave_id):
    # open het 'w1_slave' bestand voor de sensor:
    ...
    # haal er er de juiste regel uit:
    ...

    # haal de waarde van t uit de regel:
    ...
    # zet om naar int en deel door 1000 alvorens de waarde te returnen
    return ...


class PwmPin:
    def __init__(self, pin, frequency=1000, duty_cycle=0):
        self.pin = pin
        self._duty_cycle = duty_cycle
        # Initialiseer de pin
        ...
        # Maak een PWM-object met de gegeven frequentie en start het met de gegeven duty cycle
        self._pwm = ...

    @property
    def duty_cycle(self):
        return self._duty_cycle

    # c) In de setter wordt meteen ook de duty cycle van het PWM-object ingesteld. Als de waarde buiten
    # het bereik 0-100 valt, wordt een ValueError gegenereerd.
    @duty_cycle.setter
    def duty_cycle(self, value):
        ...
        self._duty_cycle = value
        ...

    def on(self):
        self._pwm.start(self._duty_cycle)

    def off(self):
        self._pwm.stop()

    def __del__(self):
        self._pwm.stop()


class DCMotor(PwmPin):
    speed = PwmPin.duty_cycle


class Heater(PwmPin):
    heat = PwmPin.duty_cycle


def thermostat():
    led = RGBLED(18, 23, 24)
    fan = DCMotor(26)
    heat = Heater(8)

    slave_id = ...
    hysteresis = 1
    set_point = ...

    # Stuur de ventilator en verwarming aan:
    # - als de temperatuur te hoog is, zet je de verwarming uit en de ventilator aan
    # - als de temperatuur te laag is, zet je de verwarming aan en de ventilator uit
    # - anders is de temperatuur goed en zet je allebei uit
    ...

    # CHALLENGE: geef de toestand van de hysterese weer op de RGB-LED:
    # Ondergrens bereikt = 100% blauw
    # Perfecte temperatuur = paars (50% rood, 50% blauw)
    # Bovengrens bereikt = 100% rood
    # Daartussen is er een geleidelijke overgang van blauw naar rood
    ...


def main():
    GPIO.setmode(GPIO.BCM)
    try:
        # Hier kan je functies oproepen om te testen:
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
