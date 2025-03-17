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

string = []

while True:
    text = input("$")
    string.append(text)

    for i in string:
        oled.text(string, 0,0,1)
    oled.show()
