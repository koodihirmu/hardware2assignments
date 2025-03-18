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

speed = -5
is_filled = False

while True:
    count = 0
    if sw0.pressed():
        flips = rd.randint(0, 10)
        while count < flips:
            time.sleep_ms(50)
            oled.fill(0)

            size["x"] += speed

            if (size["x"] <= 0 or size["x"] >= 25):
                speed *= -1
                if (size["x"] <= 0):
                    is_filled = not is_filled
                if (size["x"] >= 25):
                    count += 1

            oled.ellipse(pos_x, pos_y, size["x"], size["y"], 1, is_filled)
            # oled.fill(0)
            oled.show()
