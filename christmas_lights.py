import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)                                         # Disables warnings
GPIO.setmode(GPIO.BOARD)                                        # Sets the BOARD numbering system


def setup():                                                    # Setup of the LEDs and the button
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
    GPIO.setup(red_led_1, GPIO.OUT, initial=GPIO.LOW)           # GPIO.OUT: configures a channel as output
    GPIO.setup(red_led_2, GPIO.OUT, initial=GPIO.LOW)           # GPIO.LOW: set the output state
    GPIO.setup(yellow_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(yellow_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(blue_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(green_led_2, GPIO.OUT, initial=GPIO.LOW)         # GPIO.IN: configures a channel as input
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)       # GPIO.PUD_UP: it is equal to "True"
    n = 0


def all_lights():                                               # This effect lights up all LEDs
    while GPIO.input(button) == True:                           # When the button is pressed, the input becomes "False"
        time.sleep(0.01)                                        # When it is released, the input becomes "True" again
        GPIO.output(red_led_1, True)
        GPIO.output(red_led_2, True)
        GPIO.output(blue_led_1, True)
        GPIO.output(blue_led_2, True)
        GPIO.output(yellow_led_1, True)
        GPIO.output(yellow_led_2, True)
        GPIO.output(green_led_1, True)
        GPIO.output(green_led_2, True)
    return 1                                                    # Returns the number of the next effect


def all_lights_blinking():                                      # This effect makes all LEDs blink
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


def warm_and_cold():                                            # This effect makes either red and yellow LEDs or
    while GPIO.input(button) == True:                           # blue and green LEDs blink
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


def same_colour():                                              # This effect lights up two LEDs of the same colour,
    while GPIO.input(button) == True:                           # one colour at a time
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


def one_at_once():                                              # This effect lights up just one LED at a time
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
            if n == 0:                                          # Each effect has its own number [0, 4]
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
except KeyboardInterrupt:                                       # Press Ctrl + C to turn off the lights
    GPIO.cleanup()                                              # Cleans up GPIO channels that the script has used
