"""EE1021 Week 7 worksheet submission template."""


class Sensor:
    """Store readings and behavior for one sensor."""

    def __init__(self, sensor_id, unit):
        raise NotImplementedError("complete Sensor.__init__")

    def add_reading(self, value):
        raise NotImplementedError("complete add_reading")

    def reading_count(self):
        raise NotImplementedError("complete reading_count")

    def latest(self):
        raise NotImplementedError("complete latest")

    def average(self):
        raise NotImplementedError("complete average")

    def status(self, low, high):
        raise NotImplementedError("complete status")

    def __str__(self):
        raise NotImplementedError("complete Sensor.__str__")


class Resistor:
    """Represent one resistor with a positive resistance."""

    def __init__(self, label, resistance_ohm):
        raise NotImplementedError("complete Resistor.__init__")

    def current(self, voltage):
        raise NotImplementedError("complete current")

    def power(self, voltage):
        raise NotImplementedError("complete power")

    def __str__(self):
        raise NotImplementedError("complete Resistor.__str__")


def run_tests():
    """Add normal, boundary, invalid, and independence tests."""
    raise NotImplementedError("complete run_tests")


if __name__ == "__main__":
    run_tests()
