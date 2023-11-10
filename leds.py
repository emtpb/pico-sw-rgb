"""
Module for handling LED functionality
"""
from machine import Pin, PWM

# Mapping of leds and GPIOs
D1_RED_PIN = 27
D1_GREEN_PIN = 26
D1_BLUE_PIN = 22
D2_RED_PIN = 21
D2_GREEN_PIN = 20
D2_BLUE_PIN = 19


class Leds:
    """Simple helper class for managing leds on EMT's additional led board"""
    def __init__(self):
        """Initialize all led gpios as pwm"""
        self.red_top = PWM(Pin(D1_RED_PIN))
        self.red_top.freq(1000)

        self.green_top = PWM(Pin(D1_GREEN_PIN))
        self.green_top.freq(1000)

        self.blue_top = PWM(Pin(D1_BLUE_PIN))
        self.blue_top.freq(1000)

        self.red_bottom = PWM(Pin(D2_RED_PIN))
        self.red_bottom.freq(1000)

        self.green_bottom = PWM(Pin(D2_GREEN_PIN))
        self.green_bottom.freq(1000)

        self.blue_bottom = PWM(Pin(D2_BLUE_PIN))
        self.blue_bottom.freq(1000)

        self.leds = [self.red_top, self.green_top, self.blue_top,
            self.red_bottom, self.green_bottom, self.blue_bottom]

    @staticmethod
    def set_pwm(led: object, duty_cycle: float):
        """
        Sets the duty cycle for a led gpio

        Args:
            led (obj): Led object
            duty_cycle (float): Value must be in the range from 1 to 0
        """
        if duty_cycle > 1 or duty_cycle < 0:
            return

        # 65535 is the max duty cicle.
        # This value turns the led off so brightness has to be inverted.
        dc = int(65535 - (65535 * duty_cycle))
        led.duty_u16(dc)


    def mix_color(self, d1_red_dc: float, d1_green_dc: float, d1_blue_dc: float,
        d2_red_dc: float, d2_green_dc: float, d2_blue_dc: float):
        """
        Sets the duty cycle for every led gpio

        Args:
            d1_red_dc (float): Duty cycle for red top LED
            d1_green_dc (float): Duty cycle for green top LED
            d1_blue_dc (float): Duty cycle for blue top LED
            d2_red_dc (float): Duty cycle for red bottom LED
            d2_green_dc (float): Duty cycle for green bottom LED
            d2_blue_dc (float): Duty cycle for blue bottom LED
        """
        self.set_pwm(self.red_top, d1_red_dc)
        self.set_pwm(self.green_top, d1_green_dc)
        self.set_pwm(self.blue_top, d1_blue_dc)
        self.set_pwm(self.red_bottom, d2_red_dc)
        self.set_pwm(self.green_bottom, d2_green_dc)
        self.set_pwm(self.blue_bottom, d2_blue_dc)


    def set_all(self, duty_cycle):
        """
        Sets all led gpios to one specific duty cycle
        """
        self.set_pwm(self.red_top, duty_cycle)
        self.set_pwm(self.green_top, duty_cycle)
        self.set_pwm(self.blue_top, duty_cycle)
        self.set_pwm(self.red_bottom, duty_cycle)
        self.set_pwm(self.green_bottom, duty_cycle)
        self.set_pwm(self.blue_bottom, duty_cycle)
