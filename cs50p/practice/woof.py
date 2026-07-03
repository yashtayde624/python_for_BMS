def main():
    numbers = howmanytime()
    Woof(numbers)

def howmanytime():
    while True:
        n = int(input("how many times to Woof!!"))
        if n > 0:
            break
    return n
        
def Woof(n):
    for _ in range(n):
        print("Woof")



main()
