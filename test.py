import time
from machine import UART, Pin, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C

# Button class for debouncing etc
class Button:
    def __init__(self, pin, debounce_ms) -> None:
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.debounce_ms = debounce_ms
    
    def pressed(self) -> bool:
        if (not self.pin()):
            time.sleep_ms(self.debounce_ms)
            if (not self.pin()):
                return True
        return False

sw0 = Button(9, 100)
sw1 = Button(8, 100)
sw2 = Button(7, 100)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

ufo = "<=>"
ufo_size = len(ufo)*8

pos_x = int(oled_width/2 - ufo_size/2)
pos_y = oled_height - 8
oled.text(ufo, pos_x, pos_y, 1)
speed = 5

while True:

    # move to the right
    if (sw2.pressed()):
        oled.fill(0)
        if pos_x < 123 - ufo_size:
            pos_x += speed
        oled.text("<=>", pos_x, pos_y, 1)

    # move to the left
    if (sw0.pressed()):
        oled.fill(0)
        if pos_x > 5:
            pos_x -= speed
        oled.text("<=>", pos_x, pos_y, 1)

    oled.show()
