import time
from RPi import GPIO

from datacom.week02 import RGBLED


def onewire_tryout():
    # open het 'w1_slave'bestand voor jouw sensor:
    with open('/sys/bus/w1/devices/28-0417b29bccff/w1_slave') as f:
        # haal er er de juiste regel uit:
        ...
        # haal de waarde van t uit de regel:
        raw = ...
        # zet om naar int en deel door 1000:
        temp = ...
        # druk de temperatuur af met 1 cijfer na de komma:
        print(...)


class OneWire(object):
    MASTER_NAME = 'w1_bus_master1'
    BASE_PATH = '/sys/bus/w1/devices'

    @staticmethod
    def make_path(filename, device=MASTER_NAME):
        return '{}/{}/{}'.format(OneWire.BASE_PATH, device, filename)

    @staticmethod
    def slave_count():
        # Lees het bestand w1_master_slave_count in, zet de inhoud ervan om naar een int en return die
        ...

    @staticmethod
    def list_slaves():
        # Lees het bestand w1_master_slaves in. Het bevat 1 slave ID per regel. Return een 'list' van slave ID's
        ...

    @staticmethod
    def get_slave_data(slave_id, name):
        # Check eerst of de slave wel bestaat a.d.h.v. de methode list_slaves() die je net schreef.
        # Indien niet raise je een ValueError.
        ...

        # Open het bestand w1_slave voor deze slave en overloop elke regel. Als op de regel 'name=' voorkomt (waarbij
        # 'name' de inhoud van de parameter name is), return je de rest van de regel achter =.
        # Deze methode kunnen we dan straks gebruiken om de waarde 't' van onze temperatuursensor te lezen.
        ...
        raise ValueError("Variable {name} not found for slave ID {id}".format(name=name, id=slave_id))


class DS18B20:
    def __init__(self, slave_id):
        self.slave_id = slave_id

    def get_temperature(self):
        # haal de waarde van 't' op:
        data = ...
        # zet de data om naar een getal in graden Celcius voor je ze returnt
        return ...


def demo_onewire():
    # print het aantal en de id's van de gevonden slaves
    slave_count = ...
    slaves = ...
    print(...)

    # we gaan er voor het gemak van uit dat de eerste gevonden sensor de juiste is
    if slave_count > 0:
        sensor_address = slaves[0]

        # druk de temperatuur af met 1 cijfer na de komma:
        print(...)

        # druk de temperatuur af met 1 cijfer na de komma:
        thermometer = ...
        print(...)


class PwmPin:
    def __init__(self, pin, frequency=1000, duty_cycle=0):
        self.pin = pin
        self._duty_cycle = duty_cycle
        # Initialiseer de pin
        ...
        # Maak een PWM-object met de gegeven frequentie en start het met de gegeven duty cycle
        self._pwm = ...
        ...

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
    sensor = DS18B20(OneWire.list_slaves()[0])
    led = RGBLED(18, 23, 24)
    fan = DCMotor(26)
    heat = Heater(8)

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
    # Gebruik deze functie om je code te testen. Vergeet niet eerst de pinnumering in
    # te stellen, en achteraf op te ruimen!
    GPIO.setmode(GPIO.BCM)
    try:
        ...
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
