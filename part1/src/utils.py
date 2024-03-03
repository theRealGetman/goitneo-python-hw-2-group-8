def input_error(args_error_label, key_error_label):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, IndexError):
                return args_error_label
            except KeyError:
                return key_error_label
        return inner
    return decorator
