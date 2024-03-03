class PhoneValidationError(Exception):
    pass


def handle_error(error_label):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                print(error_label)
            except PhoneValidationError:
                print('Phone must be 10 digits')
            except Exception as e:
                print(f'Exception during {func.__name__} >>> {e}')
        return inner
    return decorator
