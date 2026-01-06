### Ask user for their name
class Person:
    def __init__(self, name):
        self.name = name

### Game Introduction
name = input("Welcome to Charlotte, North Carolina. What's your name? ")
person = Person(name=name)

print(f"Hi {person.name}!\n")
print("You've landed in the Queen City!")
print("So much to do, so little time.")
print("Let's start on our food tour!")

### Main Game Loop
def play_game():
    while True:
        print("\nWhere would you like to go for your first destination?")
        print("Choose a number from the list below:")

        ### List of destinations
        destinations = {
            "1": "The Salty (donut shop)",
            "2": "The Dive N (diner in Pineville)",
            "3": "Metro Diner",
            "4": "Easy Like Sunday",
            "5": "Red Eye Diner",
            "6": "Ballantyne (upscale dining)",
            "7": "Uptown (city center dining)",
            "8": "South End (trendy restaurants)",
            "9": "NoDa (arts district eats)",
        }

        for key, value in destinations.items():
            print(f"{key}: {value}")

        travelChoice = input("> ")

        if travelChoice not in destinations:
            print("Invalid choice. Please select a valid destination number.")
            continue

        print(f"You selected to go to {destinations[travelChoice]}.")

        # --- Destination Logic ---

        if travelChoice == "1":  # The Salty (donut shop)
            print("You are off to The Salty to grab a donut.")
            while True:
                print("Are you feeling like a:")
                print("1: Classic donut")
                print("2: Special donut")
                donutChoice = input("> ")

                if donutChoice == "1":
                    print("You picked a Glazed donut!")
                    print("Good choice! You played it safe.")
                    break
                elif donutChoice == "2":
                    print("You picked the Whipped Lemon Ricotta Boboloni donut!")
                    print("While adventurous, this was way sweeter than expected.")
                    print("You also had to spend money on a simple coffee.")
                    break
                else:
                    print("Invalid donut choice. Please enter 1 or 2.")

        elif travelChoice == "2":  # The Dive N (diner in Pineville)
            print("You took an Uber to a small diner in Pineville called The Dive N.")
            while True:
                print("Do you want:")
                print("1: The junkyard plate")
                print("2: An egg plate")
                plateChoice = input("> ")

                if plateChoice == "1":
                    print("You picked the junkyard plate.")
                    print("This is a combo plate with eggs, meat choice, cheese, peppers, onions, and hashbrowns.")
                    print("This is a classic but very filling choice. Your stomach is really full.")
                    break
                elif plateChoice == "2":
                    print("You picked the egg plate.")
                    print("For your side, you asked for livermush.")
                    print("You had instant regret and are feeling very sick.")
                    break
                else:
                    print("Invalid plate choice. Please enter 1 or 2.")

        elif travelChoice == "3":  # Metro Diner (local diner)
            print("You are off to Metro Diner for a bite to eat!")
            while True:
                print("Are you feeling:")
                print("1: Pancakes")
                print("2: An omelet")
                plate2Choice = input("> ")

                if plate2Choice == "1":
                    print("You picked a Maple Bacon Pancake!")
                    print("You really enjoyed this, but you are still hungry.")
                    break
                elif plate2Choice == "2":
                    print("You picked a Western Omelet.")
                    print("Good choice!")
                    break
                else:
                    print("Invalid food choice. Please type 1 or 2.")

        elif travelChoice == "4":  # Easy Like Sunday (located in ParkTowne Village)
            print("You are off to Easy Like Sunday for a bite to eat!")
            while True:
                print("Are you feeling:")
                print("1: A burger")
                print("2: A burrito")
                plate3Choice = input("> ")

                if plate3Choice == "1":
                    print("You picked a Breakfast Burger!")
                    print("That was a good burger! The best part was the over easy egg.")
                    break
                elif plate3Choice == "2":
                    print("You picked a Breakfast Burrito.")
                    print("Yum! This had potatoes, green chilis, eggs, cheese, and bacon!")
                    break
                else:
                    print("Invalid food choice. Please type 1 or 2.")

        elif travelChoice == "5":  # Red Eye Diner
            print("You are off to Red Eye Diner for a bite to eat!")
            while True:
                print("Are you feeling:")
                print("1: Biscuits & gravy")
                print("2: French toast with eggs")
                plate4Choice = input("> ")

                if plate4Choice == "1":
                    print("You picked Biscuits & Gravy!")
                    print("That was really good! You enjoyed that.")
                    break
                elif plate4Choice == "2":
                    print("You picked French Toast with Eggs.")
                    print("Yum! Good choice.")
                    break
                else:
                    print("Invalid food choice. Please type 1 or 2.")

        elif travelChoice == "6":  # Ballantyne
            print("You've arrived in **Ballantyne**, known for its upscale dining.")
            while True:
                print("Where would you like to eat in Ballantyne?")
                print("1: Rooster's Wood-Fired Kitchen (American)")
                print("2: North Italia (Italian)")
                print("3: Gallery Restaurant (Contemporary American)")
                ballantyne_choice = input("> ")

                if ballantyne_choice == "1":
                    print("You chose **Rooster's Wood-Fired Kitchen**.")
                    print("You enjoyed their famous rotisserie chicken and a glass of wine.")
                    break
                elif ballantyne_choice == "2":
                    print("You chose **North Italia**.")
                    print("Their handmade pasta was exquisite, a true taste of Italy!")
                    break
                elif ballantyne_choice == "3":
                    print("You chose **Gallery Restaurant**.")
                    print("The seasonal menu and art display made for a sophisticated dining experience.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")

        elif travelChoice == "7":  # Uptown
            print("You're in **Uptown**, the heart of Charlotte!")
            while True:
                print("Where would you like to eat in Uptown?")
                print("1: Mert's Heart & Soul (Soul Food)")
                print("2: Tupelo Honey (Southern Comfort)")
                print("3: The Cellar at Duckworth's (Gastropub)")
                uptown_choice = input("> ")

                if uptown_choice == "1":
                    print("You're at **Mert's Heart & Soul**.")
                    print("Their famous shrimp and grits hit the spot!")
                    break
                elif uptown_choice == "2":
                    print("You're at **Tupelo Honey**.")
                    print("The fried chicken and biscuits were amazing, pure Southern comfort!")
                    break
                elif uptown_choice == "3":
                    print("You're at **The Cellar at Duckworth's**.")
                    print("The speakeasy vibe and craft beers were a great experience, along with delicious gastropub fare.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")

        elif travelChoice == "8":  # South End
            print("Welcome to **South End**, a vibrant neighborhood with many trendy spots.")
            while True:
                print("Where would you like to eat in South End?")
                print("1: Superica (Tex-Mex)")
                print("2: Leroy Fox (Southern Fried Chicken)")
                print("3: Culinary Dropout (American Comfort)")
                southend_choice = input("> ")

                if southend_choice == "1":
                    print("You're at **Superica**.")
                    print("The wood-grilled fajitas were a delicious Tex-Mex treat!")
                    break
                elif southend_choice == "2":
                    print("You're at **Leroy Fox**.")
                    print("Their fried chicken is legendary! You enjoyed every bite.")
                    break
                elif southend_choice == "3":
                    print("You're at **Culinary Dropout**.")
                    print("You loved their pretzel bites and provolone fondue, and the lively atmosphere.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")

        elif travelChoice == "9":  # NoDa
            print("You're in **NoDa**, Charlotte's arts district, full of unique eateries.")
            while True:
                print("Where would you like to eat in NoDa?")
                print("1: The Goodyear House (Elevated Southern Comfort)")
                print("2: Salud Cerveceria (Brewery & Pizza)")
                print("3: Brooks' Sandwich House (Classic Burgers)")
                noda_choice = input("> ")

                if noda_choice == "1":
                    print("You chose **The Goodyear House**.")
                    print("The smoked cashew mac and cheese was a standout dish, and the patio was lovely.")
                    break
                elif noda_choice == "2":
                    print("You're at **Salud Cerveceria**.")
                    print("You enjoyed a great craft beer and some fantastic wings.")
                    break
                elif noda_choice == "3":
                    print("You're at **Brooks' Sandwich House**.")
                    print("This cash-only institution lived up to its hype with a classic chili cheeseburger.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")

        # --- Continue Exploring Option ---
        print("\nDo you want to explore more destinations? (yes/no)")
        exploreChoice = input("> ")

        if exploreChoice.lower() == "no":
            print("Thanks for exploring Charlotte! Have a great day!")
            break

if __name__ == "__main__":
    play_game()