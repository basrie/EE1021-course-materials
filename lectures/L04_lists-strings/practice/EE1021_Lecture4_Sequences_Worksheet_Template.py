"""EE1021 Week 4 worksheet submission template.

Replace every pass and None placeholder. Record predictions and explanations as
comments before running each task. Keep the provided names so the instructor's
checks can run against your work.
"""

STUDENT_NAME = "<enter your name>"
STUDENT_NUMBER = "<enter your number>"


# Task 1: Return and unpack a tuple
def reading_limits(readings):
    """Return (minimum, maximum) for a non-empty list of readings."""
    pass


limits_input = [4.92, 5.08, 4.97, 5.11]
low = None
high = None
# TODO: Call reading_limits, unpack the result, and print the requested line.
# Explanation:


# Task 2: Prediction, indexing, slicing, and mutation
# Prediction for the four print statements:
values = [10, 20, 30, 40, 50]
print(values[-1])
print(values[1:4])
values[2] = 31
values[0:2] = [11, 21]
print(values)
print(len(values))
# Mutating lines:


# Task 3: Choose list operations
lab_queue = ["group-01", "group-03", "group-04"]
processed = None
# TODO: insert group-02 and print
# TODO: append group-05 and print
# TODO: add group-06 and group-07 as separate elements and print
# TODO: remove group-03 by value and print
# TODO: remove/store the front group, then print the queue and processed


# Task 4: Repair append versus extend
readings = [4.90, 4.95]
new_readings = [5.00, 5.05]
# Prediction of the incorrect append result:
# TODO: Add the corrected one-line operation and print readings.
# Explanation:


# Task 5: Build and filter lists
millivolts = [4100, 4920, 5080, 5700, 4970]
volts = None
valid_volts = None
# TODO: Replace both None values with comprehensions and print the requested results.


# Task 6: Trace aliasing and cloning
# Predictions for original, alias, and clone:
original = [1, 2]
alias = original
clone = original.copy()
alias.append(3)
clone.append(4)
print(original)
print(alias)
print(clone)
# Reference explanation:


# Task 7: Engineering mini-problem
def clean_readings(readings, low=4.75, high=5.25):
    """Return valid readings without changing the input list."""
    pass


raw = [4.10, 4.92, 5.08, 5.70, 4.97]
valid = None
minimum = None
maximum = None
# TODO: Call clean_readings, unpack the limits, and print raw/valid/range.


# Self-checks: these should pass after Tasks 1 and 7 are complete.
# assert reading_limits([3.0, 1.0, 2.0]) == (1.0, 3.0)
# test_raw = [4.1, 4.9, 5.0, 5.7]
# assert clean_readings(test_raw) == [4.9, 5.0]
# assert test_raw == [4.1, 4.9, 5.0, 5.7]
