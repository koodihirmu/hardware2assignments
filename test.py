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

pos_x, pos_y = (0, int(oled_height/2))

while True:

    # check inputs
    if (sw0.pressed()):
        pos_y += 1
    if (sw1.pressed()):
        pos_x += 1
    if (sw2.pressed()):
        pos_y -= 1

    # use modulo for wrapping the lines
    oled.pixel(pos_x % oled_width, pos_y % oled_height, 1)

    oled.show()
