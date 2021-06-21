from datetime import datetime


class Date:
    def __init__(self, day: str, month: str, year: str):
        self.date = datetime.strptime('{}/{}/{}'.format(day, month, year), "%d/%m/%Y").isoformat()
