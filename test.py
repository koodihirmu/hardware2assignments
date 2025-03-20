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

timestamp = 0
point = 0
tolerance = 0.05
is_pos = True
peaks = []

for samples in range(1, 1000):
    new_point = int(data.get())
    new_timestamp = samples/250

    # calculate slope
    slope = (new_point - point)/(new_timestamp - timestamp)

    timestamp = new_timestamp
    point = new_point

    if is_pos and slope < 0:
        peaks.append((point, timestamp, samples,))
        is_pos = False

    if not is_pos and slope > 0:
        is_pos = True

if len(peaks) > 0:
    # calculate frequency t/peaks
    signal_frequency = len(peaks) / (peaks[-1][1] - peaks[0][1])
    # get the delta sample part of the tuple
    number_of_samples = peaks[-1][2] - peaks[0][2]
    # get the delta seconds part of the tuple
    seconds = peaks[-1][1] - peaks[0][1]

    print(f"Frequency of the signal: {signal_frequency} Hz")
    print(f"Samples considered: {number_of_samples}")
    print(f"Seconds: {seconds}")
