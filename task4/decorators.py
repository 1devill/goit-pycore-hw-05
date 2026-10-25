from functools import wraps

def input_error(usage):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                return f"Usage: {usage}"
            except KeyError as error:
                return f"Contact '{error.args[0]}' not found."
        return inner
    return decorator
