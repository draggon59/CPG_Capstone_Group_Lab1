# ticket.py
# Handles ticket file creation


def create_ticket(name, issue, priority):

    # Create text for ticket
    ticket_data = (
        f"User: {name}\n"
        f"Issue: {issue}\n"
        f"Priority: {priority}\n"
    )

    # Create a file
    with open("helpdesk_ticket.txt", "w") as ticket_file:
        ticket_file.write(ticket_data)

    print("\nTicket saved successfully.")
    print("File created: helpdesk_ticket.txt")