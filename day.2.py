# hiiii,,, It it day 2 of learning python
#in the project below ill use,print,strip,int,float,def,input,title etc...
#OHMs, law calculator
print("..................................................")
name = input("Hey....welcome, What is your name buddy?").title().strip()
print("nice to meet u",name,",this is an tool to calculate voltage from given resistance and current")
volt = float(input("What is the value of Voltage?"))
res = float(input("what is the value of resistance?"))
current = round(volt/res,2)
print("The value of current is:",current,"Amp")
def oh():
    print("Thanks!!!",name,(" Ta Ta"))
oh()
print("..................................................")

