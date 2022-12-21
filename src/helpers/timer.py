import time


def timer(func):
    def timer_wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"{func.__name__}: {stop - start:.2f}s to excute.")
        return result

    return timer_wrapper
