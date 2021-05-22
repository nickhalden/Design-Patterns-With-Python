from abc import ABC, abstractmethod


#  defines a contract which switchable things can implement
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# LightBulb implements the Switchable contract/interface
class LightBulb(Switchable):

    def turn_on(self):
        print("LightBulb: turn on")

    def turn_off(self):
        print("LightBulb: turned off")


# Fan implements the Switchable contract/interface
class Fan(Switchable):

    def turn_on(self):
        print("Fan: turn on")

    def turn_off(self):
        print("Fan: turned off")


# ElectricPowerSwitch is dependable on Switchable class and not light bulb
class ElectricPowerSwitch:
    def __init__(self, c=Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

f = Fan()
switch = ElectricPowerSwitch(f)
switch.press()
switch.press()
