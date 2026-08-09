from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP

def money(value):
    # Step 1: Convert the number into a rounded decimal
    return Decimal(str(value)).quantize(
        Decimal("0.01"),
        rounding = ROUND_HALF_UP
    )