from task_2 import gcd_iteration, gcd_recursion
from timeit import timeit

def main():
    first_number = int(input("Please enter first number: "))
    second_number = int(input("Please enter second number: "))
    iteration_time = timeit(lambda: gcd_iteration(first_number, second_number), number = 100000)
    recursion_time = timeit(lambda : gcd_recursion(first_number, second_number), number = 100000)
    print(f"time passed iteration: {iteration_time}")
    print(f"time passed recursion: {recursion_time}")
    if iteration_time > recursion_time:
        print(f"recursion is {iteration_time - recursion_time} faster")
    else:
        print(f"iteration is {recursion_time - iteration_time} faster ")

if __name__ == "__main__":
    main()