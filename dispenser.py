from time import sleep
import RPi.GPIO as GPIO

DIR = 20
PUL = 21
ENA = 16
SPR = 6400
CLOCK_WISE = 1
COUNTER_CLOCK_WISE = 0
DELAY = 0.000001
STEPS = 8000
SLEEP_TIME = 0.5

class Dispenser:
    def __init__(self):
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PUL, GPIO.OUT)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(ENA, GPIO.OUT)

    def enable_engine(self):
        GPIO.output(ENA, GPIO.HIGH)

    def disable_engine(self):
        GPIO.output(ENA, GPIO.LOW)

    def spin(self, steps, delay, direction):
        GPIO.output(DIR, direction)
        for x in range(steps):
            GPIO.output(PUL, GPIO.HIGH)
            sleep(delay)
            GPIO.output(PUL, GPIO.LOW)
            sleep(delay)

    def dispense_food(self):
        self.spin(STEPS, DELAY, CLOCK_WISE)
        sleep(SLEEP_TIME)
        self.spin(STEPS, DELAY, COUNTER_CLOCK_WISE)
