x = [0] * (5)

x[0] = 64
x[1] = 5
x[2] = 46
x[3] = 33
x[4] = 2
for i in range(0, 3 + 1, 1):
    for g in range(0, 4 + 1, 1):
        print(x[g])
    d = i
    for n in range(i + 1, 4 + 1, 1):
        if x[d] > x[n]:
            d = n
    t = x[d]
    x[d] = x[i]
    x[i] = t
    print("after pass " + str(i + 1))
for i in range(0, 4 + 1, 1):
    print(x[i])
