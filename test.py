import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

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

string = []

while True:
    text = input("$")
    string.append(text)

    oled.fill(0)

    if len(string) < 8:
        for row in range(0, len(string)):
            oled.text(string[row], 0, row*8, 1)
    else:
        for row in range(0, 8):
            oled.text(string[len(string) - (8 - row)], 0, row*8, 1)

    oled.show()
