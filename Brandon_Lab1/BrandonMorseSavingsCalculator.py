from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP


# Step 1: Convert the number into a rounded decimal
def money(value):
    return Decimal(str(value)).quantize(
        Decimal("0.01"),
        rounding = ROUND_HALF_UP
    )

def count_paychecks(start_date, end_date, first_payday, pay_frequency):
    # Step 2: Count the paychecks from the start date to the end date

    if first_payday > end_date:
        return 0

    if pay_frequency == "weekly":
        interval = timedelta(days = 7)
    else:
        interval = timedelta(days = 14)

    # Proceed forward until the payday reaches the pay period the user inputted
    payday = first_payday

    while payday < start_date:
        payday += interval

    count = 0    

    while payday <= end_date:
        count += 1
        payday += interval

    return count  


# Step 3: Calculate the number of days for a full month of expenses to subtract from the total

def calculate_expenses(monthly_expenses, start_date, end_date):

    current_date = start_date
    total_expenses = Decimal("0")

    while current_date <= end_date:

        month_start = current_date.replace(day = 1)

        if current_date.month == 12:
            next_month = current_date.replace(
                year = current_date.year + 1,
                month = 1,
                day = 1
            )
        else: next_month = current_date.replace(
            month = current_date.month + 1,
            day = 1
        )  

        days_in_month = (next_month - month_start).days

        month_end = min(
            end_date,
            next_month - timedelta(days = 1)
        )    

        applicable_days = (month_end - current_date).days + 1

        monthly_portion = (
            monthly_expenses * 
            Decimal(applicable_days) /
            Decimal(days_in_month)
        )

        total_expenses += monthly_portion

        current_date = next_month

        return money(total_expenses)

def calculate_finances(
        paycheck_amount,
        pay_frequency,
        first_payday,
        monthly_expenses,
        end_date
):

    # Step 4: Define the calculations the user will eventual see

    today = date.today()

    if end_date < today:
        raise ValueError("End date cannot be before today!")

    if first_payday > end_date:
        paycheck_count = 0
    else:
        paycheck_count = count_paychecks(
            today,
            end_date,
            first_payday,
            pay_frequency
        )    
    total_income = money(
        paycheck_amount * paycheck_count
    )

    total_expenses = calculate_expenses(
        monthly_expenses,
        today,
        end_date
    )

    net_income = money(
        total_income - total_expenses
    )

    return paycheck_count, total_income, total_expenses, net_income

# Step 5: Prompt the suer to enter the date in YYYY-MM-DD format
def get_date(prompt):

    while True:
        value = input(prompt)

        try:
            return date.fromisoformat(value)

        except ValueError:
            print("Please enter the date in YYYY-MM-DD format!")


# Step 6: Show the user the current date
def main():

    today = date.today()

    print ("===========================")
    print ("   Savings Calculator")
    print ("===========================")

    print (f"\nToday's date: {today}")


    # Step 7: prompt the user to choose weekly or biweekly pay
    while True:
        frequency = input(
            "\nAre you paid weekly or biweekly or biweekly?"
        ).strip().lower()

        if frequency in ("weekly", "biweeky"):
            break

        print("Please enter 'weekly' or 'biweekly'")

        #Step 8: Ask the user HOW MUCH they get paid per-paycheck

    while True:
        try:
            paycheck_amount = money(
                input(
                    "\nHow much is your take-home pay per paycheck? $"
                )
            )

            if paycheck_amount <= 0:
                raise ValueError

            break

        except ValueError:
            print("Please enter a valid positive amount.")

        #Step 9: Ask WHEN the user gets paid next
        print("\nEnter your payday date:")

        first_payday = get_date("Payday (YYYY-MM-DD): ")

        while True:
            try:
                monthly_expenses = money(
                    input(
                "\nWhat are your total monthly expenses? $"
            )
        )

                if monthly_expenses < 0:
                    raise ValueError

                break

            except ValueError:
                print("Please enter a positive number amount!")

while True:
    end_date = get_date(
        "\nWhat date do you want to see your savings?"
        "(YYYY-MM-DD):"
    )

    if end_date >= today:
        break

    print("The end date cannot be before today!")







if __name__ == "__main__":
    main()