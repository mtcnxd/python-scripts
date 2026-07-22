# Helpers functions

def calculate_percentage(current, last):
    current = float(current)
    last = float(last)
    return round(((current - last) / last) * 100, 2)

def to_percentage(number):
    return f"{number:,.2f}%"

def to_currency(number):
    return f"${float(number):,.2f}"
