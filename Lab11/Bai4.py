from datetime import datetime


class DateHandler:

    def __init__(self) -> None:
        pass

    @classmethod
    def format_date(cls, date):
        return date.strftime("%d/%m/%Y")

    @classmethod
    def get_days_between(date1, date2):
        return (date1 - date2).days