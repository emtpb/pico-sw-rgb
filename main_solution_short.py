"""
Main function of the program.
"""
# Import libraries
from machine import Pin, PWM
import time
import leds
import temp_sensor as temp

# Turn all LED off
lds = leds.Leds()
lds.set_all(0)

# Set exercise
exercise = 0

if exercise == 1.2:
    d1_r = Pin(27, Pin.OUT)    # create output pin on GPIO27, D1 red here
    d1_r.value(0)


if exercise == 1.3:
    d1_r = Pin(27, Pin.OUT)    # create output pin on GPIO27, D1 red here
    while True:
        d1_r.value(0)
        time.sleep(0.5)
        d1_r.value(1)
        time.sleep(0.5)


if exercise == 1.4:
    d1_r = Pin(27, Pin.OUT)
    d1_g = Pin(26, Pin.OUT)
    d1_b = Pin(22, Pin.OUT)

    while True:
        d1_r.value(1)
        d1_g.value(0)
        d1_b.value(0)
        time.sleep(0.5)

        d1_r.value(0)
        d1_g.value(1)
        d1_b.value(0)
        time.sleep(0.5)

        d1_r.value(0)
        d1_g.value(0)
        d1_b.value(1)
        time.sleep(0.5)


if exercise == 2.2:
    d1_r_pin = Pin(27, Pin.OUT)
    d1_r_pwm = PWM(d1_r_pin)

    d1_r_pwm.duty_u16(63000)


if exercise == 2.3: # and 2.4
    # D1 orange
    d1_r_pin = Pin(27, Pin.OUT)
    d1_r_pwm = PWM(d1_r_pin)
    d1_r_pwm.duty_u16(10000)

    d1_g_pin = Pin(26, Pin.OUT)
    d1_g_pwm = PWM(d1_g_pin)
    d1_g_pwm.duty_u16(60000)

    # D2 purple
    d2_r_pin = Pin(21, Pin.OUT)
    d2_r_pwm = PWM(d2_r_pin)
    d2_r_pwm.duty_u16(30000)

    d2_b_pin = Pin(19, Pin.OUT)
    d2_b_pwm = PWM(d2_b_pin)
    d2_b_pwm.duty_u16(20000)


if exercise == 4:
    d1_r = Pin(27, Pin.OUT)
    d1_g = Pin(26, Pin.OUT)
    d1_b = Pin(22, Pin.OUT)
    while True:
        temp.print_temp()
        t = temp.get_temp()
        if (t > 30):
            d1_r.value(0)
            d1_g.value(1)
            d1_b.value(1)
        elif (t > 25):
            d1_r.value(0)
            d1_g.value(0)
            d1_b.value(1)
        elif (t > 20):
            d1_r.value(1)
            d1_g.value(0)
            d1_b.value(1)
        elif (t > 15):
            d1_r.value(1)
            d1_g.value(0)
            d1_b.value(0)
        else:
            d1_r.value(1)
            d1_g.value(1)
            d1_b.value(0)
        time.sleep(0.5)
