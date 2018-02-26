import time
from RPi import GPIO

from datacom.week02 import RGBLED, Button


class OneWire:
    MASTER_NAME = 'w1_bus_master1'
    BASE_PATH = '/sys/bus/w1/devices'

    @classmethod
    def make_path(cls, name):
        return '{}/{}/{}'.format(cls.BASE_PATH, cls.MASTER_NAME, name)

    @classmethod
    def slave_count(cls):
        # Lees het bestand w1_master_slave_count in, zet de inhoud ervan om naar een int en return die
        ...
        return ...

    @classmethod
    def list_slaves(cls):
        # Lees het bestand w1_master_slaves in. Het bevat 1 slave ID per regel. Return een 'list' van slave ID's
        ...
        return ...

    @classmethod
    def get_slave(cls, slave_id):
        # Check eerst of de slave wel bestaat a.d.h.v de methode list_slaves() die je net schreef.
        # Indien niet raise je een ValueError.
        ...
        return OneWire.Slave(cls.MASTER_NAME, slave_id)

    class Slave:
        def __init__(self, master, slave_id):
            self.master = master
            self.id = slave_id

        def get_data(self, name):
            path = '{base}/{master}/{id}/w1_slave'.format(base=OneWire.BASE_PATH,
                                                          master=self.master,
                                                          id=self.id)

            with open(path, 'r') as file:
                # Zoek in elke regel naar 'name='  (waarbij 'name' uiteraard
                # de waarde van die variabele is). Zo ja, return je de waarde ervan (het stuk achter de '=')
                # Hint: je zal dus de lengte van 'name' bij de gevonden positie moeten optellen, plus 1 voor de '='
                ...

            raise ValueError("Variable {} not found!")


def demo_onewire():
    slaves = OneWire.list_slaves()
    print('Found {} 1-wire slave(s): {}'.format(
        OneWire.slave_count(),
        ','.join(slaves)
    ))

    sensor = OneWire.get_slave(slaves[0])
    # Druk de waarde af die je uit het bestand gelezen hebt:
    print('Raw temperature data: ...')

    thermometer = DS18B20(slaves[0])
    # Druk de temperatuur correct af:
    print('The temperature is ...')


class DS18B20:
    def __init__(self, slave_id):
        self.driver = OneWire.get_slave(slave_id)

    def get_temperature(self):
        data = self.driver.get_data('t')
        # zet de data om naar een getal in graden Celcius voor je ze returnt
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

    @duty_cycle.setter
    def duty_cycle(self, value):
        # Als de waarde buiten het bereik 0-100 valt, wordt een ValueError gegenereerd.
        ...

        self._duty_cycle = value

        # Stel de duty-cycle van het PWM-object in
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


class Thermostat:
    def __init__(self, sensor: DS18B20, led: RGBLED, button: Button, fan: DCMotor, heat: Heater):
        ...


def demo_thermostat():
    ...


def main():
    # Gebruik deze functie om je code te testen. Vergeet niet eerst de pinnumering in
    # te stellen, en achteraf op te ruimen!
    GPIO.setmode(GPIO.BCM)
    try:
        demo_onewire()
        demo_thermostat()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
