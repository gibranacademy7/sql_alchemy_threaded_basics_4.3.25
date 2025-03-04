# Question 3:

# "As is well known, due to the GIL (Global Interpreter Lock), execution is not truly parallel.
# Modify the code from question 2 so that the threads run in parallel using multiprocessing
# (see example in example4_count_pr.py)."
#==============================================================================

import multiprocessing

def print_ascending():
    for i in range(1, 101):
        print(i)

def print_descending():
    for i in range(100, 0, -1):
        print(i)

if __name__ == "__main__":
    # Create processes
    process1 = multiprocessing.Process(target=print_ascending)
    process2 = multiprocessing.Process(target=print_descending)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()
