
def main():
    x = input("greet")
    x = x.strip().lower()
    if x == "hello" or x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")


main()
