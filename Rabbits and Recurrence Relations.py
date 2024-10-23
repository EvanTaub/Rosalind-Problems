# fibonacci sequence 1 1 2 3 5 8 13 21
# next digit is the sum of the previous two digits except for n = 1 and n= 2
# with given k, which represents produced pairs after a generation (the second term of n in the sequence), determine the amount of rabbits after n months
# multiply second term by k
def fibonacci(n,k):
    if n == 1 or n ==2:
        return 1
    return fibonacci(n-1,k) + k*fibonacci(n-2,k)
print(fibonacci(5,3))