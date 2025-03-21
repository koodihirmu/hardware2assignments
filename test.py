import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from filefifo import Filefifo as ff

# Button class for debouncing etc
# remember to upload Button.py file to pico
from Button import Button

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

pos_x, pos_y = (int(oled_width/2), int(oled_height/2))

# upload capture files to pico too
data = ff(10, name="capture_250Hz_01.txt")

max = 0
min = 50000

# two seconds of data at 250/s
for samples in range(1, 2 * 250):
    value = data.get()

    if value > max:
        max = value

    if value < min:
        min = value

# 10 seconds of the data and draw it on pico
for samples in range(0, 10 * 250):
    value = data.get()

    max_scale = 32
    time_scale = 0.50

    # scale the value between 0 and 100 or whatever we want
    scaled_value = (value - min)/(max - min) * max_scale

    # show the pixels every time the screen if filled with the data
    if ((samples * time_scale) % oled_width == 0) and samples != 0:
        oled.show()
        oled.fill(0)

    # draw the pixels on the screen
    oled.pixel(int(samples * time_scale) % (oled_width), pos_y +
               int(scaled_value - max_scale/2), 1)
