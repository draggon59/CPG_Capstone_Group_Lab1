# app.py
# Simple IT Help Desk Ticket Application

from pythonscript2 import create_ticket

# Static variable
COMPANY_NAME = "Cloud Fundamentals Help Desk"

def main():
    print("=" * 40)
    print(COMPANY_NAME)
    print("=" * 40)

    # Dynamic variables from user input
    user_name = input("Enter your name: ")
    issue = input("Describe your IT issue: ")
    priority = input("Priority (low, medium, high): ").lower()

    # Conditional logic
    if priority == "high":
        print("High-priority ticket created.")
    elif priority == "medium":
        print("Medium-priority ticket created.")
    else:
        priority = "low"
        print("Low-priority ticket created.")

    # Function call to another Python file
    create_ticket(user_name, issue, priority)


if __name__ == "__main__":
    main()