"""EE1021 Week 6 worksheet submission template."""


def parse_reading(record):
    """Return (sensor_id, value) for SENSOR,VALUE."""
    raise NotImplementedError("complete parse_reading")


def classify_reading(sensor, value, limits):
    """Return normal, alarm, or unknown."""
    raise NotImplementedError("complete classify_reading")


def average_reading(values):
    """Return the average of a non-empty sequence."""
    raise NotImplementedError("complete average_reading")


def process_records(records, limits):
    """Return (accepted, errors) after processing all records."""
    raise NotImplementedError("complete process_records")


def run_tests():
    """Add normal, boundary, and invalid-input tests here."""
    raise NotImplementedError("complete run_tests")


if __name__ == "__main__":
    run_tests()
