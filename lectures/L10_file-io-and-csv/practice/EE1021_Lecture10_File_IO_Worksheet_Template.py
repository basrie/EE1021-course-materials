"""EE1021 Lecture 10 worksheet: starter file.

Run this file one time first. It creates the data files of the worksheet
in the working folder and prints the path of the working folder.

Write each Part D program inside its function. At the bottom of the file,
remove the # in front of the call you want to run.
"""

import os


# ---------------------------------------------------------------------------
# Data files of the worksheet. Do not change this function.
# Every run writes the five files again, so they always have the same content.
# ---------------------------------------------------------------------------
def create_data_files():
    with open("state.txt", "w", encoding="utf-8") as file:
        file.write("on\noff\n")

    with open("volts.txt", "w", encoding="utf-8") as file:
        file.write("4.5\n5.25\n5.0\n")

    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("one\n")

    with open("devices.csv", "w", encoding="utf-8") as file:
        file.write("name,watts\n")
        file.write("router,12\n")
        file.write("desk lamp,9\n")
        file.write("heater,1500\n")
        file.write("kettle,2000\n")
        file.write("laptop,65\n")

    with open("measurements.txt", "w", encoding="utf-8") as file:
        for volts in [4.92, 5.01, 4.98, 5.10, 4.87, 5.03, 4.95, 5.06]:
            file.write(f"{volts}\n")


# ---------------------------------------------------------------------------
# Classes for question 18 and the optional question. Do not change them.
# ---------------------------------------------------------------------------
class Part:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price      # TL for one part
        self.stock = stock      # number of parts in the shop

    def value(self):
        return self.price * self.stock

    def __str__(self):
        return f"{self.name}: {self.stock} in stock, {self.price} TL each"


class Kit(Part):
    def __str__(self):
        return f"kit {self.name}: {self.stock} boxes, {self.price} TL each"


# ---------------------------------------------------------------------------
# Part D
# ---------------------------------------------------------------------------
def question_15():
    """Measurements: count, smallest, largest and average of measurements.txt."""
    # TODO: read the file line by line and convert each line to a float
    # TODO: print the four lines


def question_16():
    """A report file: read devices.csv, write report.txt."""
    # TODO: read devices.csv (skip the header)
    # TODO: write one line for each device: name and current at 230 V
    # TODO: write the last line with the total power


def log_reading(volts):
    """Add one line to readings.txt: reading: <volts> V"""
    # TODO


def question_17():
    log_reading(4.8)
    log_reading(5.1)
    log_reading(5.0)
    print("three readings logged")


def save_parts(parts, filename):
    """Write the header name,price,stock and one line for each part."""
    # TODO


def load_parts(filename):
    """Return a list of Part objects. Missing file: a message and an empty list."""
    # TODO


def question_18():
    parts = [
        Part("resistor 220R", 0.05, 400),
        Part("LED red", 0.12, 150),
        Part("capacitor 100nF", 0.08, 250),
    ]
    save_parts(parts, "parts.csv")

    loaded = load_parts("parts.csv")
    total = 0
    for p in loaded:
        print(p)
        total += p.value()
    print(f"stock value: {total:.2f} TL")

    print(load_parts("no_such_file.csv"))


# ---------------------------------------------------------------------------
# Optional
# ---------------------------------------------------------------------------
def save_kinds(parts, filename):
    """Like save_parts, with the class name in the first column."""
    # TODO


def load_kinds(filename):
    """Return a list with Part objects and Kit objects."""
    # TODO


def optional_kinds():
    parts = [Part("resistor 220R", 0.05, 400), Kit("starter kit", 350.0, 12)]
    save_kinds(parts, "kinds.csv")
    for p in load_kinds("kinds.csv"):
        print(p)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------
create_data_files()
print("working folder:", os.getcwd())

# question_15()
# question_16()
# question_17()
# question_18()
# optional_kinds()
