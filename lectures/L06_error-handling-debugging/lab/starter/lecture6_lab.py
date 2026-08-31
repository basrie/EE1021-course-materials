"""EE1021 Week 6 lab starter: debugging and defensive error handling."""


def celsius_to_fahrenheit(celsius):
    """Return the Fahrenheit equivalent of a Celsius value."""
    # BUG: compare expected and actual behavior before editing.
    return celsius * 9 / 5 - 32


def parse_reading(record):
    """Return (sensor_id, value) for a SENSOR,VALUE record."""
    # BUGS: malformed structure and nonnumeric values are not explained clearly.
    sensor, value_text = record.split(",")
    return sensor, float(value_text)


def classify_reading(sensor, value, limits):
    """Return normal, alarm, or unknown."""
    # BUG: a missing sensor currently raises KeyError.
    limit = limits[sensor]
    if value > limit:
        return "alarm"
    return "normal"


def average_reading(values):
    """Return the average of a non-empty sequence."""
    # BUGS: empty input fails indirectly and the denominator is wrong.
    return sum(values) / (len(values) - 1)


def process_records(records, limits):
    """Return (accepted, errors) after processing all records."""
    accepted = []
    errors = []

    for record in records:
        # TODO: parse expected bad records without hiding unexpected failures.
        # Append (sensor, value, status) to accepted or a useful message to errors.
        raise NotImplementedError("complete process_records")

    return accepted, errors


if __name__ == "__main__":
    limits = {"T1": 80.0, "T2": 75.0}
    sample_records = ["T1,23.5", "T2,error", "missing-comma", "T9,21.0"]

    print("20 C should be 68 F; actual:", celsius_to_fahrenheit(20))
    print("Run one focused test at a time and record the evidence before editing.")
