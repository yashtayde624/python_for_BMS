def main():
    while True:
        try:
            fraction = input("Fraction: ")
            result = float(get_per(fraction))
        except( ValueError,ZeroDivisionError):
            pass
        else:
            break
    print(gauge(result))

def get_per(fraction):
    a , b = fraction.split("/")
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivisionError
    if a > b or a < 0 or b < 0:
        raise ValueError
    return round((a / b)*100)
def gauge(pop):
    if pop >= 99:
        return "F"
    if pop <= 1:
        return "E"
    else:
        return f"{pop}%"

main()
