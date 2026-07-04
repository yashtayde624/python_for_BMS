def main():
 Charging = 0
 Empty = 0
 Overcurrent = 0

 for i in range(1,5):
 #   this below line is to ask for current, in decimal and in a range
    current = float(input(f"What's current{i}?"))


    if current > 32:
     Overcurrent += 1
    elif current == 0:
        Empty += 1
    elif 0 < current <= 32:
        Charging += 1

 print(f"Charging Slots: {Charging}")
 print(f"Empty Slots: {Empty}")
 print(f"Overcurrent Slots: {Overcurrent}")
  
main()
