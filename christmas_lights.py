import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def setup():
    global red_led_1, red_led_2, yellow_led_1, yellow_led_2
    global blue_led_1, blue_led_2, green_led_1, green_led_2
    global button, n
    red_led_1 = 31
    red_led_2 = 40
    yellow_led_1 = 35
    yellow_led_2 = 36
    blue_led_1 = 33
    blue_led_2 = 38
    green_led_1 = 37
    green_led_2 = 32
    button = 16
    GPIO.setup(red_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(yellow_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(yellow_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    n = 0


def all_lights():
    while GPIO.input(button) == True:
        time.sleep(0.01)
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, True)
        GPIO.output(blue_led_1, True)
        GPIO.output(blue_led_2, True)
        GPIO.output(yellow_led_1, True)
        GPIO.output(yellow_led_2, True)
        GPIO.output(green_led_1, True)
        GPIO.output(green_led_2, True)
    return 1


def all_lights_blinking():
    while GPIO.input(button) == True:
        time.sleep(0.01)
        GPIO.output(red_led_1, False)
        GPIO.output(red_led_2, False)
        GPIO.output(blue_led_1, False)
        GPIO.output(blue_led_2, False)
        GPIO.output(yellow_led_1, False)
        GPIO.output(yellow_led_2, False)
        GPIO.output(green_led_1, False)
        GPIO.output(green_led_2, False)
        time.sleep(0.5)
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, True)
        GPIO.output(blue_led_1, True)
        GPIO.output(blue_led_2, True)
        GPIO.output(yellow_led_1, True)
        GPIO.output(yellow_led_2, True)
        GPIO.output(green_led_1, True)
        GPIO.output(green_led_2, True)
        time.sleep(0.5)
    return 2


def warm_and_cold():
    while GPIO.input(button) == True:
        time.sleep(0.01)
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, True)
        GPIO.output(yellow_led_1, True)
        GPIO.output(yellow_led_2, True)
        GPIO.output(blue_led_1, False)
        GPIO.output(blue_led_2, False)
        GPIO.output(green_led_1, False)
        GPIO.output(green_led_2, False)
        time.sleep(0.5)
        GPIO.output(red_led_1, False)
        GPIO.output(red_led_2, False)
        GPIO.output(yellow_led_1, False)
        GPIO.output(yellow_led_2, False)
        GPIO.output(blue_led_1, True)
        GPIO.output(blue_led_2, True)
        GPIO.output(green_led_1, True)
        GPIO.output(green_led_2, True)
        time.sleep(0.5)
    return 3


def same_colour():
    while GPIO.input(button) == True:
        time.sleep(0.01)
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, True)
        GPIO.output(blue_led_1, False)
        GPIO.output(blue_led_2, False)
        GPIO.output(yellow_led_1, False)
        GPIO.output(yellow_led_2, False)
        GPIO.output(green_led_1, False)
        GPIO.output(green_led_2, False)
        time.sleep(0.5)
        GPIO.output(red_led_1, False)
        GPIO.output(red_led_2, False)
        GPIO.output(blue_led_1, True)
        GPIO.output(blue_led_2, True)
        time.sleep(0.5)
        GPIO.output(blue_led_1, False)
        GPIO.output(blue_led_2, False)
        GPIO.output(yellow_led_1, True)
        GPIO.output(yellow_led_2, True)
        time.sleep(0.5)
        GPIO.output(yellow_led_1, False)
        GPIO.output(yellow_led_2, False)
        GPIO.output(green_led_1, True)
        GPIO.output(green_led_2, True)
        time.sleep(0.5)
    return 4


def one_at_once():
    while GPIO.input(button) == True:
        time.sleep(0.01)
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, False)
        GPIO.output(blue_led_1, False)
        GPIO.output(blue_led_2, False)
        GPIO.output(yellow_led_1, False)
        GPIO.output(yellow_led_2, False)
        GPIO.output(green_led_1, False)
        GPIO.output(green_led_2, False)
        time.sleep(0.5)
        GPIO.output(red_led_1, False)
        GPIO.output(blue_led_1, True)
        time.sleep(0.5)
        GPIO.output(blue_led_1, False)
        GPIO.output(yellow_led_1, True)
        time.sleep(0.5)
        GPIO.output(yellow_led_1, False)
        GPIO.output(green_led_1, True)
        time.sleep(0.5)
        GPIO.output(green_led_1, False)
        GPIO.output(red_led_2, True)
        time.sleep(0.5)
        GPIO.output(red_led_2, False)
        GPIO.output(blue_led_2, True)
        time.sleep(0.5)
        GPIO.output(blue_led_2, False)
        GPIO.output(yellow_led_2, True)
        time.sleep(0.5)
        GPIO.output(yellow_led_2, False)
        GPIO.output(green_led_2, True)
        time.sleep(0.5)
    return 0


try:
    if __name__ == "__main__":
        setup()
        while True:
            if n == 0:
                n = all_lights()
                time.sleep(1)
            elif n == 1:
                n = all_lights_blinking()
                time.sleep(1)
            elif n == 2:
                n = warm_and_cold()
                time.sleep(1)
            elif n == 3:
                n = same_colour()
                time.sleep(1)
            elif n == 4:
                n = one_at_once()
                time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()