from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Enter contact name and/or phone number."
        except KeyError:
            return "There is no such contact"
    return inner
