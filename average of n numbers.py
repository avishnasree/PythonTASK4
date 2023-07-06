#4- Program to print the average of n numbers.

def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average


n = int(input("Enter the value of n: "))


numbers = []


for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

average = calculate_average(numbers)
print("The average is:", average)

