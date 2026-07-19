import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            Enter = input("Name: ").strip()
            names.append(Enter)
        except EOFError:
            break
    print(f"Adieu, adieu, to {p.join(names)}")

main()
