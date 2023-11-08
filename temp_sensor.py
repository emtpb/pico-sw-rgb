"""
Helper module to determine the actual temperature of the microcontroller
"""
from machine import ADC


def get_temp():
    """
    Use the internal temperature sensor and ADC to determine the actual
    temperature of the microcontroller

    Returns:
        float: temperature in °C
    """
    # Initialize ADC
    sensor = ADC(4)
    conversion_factor = 3.3 / 65535

    # Read temperature sensor
    tp_dec = sensor.read_u16()

    # Convert to voltage
    voltage = tp_dec * conversion_factor

    # Convert voltage to temperature (Reference Voltage is at 27°C)
    temperature = 27 - ((voltage - 0.706) / 0.001721)

    return round(temperature, 2)


def print_temp():
    """Prints the formatted temperature value"""
    print("Temperature: " + str(get_temp()) + " °C")
