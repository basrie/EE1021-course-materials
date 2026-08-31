"""EE1021 Week 7 lab starter: classes, objects, and methods."""


class Sensor:
    """Store readings and behavior for one engineering sensor."""

    def __init__(self, sensor_id, unit):
        # TODO: validate and store independent instance state.
        raise NotImplementedError("complete Sensor.__init__")

    def add_reading(self, value):
        """Append one numeric reading and return None."""
        raise NotImplementedError("complete add_reading")

    def reading_count(self):
        """Return the number of stored readings."""
        raise NotImplementedError("complete reading_count")

    def latest(self):
        """Return the latest reading; reject an empty history."""
        raise NotImplementedError("complete latest")

    def average(self):
        """Return the average reading; reject an empty history."""
        raise NotImplementedError("complete average")

    def status(self, low, high):
        """Return low, normal, or high for the latest reading."""
        raise NotImplementedError("complete status")

    def __str__(self):
        """Return SENSOR: N readings (UNIT)."""
        raise NotImplementedError("complete __str__")


def sensor_report(sensor, low, high):
    """Return a dictionary summarizing one Sensor."""
    raise NotImplementedError("complete sensor_report")


def run_tests():
    """Add normal, boundary, invalid, and independence tests."""
    raise NotImplementedError("complete run_tests")


if __name__ == "__main__":
    run_tests()
