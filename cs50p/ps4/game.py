import random
def main():
    n = int(input("Level: "))
    level = random.randint(1,n)
    while True:
         try:
            if n > 0:
             guessing = int(input("Guess: "))
             if guessing > level:
                print("Too large!")
             elif guessing < level:
                print("Too small!")
             else:
                print("Just right!")
                break
         except ValueError:
           pass


main()
