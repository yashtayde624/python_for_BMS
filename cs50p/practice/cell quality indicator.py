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
