def main():
    text = input("Text: ")
    result = ""
    # for each individual alphabet,,,
    for c in text:
        if c not in ["A","E","I","O","U","a","e","i","o","u"]:
            result += c

    print(result)



main()
