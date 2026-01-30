import random
import os
import time # for sleep function

DIE_FACES = {
    1: [
        "+-------+",
        "|       |",
        "|   ●   |",
        "|       |",
        "+-------+",
    ],
    2: [
        "+-------+",
        "| ●     |",
        "|       |",
        "|     ● |",
        "+-------+",
    ],
    3: [
        "+-------+",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "+-------+",
    ],
    4: [
        "+-------+",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "+-------+",
    ],
    5: [
        "+-------+",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "+-------+",
    ],
    6: [
        "+-------+",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "+-------+",
    ],
}

def roll_die(): 
    """Roll exactly one 6-sided die."""
    return random.randint(1, 6) # returns a random integer between 1 and 6 inclusive

def clear():
    os.system("cls")

def print_die(face):
    for line in DIE_FACES[face]:
        print(line)

def main():
    clear()
    print("Welcome to the Dice Roller — 1 six-sided die\n")
    while True:
        choice = input("Press Enter to roll (or type 'q' then Enter to quit): ").strip().lower()
        if choice == "q":
            print("Come To Play Soon.")
            break
        # quick rolling animation
        for _ in range(8):
            r = random.randint(1, 6)
            clear()
            print("Rolling...\n")
            print_die(r)
            time.sleep(0.08)
        result = roll_die()
        clear()
        print("Result:\n")
        print_die(result)
        print(f"\nYou rolled: {result}\n")

if __name__ == "__main__":
    main()