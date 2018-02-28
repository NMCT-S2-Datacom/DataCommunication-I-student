# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# HOUD JE STRIKT AAN DE NAAMGEVING EN GEBRUIKTE PINNUMMERS UIT DE OPGAVE
# DE EXPRESSIE ... DIENT ALS PLAATSHOUDER EN MOET JE VERVANGEN DOOR EIGEN CODE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import time
from RPi import GPIO

# We zullen de klasse Button en LED van vorige week uitbreiden, daarom importeren we ze onder een andere naam:
from .week01 import LED as BaseLED, Button as BaseButton


# 1) Schrijf een klasse Button die erft van de klasse van vorige week:
class Button:
    # a) de init-methode krijgt een extra parameter 'bouncetime' met defaultwaarde None,
    # die wordt bijgehouden in een protected member.
    ...

    # b) overschrijf de methode wait_for_press zodat gebruik gemaakt wordt van de functionaleit van de library.
    # Voeg ook een parameter ' timeout' toe met defaultwaarde None
    ...

    # c) voeg een methode on_press toe, die een callbackfunctie aanneemt om
    # op te roepen wanneer op de knop gedrukt wordt. Hou rekening met de bouncetime uit de klassevariabele.
    ...

    # c) voeg een methode on_release toe, die een callbackfunctie aanneemt om
    # op te roepen wanneer op de knop losgelaten wordt. Hou rekening met de bouncetime uit de klassevariabele.
    ...


def demo_button():
    # Initialiseer de twee Buttons met een bouncetime van 20ms
    #btn1, btn2 = ...
    #yup
    # Wanneer op een van de knoppen gedrukt wordt, wordt er een boodschap afgedrukt op het scherm
    ...

    time.sleep(60)  # geeft je 60sec om te testen


# 2) Schrijf een klasse LED die erft van de klasse van vorige week:
class LED(BaseLED):
    # a) de init-methode krijgt een extra parameter 'brightness' met standaardwaarde 100,
    # die wordt bijgehouden in een protected member.
    # De protected variabele 'pwm' houdt een extra PWM-object bij met frequentie 1kHz.
    ...

    # b) De klasse heeft een (read/write) property 'brightness'.
    ...

    # c) In de setter wordt meteen ook de duty cycle van het PWM-object ingesteld. Als de waarde buiten
    # het bereik 0-100 valt, wordt een ValueError gegenereerd.
    ...

    # d) de methodes on en off moet je overschrijven: in plaats van naar de pin te schrijven,
    # starten en stoppen we nu het PWM-signaal
    ...

    # e) de speciale methode __del__ is de tegenhanger van __init__ en
    # wordt opgeroepen wanneer de klasse wordt afgebroken. Hier roepen we
    # de stop-methode van het PWM-object aan zodat alles netjes wordt opgekuist
    ...


def demo_led():
    # Initialiseer de LED op pin 25 op halve intensiteit
    ...

    while True:
        # lees een intensiteitswaarde in van de gebruiker en stel de LED daarop in. Bij een
        # ongeldige waarde stopt de functie
        ...


# 3) Maak een klasse RGBLED
class RGBLED:
    # a) de init-methode krijgt 3 parameters; 'red', 'green', 'blue' mee die verwijzen naar de resp. pinnummers waarop
    # de RGB-LED is aangesloten. Je maakt 3 overeenkomstige klassevariabelen waarin je telkens een LED-object
    # initialiseert op de overeenkomstige pin, en met brightness 0
    ...

    # b) de methode set_color heeft 3 parameters; r, g, b; die samen een kleur voorstellen (0-255). Reken deze om naar
    # een brightness-waarde (0-100) en stel die in op de respectievelijke LEDs
    ...


def demo_rgb():
    # Initialiseer de twee Buttons
    ...

    # Initialiseer de RGB-led
    ...

    # Wanneer je op de eerste knop drukt, krijgt de LED een willekeurige nieuwe kleur
    ...


# 4) Maak een klasse LEDBar
class LEDBar:
    # a) de init-methode heeft een speciaal argument: *args. Hiermee kan je zoveel argumenten meegeven als je wil.
    # De bedoeling is dat je een lijst van pinnummers kan meegeven, aan de hand daarvan wordt een klassevariabele
    # 'leds' geïnitialiseerd met een list van LED-objecten
    ...

    # b) de functie set_value() heeft een parameter 'value' die het aantal LEDs bepaalt die moeten branden.
    # Als de waarde kleiner is dan 0, of groter dan het aantal LEDs in self.leds, wordt een ValueError gegenereerd.
    # Vervolgens schrijf je een loop om het overeenkomstig aantal LEDs te laten branden.
    ...

    # c) De functie set_percent heeft eveneens een parameter 'value'. Indien die kleiner dan 0 of groter dan 100 is,
    # genereer je opnieuw een ValueError. Vervolgens reken je het percentage om naar het kortstbijliggend aantal LEDs
    # en roep je daarmee de methode set_value aan.
    ...


def demo_ledbar():
    # Maak een LEDBar met de 5 LEDs die je hebt aangesloten
    ...

    # stel de maximumwaarde in voor 1 sec:
    ...

    # stel de minimumwaarde (0) in voor 1 sec:
    ...

    # stel in op 50% voor 1 sec:
    ...

    # stel in op 20% voor 1 sec:
    ...


def main():
    # Gebruik deze functie om je code te testen. Vergeet niet eerst de pinnumering in
    # te stellen, en achteraf op te ruimen!
    ...


if __name__ == '__main__':
    main()
