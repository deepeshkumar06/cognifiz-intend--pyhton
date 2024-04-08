def generate_fibonacci(n):
    fib_sequence = []
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        fib_sequence = [0]
    elif n == 2:
        fib_sequence = [0, 1]
    else:
        fib_sequence = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fib_sequence.append(b)
    return fib_sequence

num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
if( num_terms > 0 ):
    fibonacci_sequence = generate_fibonacci(num_terms)
    print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)
else:
     print("Please enter a valid integer.")

