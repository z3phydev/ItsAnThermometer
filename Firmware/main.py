import time
import board
import analogio
import digitalio

sensor = analogio.AnalogIn(board.A0)

red = digitalio.DigitalInOut(board.D29)
red.direction = digitalio.Direction.OUTPUT

green = digitalio.DigitalInOut(board.D28)
green.direction = digitalio.Direction.OUTPUT

blue = digitalio.DigitalInOut(board.D27)
blue.direction = digitalio.Direction.OUTPUT

def get_voltage(pin):
    return (pin.value * 3.3) / 65535

while True:
    voltage = get_voltage(sensor)

    temp_c = voltage / 0.01

    if temp_c > 24:
        red.value = True
        green.value = False
        blue.value = False

    elif 21 <= temp_c <= 24:
        red.value = False
        green.value = True
        blue.value = False

    else:
        red.value = False
        green.value = False
        blue.value = True

    time.sleep(0.5)
