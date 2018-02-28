from RPi import GPIO
import time

led = 13 #check pinnumers
button = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)



print("programma is running")
try:
    #pollen voortdurend controleren of er op knop gedrukt worden
    # while True:
    #     button_status = GPIO.input(button)
    #     print("knopstatus is : {0}".format(button_status))
    #     time.sleep(0.1)  #pi krijgt wat tijd om andere zaken te doen
    #     if not button_status:
    #         GPIO.output(led,GPIO.HIGH)
    #         print("aan")
    #     else:
    #         GPIO.output(led,GPIO.LOW)
    #         print("uit")

    #wait for edge() function
    # print("app wacht op rising edge")
    # GPIO.wait_for_edge(button,GPIO.RISING,timeout=5000)  #app wacht 5s en gaat dan verder
    # print("er is op de knop gedrukt")


    #the event detected() function
    #voordeel onmiddellijk toggle button
    #nadeel while True:
    # GPIO.add_event_detect(button,GPIO.FALLING)
    # while True:
    #     status = GPIO.event_detected(button)
    #     print(status)
    #     time.sleep(0.3)
    def toggle_led(pinnummer):
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.008)
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.002)
        print("toggle")
        print(pinnummer)

    #Threaded callback

    #GPIO.add_event_callback(toggle_led())
    # GPIO.add_event_detect(button,GPIO.FALLING,toggle_led ,bouncetime=50)
    #
    # time.sleep(20)

    #pwm pin
    pwm = GPIO.PWM(led,1000) #frequentie van de blokgolf van mijn pwm signaal
    pwm.start(50) #blokgolf 50% van de tijd hoog staan
    print(50)
    time.sleep(2)
    pwm.ChangeDutyCycle(100)
    print(100)
    time.sleep(2)
    pwm.ChangeDutyCycle(20)
    print(20)
    time.sleep(2)

    time.sleep(5)

except KeyboardInterrupt:
    pass
finally:
    print("einde programma")
    GPIO.cleanup()