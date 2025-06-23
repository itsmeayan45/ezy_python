import multiprocessing
import math
import sys
import time

# increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial of a given number
def compute_factorial(num):
    print(f"Computing the factorial of {num}")
    result=math.factorial(num)
    print(f"Factorial of the {num} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,700,8000]
    start_time=time.time()
    # create a pool of worker process
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)

    end_time=time.time()

    print(f"results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")