# Potentiometer Voltage

> Use the ADC function of ADC Module to read the voltage value of potentiometer.

![Breadboard with RPi GPIO Extension Board](https://i.ibb.co/MB8vJb4/IMG-20200725-171244.jpg)

## Table of Contents
- Components
- Circuits Knowledge
- Components Knowledge
- Configuration
- Contact


### Components
[] Raspberry Pi 4
[] GPIO Extension Board
[] Jump Wires M-M
[] Breadboard
[] Rotary Potentiometer
[] ADC module (PCF8591)
[] Resistor 10k &Omega;

### Circuits Knowledge
- [Analog-to-Digital Converter](https://en.wikipedia.org/wiki/Analog-to-digital_converter): Simply, a device used to convert analog to digital. For this project, Im using the PCF8591 module, which is an 8 bit ADC that can read values up to 256 (2^8). This module also has 4 analog inputs and 1 analog output and works with I2C communication software to connect with our GPIO 22(SCL) and GPIO 21 (SDA).

### Components Knowledge
- [Rotary Potentiometer](https://en.wikipedia.org/wiki/Potentiometer): Essentially used for mesasuring electric potentional (voltage) and acts as a variable resistor where we will adjust the resistance through rotating the potentiometer.
- [I2C communication](https://en.wikipedia.org/wiki/I%C2%B2C): We'll be using this Inter-Integrated Circuit to connect a microcontroller and be used as a transmitter or receiver to communicate with devices connected to the bus.

### Configuration
1. Enable the i2C interface in your RPi via terminal:
    a. `sudo raspi-config`
    b. Choose `5 Interfacing Options > PG I2C > Yes > OK > Finish`
    
2. Install I2C-Tools:
    a. `apt-get install i2c-tools`
    b. Detect the I2C device address: `i2cdetect -y 1`
    c. You should be able to detect the address in row 8, column 40 with the HEX 48.
    
    ![Terminal detecting i2c](https://i.ibb.co/c11gjPj/i2cdetect.png)
    
3. Install Smbus Module:
    `apt-get install python-smbus`
    
4. Install ADCDevice, a custom module
    `python3 setup.py install`
    
5. Execute the code:
    `python adc.py`

6. After the program is executed, you can adjust the potentiometer and the terminal will printout the voltage value and converted digital content.

:pushpin: www.jackiepareja.com
    