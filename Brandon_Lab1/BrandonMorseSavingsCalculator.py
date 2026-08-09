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


# Step 3: 