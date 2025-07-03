import math
import random
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    print("\nMATH VISUALIZER")
    print("1. Prime Number Finder")
    print("2. Multiplication Table Generator")
    print("3. Dice Roll Simulator + Histogram")
    print("4. Coin Toss Simulator")
    print("5. Exit")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_finder():
    print("---Prime Number Finder---")
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        print(f"\nPrimes between {start} and {end}: ")
        for num in range(start, end + 1):
            if is_prime(num):
                print(num, end=" ")
        print("\n")
    except ValueError:
        print("Please Enter Valid Numbers.")

def multiplication_table():
    print("\n---Multiplication Table Generator---")
    try: 
        number = int(input("Enter the number for the table: "))
        upto = int(input("Enter how many multiples to show: "))
        print()
        for i in range(1, upto + 1):
            print(f"{number} x {i} = {number * i}")
    except:
        print("Please enter valid numbers.")

def dice_simulator():
    print("\n---Dice Roll Simulator---")
    try: 
        rolls = int(input("How many times to roll the die? "))
        results = [0] * 6 

        for _ in range(rolls):
            roll = random.randint(1,6)
            results[roll - 1] += 1
        
        print("\nResults: ")
        for i, count in enumerate(results):
            print(f"{i+1}: {count} times")
        
        print("\nHistogram: ")
        for i, count in enumerate(results):
            print(f"{i+1}: {'#' * count}")
    except ValueError:
        print("Please enter a valid number.")

def coin_toss_simulator():
    print("\n---Coin Toss Simulator---")
    try: 
        tosses = int(input("How many times to toss the coin?"))
        heads = 0
        tails = 0
        
        for _ in range(tosses):
            toss = random.choice(["heads", "tails"])
            if toss == "heads":
                heads += 1
            else:
                tails += 1
        
        print(f"\nHeads: {heads} times")
        print(f"\nTails: {tails} times")
        print(f"Heads %: {heads/tosses * 100:.2f}%")
        print(f"Tails %: {tails/tosses * 100:.2f}%")
    except ValueError:
        print("Please enter a valid number.")

#Main

while True:
    #clear_screen()
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        prime_finder()
    elif choice == "2":
        multiplication_table()
    elif choice == "3":
        dice_simulator()
    elif choice == "4":
        coin_toss_simulator()
    elif choice == "5":
        print("GoodBye!")
        break
    else:
        print("Invalid Choice. Try again.")


