"""
Cell Quality Indicator
======================
Author: Yash Tayde
Description:
    Reads voltage from 5 Li-ion battery cells and
    classifies each cell as Good or Bad based on
    the safe operating voltage range.

Cell Quality Logic:
    3.0V - 4.2V --> Good Cell (safe operating range)
    Below 3.0V  --> Bad Cell (undervoltage fault)
    Above 4.2V  --> Bad Cell (overvoltage fault)

Skills Demonstrated:
    - Python loops and conditionals
    - Battery cell fault detection
    - Voltage threshold monitoring
"""
def main():
    good = 0
    bad = 0
    
    for i in range(1, 6):
        voltage = float(input(f"voltage {i}? "))
        if 3.0 <= voltage <= 4.2:
            good += 1
        else:
            bad += 1
    
    print(f"Good cells: {good}")
    print(f"Bad cells: {bad}")

main()
