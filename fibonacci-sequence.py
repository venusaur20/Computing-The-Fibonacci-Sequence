import math

fib_seq =[0,1]

def fibonacci(iterations):
    
    for n in range(0,iterations):
        fib_seq.append(fib_seq[0] + fib_seq[1])
        del fib_seq[0]

    return fib_seq[1]

iterations = (int(input("What iteration in the Fibonacci sequence would you like to calculate? "))) - 2
print(fibonacci(iterations))
