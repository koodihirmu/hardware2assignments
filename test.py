import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

button = Pin(9, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0)
oled.text('Hello World', 0, 0, 1)
oled.show()
oled.fill(0)
oled.text('Button pressed', 0, 10, 1)

while button() == 1:
    time.sleep(0.05)
    oled.show()
