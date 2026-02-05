import datetime

def get_current_year():
    return datetime.datetime.now().year


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
