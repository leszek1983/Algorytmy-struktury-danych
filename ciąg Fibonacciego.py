
def Fibonacci(x):

    if(x == 0):
        return 0
    elif(x == 1):
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)


x = int(input("Wprowadź liczbę aby uzyskać wynik ciągu: "))

for i in range(x):
    print(Fibonacci(i))



