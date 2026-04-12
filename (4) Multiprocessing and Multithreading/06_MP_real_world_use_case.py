'''
Real Wolrd Example: Multi Processing for CPU bound tasks
Scenario: Factorial Calculation for larger numbers
MP improves performance and distribute work load across multiple CPU cores
'''
from concurrent.futures import ProcessPoolExecutor
import math
import time


def factorial(number):
    print(f"Computing Factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result
if __name__ == "__main__":
    numbers = [5000,6000,700,8000]
    start_time = time.time()

    ##create a pool of worker processes
    with ProcessPoolExecutor() as executor:
        results = executor.map(factorial,numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time Taken : {end_time - start_time} seconds")