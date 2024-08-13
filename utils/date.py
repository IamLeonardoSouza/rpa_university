from datetime import datetime

def get_current_month_year() -> str:
    """
    Returns the current month and year in the format "MM / YYYY".

    The function retrieves the current date and formats it to display the month and year 
    separated by a slash and a space.

    Returns:
        str: The formatted date string representing the current month and year.
    """
    now = datetime.now()
    formatted_date = now.strftime("%m / %Y")
    return formatted_date
