import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def recur_fib(n):
    if n <= 1:
        return n
    else:
        return recur_fib(n - 1) + recur_fib(n - 2)

@memoize
def memo_fib(n):
    if n <= 1:
        return n
    else:
        return memo_fib(n - 1) + memo_fib(n - 2)

def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

def main():
    n = 35
    print(f"Calculating fibonacci for n={n}...")
    original_result, original_time = measure_time(recur_fib, n)
    memoized_result, memoized_time = measure_time(memo_fib, n)
    print(f"Original fibonacci result: {original_result}, Time taken: {original_time:.6f} seconds")
    print(f"Memoized fibonacci result: {memoized_result}, Time taken: {memoized_time:.6f} seconds")
    print(f"Time saved using the memoized version: {original_time-memoized_time:.6f} seconds")
if __name__ == "__main__":
    main()
