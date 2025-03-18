import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
import random as rd

# Button class for debouncing etc
# remember to upload Button.py file to pico
from Button import Button


sw0 = Button(9, 100)
sw1 = Button(8, 100)
sw2 = Button(7, 100)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

pos_x, pos_y = (int(oled_width/2), int(oled_height/2))

size = {"x": 25, "y": 25}

pixelpos = [(0, 0)]
count = 0

speed = -2
is_filled = False

while True:
    time.sleep_ms(200)
    oled.fill(0)

    size["x"] += speed

    if (size["x"] <= 0 or size["x"] >= 25):
        speed *= -1
        if (size["x"] <= 0):
            is_filled = not is_filled

    oled.ellipse(pos_x, pos_y, size["x"], size["y"], 1, is_filled)
    # oled.fill(0)
    oled.show()
