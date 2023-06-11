import calendar
from django.core.exceptions import ValidationError

day_abbreviations = list(calendar.day_abbr)


def validate_days_of_week(value):
    valid_days = set(day_abbreviations)
    if not set(value).issubset(valid_days):
        raise ValidationError("Invalid days entered. Valid days are: {}".format(valid_days))
    if len(value) != len(set(value)):
        raise ValidationError("Days of the week must be unique.")
