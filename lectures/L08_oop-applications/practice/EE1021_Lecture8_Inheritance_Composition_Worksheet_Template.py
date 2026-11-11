"""EE1021 Lecture 8 worksheet: starter file.

Write your code in the places marked TODO.
Run the file after each section. The tests for a section are at the bottom:
remove the # in front of the lines of the section you want to test.
"""


# ---------------------------------------------------------------------------
# Lecture classes. Do not change them (except Room in Section G, task 2).
# ---------------------------------------------------------------------------
class Device:
    def __init__(self, name, watts):
        self.name = name
        self.watts = watts
        self.is_on = False

    def switch_on(self):
        self.is_on = True

    def power(self):
        if self.is_on:
            return self.watts
        return 0

    def __str__(self):
        return f"{self.name}: {self.power()} W"


class Lamp(Device):
    def lumens(self):
        return 90 * self.power()

    def __str__(self):
        return f"lamp {self.name}: {self.lumens()} lm"


class DimmableLamp(Lamp):
    def __init__(self, name, watts, level=100):
        super().__init__(name, watts)
        self.level = level

    def power(self):
        return super().power() * self.level / 100


class Room:
    def __init__(self, volts, max_amps):
        self.volts = volts
        self.max_amps = max_amps
        self.devices = []

    def add(self, device):
        self.devices.append(device)

    def total_power(self):
        total = 0
        for device in self.devices:
            total += device.power()
        return total

    def is_overloaded(self):
        amps = self.total_power() / self.volts
        return amps > self.max_amps

    # TODO Section G, task 2: add the method devices_on(self)


# ---------------------------------------------------------------------------
# Section B: Battery
# ---------------------------------------------------------------------------
class Battery:
    pass  # TODO: write __init__, the property percent with a setter, and is_low


# ---------------------------------------------------------------------------
# Section D: Heater
# ---------------------------------------------------------------------------
class Heater(Device):
    pass  # TODO: write __init__, is_heating and __str__


# ---------------------------------------------------------------------------
# Section E: total_power
# ---------------------------------------------------------------------------
def total_power(devices):
    pass  # TODO: return the sum of power() of all devices


# ---------------------------------------------------------------------------
# Section F: Sample
# ---------------------------------------------------------------------------
class Sample:
    count = 0

    def __init__(self, volts):
        self.volts = volts
        Sample.count += 1
        self.number = Sample.count

    # TODO Section F, task 2: add the method __eq__(self, other)


# ---------------------------------------------------------------------------
# Tests. Remove the # in front of the lines of one section, then run the file.
# ---------------------------------------------------------------------------

# Section B
# b = Battery("B1", 80)
# b.percent = 15
# print(b.is_low)
# print(b.percent)

# Section C
# tv = Device("tv", 100)
# desk = Lamp("desk", 10)
# hall = DimmableLamp("hall", 40, 25)
# desk.switch_on()
# hall.switch_on()
# print(tv)
# print(desk)
# print(hall.power())
# print(hall)

# Section D
# h = Heater("heater", 2000)
# print(h)                  # heater: 0 W, target 21 C
# h.switch_on()
# print(h)                  # heater: 2000 W, target 21 C
# print(h.is_heating(18))   # True
# print(h.is_heating(23))   # False
# small = Heater("small", 800, 18)
# print(small.target)       # 18

# Section E
# tv = Device("tv", 100)
# desk = Lamp("desk", 10)
# hall = DimmableLamp("hall", 40, 25)
# h = Heater("heater", 2000)
# devices = [tv, desk, hall, h]
# for device in devices:
#     device.switch_on()
# print(total_power(devices))

# Section F
# a = Sample(3.3)
# b = Sample(5.0)
# c = Sample(3.3)
# print(a.number, c.number)
# print(Sample.count)
# print(a == c)

# Section G
# lab = Room(230, 10)
# pc = Device("pc", 300)
# printer = Device("printer", 600)
# desk = Lamp("desk", 10)
# lab.add(pc)
# lab.add(printer)
# lab.add(desk)
# pc.switch_on()
# print(lab.devices_on())
# printer.switch_on()
# desk.switch_on()
# print(lab.total_power())
# print(lab.is_overloaded())
# kettle = Device("kettle", 2000)
# lab.add(kettle)
# kettle.switch_on()
# print(lab.total_power())
# print(lab.is_overloaded())
