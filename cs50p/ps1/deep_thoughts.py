def main():
    n = input("What is the answer to the questions of universe?")
    n = n.strip().lower()
    if n == "42" or n == "forty two" or n == "forty-two":
        print("Yes")
    else:
        print("No")


main()
