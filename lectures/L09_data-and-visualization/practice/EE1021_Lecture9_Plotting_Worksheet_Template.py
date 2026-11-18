"""EE1021 Lecture 9 worksheet: Part D template.

Write each program inside its function.
Run one function at a time: put a # in front of the other calls at the bottom.
plt.show() waits until you close the plot window. On macOS the window
can open behind VS Code: look for the Python icon in the Dock.
"""

import numpy as np
import matplotlib.pyplot as plt


def question_14():
    """Three resistors: current in mA for 0 V to 12 V, 50 points."""
    volts = np.linspace(0, 12, 50)
    # TODO: three current arrays in mA (100, 220 and 470 ohm)
    # TODO: one axes, three lines with labels, legend, title, labels, grid
    # TODO: save as three_resistors.png with dpi=200, then plt.show()


def question_15():
    """A capacitor charges: v = 5 * (1 - np.exp(-t / 0.1))."""
    # TODO: t from 0 s to 0.5 s with 200 points
    # TODO: v, then the plot with title, labels and grid
    # TODO: print the exact value of v at t = 0.1 s


def question_16():
    """Voltage and power of a 50 Hz sine wave in two axes."""
    # TODO: t from 0 s to 0.04 s with 200 points
    # TODO: volts (amplitude 10 V) and watts (100 ohm)
    # TODO: plt.subplots(2, 1): voltage on top, power in red below


def question_17():
    """The low-pass filter on a log-log plot."""
    f = np.linspace(10, 100000, 10000)
    gain = 1 / np.sqrt(1 + (f / 1000) ** 2)
    # TODO: ax.loglog(f, gain), title, labels, grid, plt.show()


def optional_measured():
    """Measured points (scatter) and the theory line for 220 ohm."""
    volts_measured = [0, 2, 4, 6, 8, 10]
    milliamps_measured = [0, 9.2, 18.0, 25.0, 36.5, 45.1]
    # TODO: ax.scatter for the measured values, ax.plot for the theory line


question_14()
question_15()
question_16()
question_17()
# optional_measured()
