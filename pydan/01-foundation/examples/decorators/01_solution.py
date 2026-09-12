import time


def timer(fn):
    def wrapper(*arg, **kwargs):
        start = time.time()
        result = fn(*arg, **kwargs)
        end = time.time()
        print(f"{fn.__name__} ran in {end - start} time")
        return result

    return wrapper


def debug(fn):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        print(
            f"calling: {fn.__name__} with args {args_value} and kwargs {kwargs_value}"
        )
        print(f"args: {args_value}")
        print(f"kwargs: {kwargs_value}")

        return fn(*args, **kwargs)

    return wrapper


def cache(fn):
    cache_value = {}

    def wrapper(*args):
        result = None
        if args in cache_value:
            return cache_value[args]
        else:
            result = fn(*args)
            cache_value[args] = result
            return result

    return wrapper


# @debug
# def cube_cal(num: int):
#     result = num**2
#     return result


# cube_cal(num=3)


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(3, 4))
print(long_running_function(3, 5))
print(long_running_function(3, 4))
print(long_running_function(3, 5))
