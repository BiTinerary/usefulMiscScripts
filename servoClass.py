#!/bin/python
import time
from pyA20.gpio import gpio
from pyA20.gpio import port

class servo():
    def __init__(self, stepPin=int(), dirPin=int()):
        self.step = stepPin
        self.dir = dirPin
        self.allPins = [self.step, self.dir]
        gpio.init()

        [gpio.setcfg(x, gpio.OUTPUT) for x in self.allPins]
        [gpio.pullup(x, 0) for x in self.allPins]
        [gpio.setcfg(x, 0) for x in self.allPins]
        
        # First initialization should PROMPT FOR MANUAL CALIBRATION/ZEROING OF DESK
        self.location = 0

    def pinState(self, pin):
        pinStateValue = gpio.input(pin) 
        if pinStateValue == 0:
                pinStateString = 'Low'
        elif pinStateValue == 1:
                pinStateString = "High"
        return pinStateValue, pinStateString

    def allPins(self, upDown):
        if upDown == 'up':
            [gpio.pullup(x, gpio.PULLUP) for x in allPins]
        elif upDown == 'down':
            [gpio.pullup(x, gpio.PULLDOWN) for x in allPins]

    def rotate(self, degree=int(), direction=bool()):
        degree = int(degree / 1.8)
        
        if direction == True:
                gpio.pullup(self.dir, gpio.PULLDOWN)
        elif direction == False:
                gpio.pullup(self.dir, gpio.PULLUP)

        for x in range(degree):
                gpio.pullup(self.step, gpio.PULLDOWN)
                gpio.pullup(self.step, gpio.PULLUP)
                time.sleep(.01)
                
    #def preset(height=str())
        # needs array -> for each step, array += step
        # middle of desk == array = 0. Top = 35. Bottom = -35
        # if array = 35, preset pressed high? do nothing.
        # if array = 35, preset pressed low? rotate counterclockwise 70x
        # [s.rotate(degree=360, clockwise=False) for x in range(35)] # < Literal of ^
    #def button():
        # If X button pressed, move up until released. Do not go above array 60.
        # If Y button pressed, move down until released. Do not go below -60

s = servo(stepPin=6, dirPin=203)

try:
        s.rotate(degree=360, clockwise=True)
        s.rotate(degree=360, clockwise=False)
        
except KeyboardInterrupt:
        s.allPins('down')
finally:
        s.allPins('down')