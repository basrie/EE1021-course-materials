"""Main program for the Week 3 custom-module task."""

import sensor_tools


raw_voltage = 4.72

calibrated = sensor_tools.calibrate_voltage(raw_voltage)
status = sensor_tools.voltage_status(calibrated)

print("Raw:", raw_voltage)
print("Calibrated:", calibrated)
print("Status:", status)

# TODO: Test at least three raw readings that produce different statuses.
