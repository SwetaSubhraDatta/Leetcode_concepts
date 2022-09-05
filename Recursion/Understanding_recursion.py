#Here we will understand the funcdemental concepts of recursion before jumping into problems

#Recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
#And hence plays  big part in dynammic programming

#Defination - A function is recursive if it calls itself directly or indirectly
#A recursive function must have a base case and a recursive case

def print_numbers(n):
    if n==5:
        return
    print(n)
    return print_numbers(n+1)


def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a=Fibonacci(n-1)
    b=Fibonacci(n-2)
    return a+b

def main():
    print_numbers(1)
    print(Fibonacci(5))
main()

