#2- Print Fibonacci Series.

def fibonacci(n):
    series = [0, 1]

    for i in range(2, n):
        next_num = series[i - 1] + series[i - 2]
        series.append(next_num)

    return series

num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

fib_series = fibonacci(num_terms)
print("Fibonacci series:", fib_series)

