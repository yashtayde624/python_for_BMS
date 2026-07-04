"""
SOC Estimator - Voltage Based
Author: Yash Tayde
Description:
    Reads voltage inputs from 10 Li-ion battery cells,
    calculates the average pack voltage, and estimates
    the State of Charge (SOC) percentage.

Voltage to SOC Mapping (Li-ion chemistry):
    4.2V        --> 100% SOC (Fully Charged)
    4.0V-4.2V   --> 80%  SOC
    3.8V-4.0V   --> 60%  SOC
    3.6V-3.8V   --> 40%  SOC
    3.4V-3.6V   --> 20%  SOC
    below 3.2V  --> 0%   SOC (Critical Low)
    above 4.2V  --> Overvoltage Fault

Skills Demonstrated:
    - Python loops and conditionals
    - Battery voltage monitoring
    - Basic SOC estimation logic
"""
def main():
    total = 0
    
    # Loop through 10 battery cells and collect voltage readings. 
    for v in range(1,11):
        voltage = float(input(f"voltage of this cell{v} :"))
        total += voltage
    # Calculate average pack voltage.     
    Average = total/10
    print(f"Avg voltage is {Average}")
    # Map average voltage to state of charge SOC percentage. 
    # Based on the lithium-ion voltage range ,3.2 V (empty) to 4.2 V (full) 
    if Average == 4.2:
         print("SOC is 100%")
    elif 4.0 < Average <= 4.2:
         print("SOC is 80%")
    elif 3.8 < Average <= 4:
          print("SOC is 60%")
    elif 3.6 < Average <= 3.8:
          print("SOC is 40%")
    elif 3.4 < Average <= 3.6:
         print("SOC is 20%")
    elif 3.2 > Average:
         print("SOC is 0%")
    else:
         print("Overvoltage") #Voltage above 4.2 V is a fault condition. 
    
main()
