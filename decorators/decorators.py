import time
import functools

def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def counter(func):
    count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function {func.__name__} called {count} times")
        return func(*args, **kwargs)
    return wrapper

def memo(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

# Пример использования декораторов

@benchmark
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Без декоратора
start_time = time.time()
result = fibonacci_recursive(30)
end_time = time.time()
print(f"Time taken to calculate fibonacci_recursive without decorators: {end_time - start_time} seconds")
print(f"Fibonacci result without decorators: {result}")

@memo
def fibonacci_recursive_memo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive_memo(n - 1) + fibonacci_recursive_memo(n - 2)

# С декоратором memo
start_time = time.time()
result = fibonacci_recursive_memo(30)
end_time = time.time()
print(f"Time taken to calculate fibonacci_recursive with memo decorator: {end_time - start_time} seconds")
print(f"Fibonacci result with memo decorator: {result}")

