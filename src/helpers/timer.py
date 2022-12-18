import time


def timer(func):
    def timer_wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"{func.__name__}: {round(stop - start,2)}s to excute.")
        return result

    return timer_wrapper
