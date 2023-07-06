#5- Program to print the sum of digits.

def sum_of_digits(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

number = int(input("Enter a number: "))


sum_digits = sum_of_digits(number)
print("The sum of digits is:", sum_digits)
