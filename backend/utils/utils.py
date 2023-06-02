from datetime import datetime


def datetime_format(value):
    try:
        datetime_object = datetime.strptime(value, "%Y-%m-%d_%H:%M")
        return datetime_object.strftime("%d/%m/%Y - %Hh%M")
    except ValueError:
        try:
            datetime_object = datetime.strptime(value, "%Y-%m-%d")
            return datetime_object.strftime("%d/%m/%Y")
        except ValueError:
            return value
