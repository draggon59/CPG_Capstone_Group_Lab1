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

    today = date.today()


    