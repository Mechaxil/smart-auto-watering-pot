from machine import Pin, ADC
from time import sleep

adc = ADC(Pin(0))  # Change this to the GPIO pin connected to the sensor OUT for example GPIO0 on ESP32-C3

while True:
    print(adc.read_u16())
    sleep(1)