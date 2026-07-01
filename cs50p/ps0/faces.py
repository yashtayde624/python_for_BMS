def main():
    print("Hello")
emoji = input("Add your message and emojii below!!")
new_emoji = (emoji).replace(":(" ,"🙁").replace(":)", "🙂")
print(new_emoji)
if __name__ == "__main__":
    main()
