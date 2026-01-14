import time

# Decorator to measure and print execution time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' execution time: {end - start:.6f} seconds")
        return result
    return wrapper

# Function to write numbers 1–100 into a file
def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        for num in range(1, 101):
            file.write(str(num) + "\n")

# Recursive factorial function decorated to show execution time
@execution_time
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    write_numbers_to_file("numbers.txt")
    print("Factorial of 10:", factorial(10))
