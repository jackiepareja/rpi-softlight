import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledPin = 11
adc = ADCDevice()

def setup():
    global adc
    if(adc.dectectI2C(0x48)):
        adc = PCF8591()
    else:
        print("No correct I2C address is found");
        exit(-1)
    global p
    GPIO.setmod(GPIO.BOARD)
    GPIO.setup(ledPin,GPIO.OUT)
    p = GPIO.PWN(ledPin, 1000)
    p.start(0)

def loop():
    while True:
        value = adc.analogRead(0)
        p.ChangeDutyCycle(value*100/255) # Mapping the PWM duty cycle
        voltage = value / 255.0 * 3.3 # calculate the voltage value. > 3.3v from GPIO board.
        print ("ADC Value: %d, Voltage : %.2f" %(value, voltage))
        time.sleep(0.03)

def destroy():
    adc.close()

if __name__ == '__main__': 
    print ("Program is starting... ")
    try:
        setup()
        loop()
    except KeyboardInterrupt: # ctrl-c
        destroy()
