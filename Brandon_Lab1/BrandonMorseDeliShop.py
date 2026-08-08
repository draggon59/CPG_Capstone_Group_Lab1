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

