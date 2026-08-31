"""EE1021 Week 5 worksheet submission template."""

STUDENT_NAME = "<enter your name>"
STUDENT_NUMBER = "<enter your number>"


# Task 1: Convert tuple records to a dictionary
samples = [("S1", 4.92), ("S2", 5.08), ("S3", 4.97)]
readings = None
# TODO: Build readings with a loop and tuple unpacking.


# Task 2: Predict dictionary state
# Predictions:
registry = {"S1": 4.90, "S2": 5.08}
registry["S1"] = 4.92
registry["S3"] = 4.97
removed = registry.pop("S2")
print(registry)
print(removed)
print("S2" in registry)
# Explanation of add versus replace:


# Task 3: Required and optional lookup
calibration = {"S1": 1.02, "S2": 0.99}
required_s1 = None
optional_s9 = None
# TODO: Use direct indexing for S1 and get with default 1.0 for S9.
# Explanation of when a default could hide an error:


# Task 4: Iterate and aggregate
def reading_summary(readings):
    """Return (minimum_id, maximum_id, average)."""
    pass


# Task 5: Frequency dictionary
events = ["normal", "alarm", "normal", "calibration", "normal", "alarm"]
event_counts = None
most_frequent_event = None
# TODO: Build counts, print pairs, identify the most frequent event, and verify the total.


# Task 6: Set relationships
registered = {"S1", "S2", "S3", "S4"}
active = {"S1", "S2", "S4", "S5"}
calibrated = {"S1", "S4"}
faulty = {"S2", "S5"}

registered_and_active = None
active_not_calibrated = None
registered_faulty = None
all_known_ids = None
exactly_one_group = None
added_later = None
# TODO: Replace every None with the required set expression.


# Task 7: Fleet report
def fleet_report(readings, calibrated):
    """Return a dictionary containing a sensor-fleet summary."""
    pass


fleet_readings = {"S1": 4.92, "S2": 5.31, "S3": 4.60, "S4": 5.02}
fleet_calibrated = {"S1", "S4"}
report = None
# TODO: Call fleet_report and display every returned field.


# Activate after completing the functions.
# summary = reading_summary({"S1": 4.92, "S2": 5.08, "S3": 4.97})
# assert summary[0] == "S1"
# assert summary[1] == "S2"
# assert round(summary[2], 2) == 4.99
# expected = fleet_report(fleet_readings, fleet_calibrated)
# assert expected["sensor_count"] == 4
# assert expected["alarm_sensors"] == {"S2", "S3"}
# assert expected["needs_calibration"] == {"S2", "S3"}
