'''Write a program which can compute the factorial of a given numbers.'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
x=int(input('Enter a number: '))
print ("The factorial of", x, "is",fact(x))