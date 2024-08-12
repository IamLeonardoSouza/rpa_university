from datetime import datetime


def get_current_month_year():
    now = datetime.now()
    formatted_date = now.strftime("%m / %Y")
    return formatted_date
