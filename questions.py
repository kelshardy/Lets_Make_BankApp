import sys, time 
from whaaaaat import Separator
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("What is 1 + 1?")
answers = ['A - 8', 'B - 2', 'C - 6', 'D - 1']

# print_slow(answers)
input()
print_slow("A - 8")
input()
print_slow("B - 2")
input()
print_slow("C - 6")
input()
print_slow("D - 1")
input()
input("Answer?: ")

