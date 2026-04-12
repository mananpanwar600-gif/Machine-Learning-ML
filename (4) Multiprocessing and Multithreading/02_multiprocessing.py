''' MULTIPROCESSING'''

''' Why we use it?'''

# CPU bound tasks (eg mathematical computaions, data processing)

# Parallel Execution - Use of multiple cores of CPU

import multiprocessing
import time

def square_numbers(lock):
    for i in range(5):
        time.sleep(1.5)
        with lock:
            print(f"Square: {i*i}")

def cube_numbers(lock):
    for i in range(5):
        time.sleep(1.5)
        with lock:
            print(f"CUBE: {i*i*i}")
            
if __name__ == "__main__":
    print_lock = multiprocessing.Lock()
    ## create two process
    p1 = multiprocessing.Process(target=square_numbers,args=(print_lock,))

    p2 = multiprocessing.Process(target=cube_numbers,args=(print_lock,))

    t = time.time()

    ## start the process
    p1.start()
    p2.start()

    # Wait for process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)