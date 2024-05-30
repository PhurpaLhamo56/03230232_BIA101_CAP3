# Read the input.txt file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

# solution
def print_solution(lines):
    total_sum = 0
    for line in lines:
        first_digit = None
        last_digit = None
        for char in line:
            if char.isdigit():
                if first_digit is None:
                    first_digit = int(char)
                else:
                    last_digit = int(char)
        if first_digit is not None and last_digit is not None:
            number = int(str(first_digit) + str(last_digit))
            total_sum += number
    print(f"The total sum from the given input file is {total_sum}")

# Other parts of code here to run your functions and printing of the required solution.
input_file = "232.txt"
lines = read_input(input_file)
print_solution(lines)
