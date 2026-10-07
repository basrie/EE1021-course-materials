"""EE1021 Homework 2 - answer template

Rename to EE1021_HW2_<student number>.py. Write each function where it says pass.
Set RUN (for example RUN = "P3") to run one problem. Paste your test outputs as
comments. The file must run without errors before you submit.
"""

STUDENT_NAME = "<your name>"
STUDENT_NUMBER = "<your student number>"

# Problem to run: "W1", "W2", "P1" ... "P5", "X1" ... "X3"
RUN = "W1"


# ===========================================================================
# Section W - Warm-up
# ===========================================================================

# W1 - my prediction of the three lists (written BEFORE running):
#
if RUN == "W1":
    values = [5, 10, 15]
    copy_a = values
    copy_b = values.copy()

    values.append(20)
    copy_a[0] = 1

    print(values)
    print(copy_a)
    print(copy_b)

# W1 real output:
#


# W2 - fix the bug: print(average([2, 4, 6])) must show 4.0
def average(values):
    total = 0
    for v in values:
        total = total + v
        return total / len(values)


if RUN == "W2":
    print(average([2, 4, 6]))

# W2 - the bug and my fix, in one comment:
#


# ===========================================================================
# Section P - Write the Functions
# ===========================================================================

# P1 - Your student number as data
def digits_of(number_text):
    """Return the digits of number_text as a list of integers."""
    pass


def digit_stats(digits):
    """Return (smallest, largest, average); average rounded to 2 decimals."""
    pass


if RUN == "P1":
    my_digits = digits_of(STUDENT_NUMBER)
    print(my_digits)
    # TODO: unpack digit_stats(my_digits) into three names and print one line.
    # TODO: test digits_of and digit_stats with at least two more inputs.

# P1 output:
#
# P1 - an input that broke my first version, and what I changed:
#


# P2 - Limit sensor readings
def limit_readings(readings, low, high):
    """Return a new list; values below low become low, above high become high."""
    pass


def count_changed(original, limited):
    """Return how many values are different between the two lists."""
    pass


if RUN == "P2":
    raw = [4.10, 4.92, 5.08, 5.70, 4.97]
    # TODO: call limit_readings and count_changed, print the results and raw.
    # TODO: test with at least two more inputs of your own.

# P2 output:
#
# P2 - an input that broke my first version, and what I changed:
#


# P3 - Compress a signal
def compress(values):
    """Replace each run of equal neighbouring values with (value, count)."""
    pass


def expand(pairs):
    """Rebuild the original list: each (value, count) becomes count copies of value."""
    pass


if RUN == "P3":
    signal = [0, 0, 0, 1, 1, 0]
    # TODO: print compress(signal) and check that expand(compress(signal)) == signal.
    # TODO: test with at least two more inputs of your own.

# P3 output:
#
# P3 - for which inputs does the compressed list store more numbers than the original?
#
# P3 - an input that broke my first version, and what I changed:
#


# P4 - Second largest (no sort, sorted, max or min; go through the list once)
def second_largest(values):
    """Return the second largest different value, or None if there is none."""
    pass


if RUN == "P4":
    print(second_largest([3, 8, 1]))      # expected 3
    print(second_largest([5, 5, 3]))      # expected 3
    print(second_largest([-4, -1, -7]))   # expected -4
    print(second_largest([7, 7]))         # expected None
    # TODO: add tests of your own.

# P4 output:
#
# P4 - an input that broke my first version, and what I changed:
#


# P5 - Merge two sorted lists (no sort or sorted; do not change a or b)
def merge_sorted(a, b):
    """Return one new sorted list with all elements of a and b."""
    pass


if RUN == "P5":
    print(merge_sorted([1, 4, 9], [2, 3, 10, 12]))   # [1, 2, 3, 4, 9, 10, 12]
    print(merge_sorted([1, 2], [2, 3]))              # [1, 2, 2, 3]
    print(merge_sorted([], [5, 6]))                  # [5, 6]
    # TODO: add tests of your own.

# P5 output:
#
# P5 - an input that broke my first version, and what I changed:
#


# ===========================================================================
# Section X - Extension (optional)
# ===========================================================================

# X1 - Find spikes
def find_spikes(readings, limit):
    """Return the indices of readings that differ from both neighbours by more than limit."""
    pass


if RUN == "X1":
    print(find_spikes([5.0, 5.1, 7.9, 5.0, 5.2, 2.1, 5.1], 1.0))   # [2, 5]

# X1 output:
#


# X2 - My own problem from another course
if RUN == "X2":
    pass

# X2 - the problem in two sentences:
#
# X2 - two test runs:
#
# X2 - one input that could break my function:
#


# X3 - Experiment: does b change after a += [4]? And after a = a + [5]?
if RUN == "X3":
    a = [1, 2]
    b = a
    pass

# X3 output:
#
# X3 - the rule I found, in one sentence:
#
