a = [0] * (4)

a[0] = 64
a[1] = 11
a[2] = 9
a[3] = 25
for i in range(0, 3 + 1, 1):
    for j in range(0, 2 + 1, 1):
        r = a[j]
        w = a[j]
        q = a[j + 1]
        if a[j] > a[j + 1]:
            a[j] = q
            a[j + 1] = w
for i in range(0, 3 + 1, 1):
    print(a[i])
