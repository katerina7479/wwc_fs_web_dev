import calendar
from django.core.exceptions import ValidationError
import re

day_abbreviations = list(calendar.day_abbr)


def validate_days_of_week(value):
    valid_days = set(day_abbreviations)
    if not set(value).issubset(valid_days):
        raise ValidationError(
            "Invalid days entered. Valid days are: {}".format(valid_days)
        )
    if len(value) != len(set(value)):
        raise ValidationError("Days of the week must be unique.")


def validate_email_address(email_address):
    if re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email_address):
        return email_address
    raise ValidationError(f"The email address {email_address} is not valid")


def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search("[a-z]", password):
        errors.append("Password must contain at least one lowercase character.")
    if not re.search("[A-Z]", password):
        errors.append("Password must contain at least one uppercase character.")
    if not re.search("\d", password):
        errors.append("Password must contain at least one digit.")
    if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character.")
    if errors:
        raise ValidationError(errors)
