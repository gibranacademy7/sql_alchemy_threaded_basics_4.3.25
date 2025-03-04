# Question 2:

# Write a program that creates two threads and runs them in parallel.

# The first thread prints the numbers from 1 to 100.
# The second thread prints the numbers from 100 to 1 (in descending order).
#==========================================================================

import threading

def print_ascending():
    for i in range(1, 101):
        print(i)

def print_descending():
    for i in range(100, 0, -1):
        print(i)

# Create threads
thread1 = threading.Thread(target=print_ascending)
thread2 = threading.Thread(target=print_descending)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
