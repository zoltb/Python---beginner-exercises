import sys


data = sys.stdin.readlines()
input_list = []

for line in data:
    input_list.append(int(line.rstrip()))

printed_lines = input_list[0]
counter = 0


def extract_input(input_list, counter):
    numbers_to_check = input_list[1:]
    for i in numbers_to_check:
        check_number(i)
        counter += 1
    return counter


def check_number(number):
    if int(number) % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")

counter = extract_input(input_list, counter)
