import time
import logging
from functools import wraps

logging.basicConfig(filename='.log',
                    format='[%(levelname)s] %(asctime)s: %(message)s',
                    filemode='a',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


def log(msg: str = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_str = f'({', '.join(list(map(str, args))) if len(args) != 0 else ''}{', ' if len(kwargs) + len(args) != 0 else ''}'
            kwargs_str = f'{', '.join(f'{key}={value}' for (key, value) in kwargs.items()) if len(kwargs) != 0 else ''})'
            params = args_str + kwargs_str
            try:
                start = time.time()
                result = func(*args, **kwargs)
                stop = time.time()
                logging.info(f'{func.__name__}{params} {msg} ({(stop - start): .3f} seconds )')
            except Exception as e:
                logging.error(f'at {func.__name__}{params} ( {e} )')
                raise e
            return result
        return wrapper
    return decorator
