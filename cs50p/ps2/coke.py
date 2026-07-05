def main():
    Amount_due = 50
    
    
    while True:
        inp = int(input("Insert coin: "))

        if inp in [5,10,25]:
            Amount_due -= inp

            if Amount_due <= 0:
                 print(f"Change Owed: {abs(Amount_due)}")
                 break
            else:
                print(f"Amount due: {Amount_due}")
        else:
            print(f"Amount due: {Amount_due}")
            
main()
