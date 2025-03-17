from machine import UART, Pin, I2C, Timer, ADC
import time

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