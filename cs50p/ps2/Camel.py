def main():
    word = input("camelCase: ")
    result =""

    for i in word:
        if i.isupper():
            result += "_" + i.lower()
        else:
            result += i
    print(f"snake_case: {result}")

main()
