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

for samples in range(1, 10 * 250):
    value = data.get()

    max_scale = 32
    time_scale = 0.2

    # scale the value between 0 and 100 or whatever we want
    scaled_value = (value - min)/(max - min) * max_scale

    # show the pixels on the screen
    oled.pixel(int(samples * time_scale) % 128, pos_y +
               int(scaled_value - max_scale/2), 1)

    if not (samples % 50):
        oled.show()

    if (samples * time_scale) % oled_width == 0:
        oled.fill(0)

    print(scaled_value)
