# Brandon Morse Simple Deli Shop #

# Step 1: Define the sandwiches and their prices for the deli as a list/array
sandwiches = {
    1: ("Brandon's Club Sanwich", 5.59),
    2: ("Ham Sandwich", 4.99),
    3: ("Veggie Sandwich", 6.49),
    4: ("Grilled Chicken Sandwich", 7.99)
}


# Step 2: Define the chips and drinks along with their prices (simple for now and not an entire list like the sandwiches)
chips_price = 2.99
drink_price = 2.49


# Step 3: Logic to Display the menu
def show_menu():
        print ("\n---Brandon Morse Deli---")
        for key, (name, price) in sandwiches.items():
            # display the total with 2 decimal points (like normal money is displayed)
            print(f"{key}. {name} - ${price:.2f}")   


# Step 4: Ask the user for a number to choose a sandwich
def get_sandwich_choice():

    # Only continue if the user enters a valid number
    while True:
        try:
            choice = int(input("Choose a sandwich(number): "))
            if choice in sandwiches:
                 return sandwiches[choice]
            
            # Do not continue unless the user inputs a number, and that number must be between 1-4 for the listed options
            else:
                 print ("Invalid choice. Please Enter a number 1-4")
        except ValueError:
             print("Please Enter a NUMBER value between 1-4")


# Step 5: Ask the user if they want chips or drinks
def ask_for_addons():
     total = 0

     chips = input("Would you like chips? (y/n): ").lower()
     if chips == "y":
          total += chips_price

     drink = input("Would you like a drink? (y/n): ").lower()
     if drink == "y":
          total += drink_price

     return total 

# Step 6, Main Menu loop:
def mainMenu():
    total_cost = 0

    print ("---Welcome to Brandon's Deli!---")

    while True:
        show_menu()

        # Sandwich Selection   
        name, price = get_sandwich_choice()
        print(f"You currently have: {name} - ${price: .2f}")
        total_cost += price

        total_cost += ask_for_addons()

        # Ask if the user wants to add anything else
        ordering_again = input("Would like to add anything else to your order? (y/n): ").lower()
        if ordering_again != "y":
            break


    # Print out the user's Total and thank them for their order
    print(f"\nYour total is: ${total_cost:.2f}")
    print("Thank you for your order!")