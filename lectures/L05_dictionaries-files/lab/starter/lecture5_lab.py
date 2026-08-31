"""EE1021 Week 5 lab starter: sensor fleet registry and event summary."""


def average_reading(readings):
    """Return the average of a non-empty reading dictionary."""
    pass


def voltage_status(value, low=4.75, high=5.25):
    """Return low, normal, or high."""
    pass


def build_statuses(readings):
    """Return a dictionary mapping each sensor ID to its status."""
    pass


def count_values(mapping):
    """Return counts of the values stored in mapping."""
    pass


def fleet_report(readings, calibrated):
    """Return a dictionary containing the required fleet summary."""
    pass


# Stage 1: Registry operations
readings = {"S1": 4.92, "S2": 5.31, "S3": 4.97}
# Predictions:
# TODO: inspect S1, length, S4 membership, and all keys.
# TODO: add S4, correct S2, pop S3, and safely pop S9.


# Stage 2: Iteration and counting
statuses = None
status_counts = None
# TODO: build statuses and status_counts using the supplied functions.


# Stage 3: Set relationships
registered = None
active = {"S1", "S2", "S4", "S5"}
calibrated = {"S1", "S4"}
faulty = {"S2", "S5"}
# TODO: calculate and print the five requested set relationships.


# Stage 4: Integrated report
report = None
# TODO: call fleet_report and display every returned field clearly.


# Activate after completing the functions.
# assert average_reading({"A": 1.0, "B": 2.0, "C": 3.0}) == 2.0
# assert voltage_status(4.74) == "low"
# assert voltage_status(4.75) == "normal"
# assert voltage_status(5.25) == "normal"
# assert voltage_status(5.26) == "high"
# assert build_statuses({"S1": 4.9, "S2": 5.4}) == {"S1": "normal", "S2": "high"}
# assert count_values({"S1": "normal", "S2": "high", "S3": "normal"}) == {"normal": 2, "high": 1}
