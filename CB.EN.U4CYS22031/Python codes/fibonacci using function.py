def fibo(n):
    a = 0
    b = 1
    c = 0
    for i in range(1, n + 1, 1):
        c = a + b
        print(str(a) + " + " + str(b) + " = " + str(c))
        a = b
        b = c

# Main
print("enter number fibonics series: ")
n = int(input())
fibo(n)
