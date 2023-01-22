import datetime


class Serializer:
    @staticmethod
    def date_to_datetime(date_obj: datetime.date):
        return datetime.datetime.combine(date_obj, datetime.time.min)
