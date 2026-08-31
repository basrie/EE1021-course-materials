"""EE1021 Week 4 lab starter: sensor reading cleanup and summary."""


def is_valid_voltage(value, low=4.75, high=5.25):
    """Return True when value is inside the inclusive valid range."""
    pass


def summarize_readings(readings):
    """Return (minimum, maximum, average) for a non-empty list."""
    pass


raw_readings = [4.91, 4.96, -1.0, 5.08, 5.72]

# Stage 1
# Predictions:
# TODO: Print the first value, last value, middle three, and length.
# TODO: Correct -1.0, insert 5.01, append 4.93, and extend with [5.03, 4.89].
# Print after every operation.

# Stage 2
valid_readings = None
rejected_count = None
# TODO: Build valid_readings with a comprehension without mutating raw_readings.
# TODO: Calculate and print rejected_count.

# Stage 3
minimum = None
maximum = None
average = None
# TODO: Call summarize_readings and unpack the tuple.
# TODO: Print minimum, maximum, and average rounded to two decimal places.

sensor_ids = ["S1", "S2", "S3"]
sample_readings = [4.92, 5.08, 4.97]
samples = []
# TODO: Build (sensor_id, reading) tuples and print one report line per tuple.

# Stage 4
original = [4.92, 5.08]
alias = None
clone = None
# TODO: Create alias and clone, mutate each, and print all three lists.
# Reference explanation:

# Activate these checks when the functions are complete.
# assert is_valid_voltage(4.74) is False
# assert is_valid_voltage(4.75) is True
# assert is_valid_voltage(5.25) is True
# assert is_valid_voltage(5.26) is False
# assert summarize_readings([1.0, 2.0, 3.0]) == (1.0, 3.0, 2.0)
