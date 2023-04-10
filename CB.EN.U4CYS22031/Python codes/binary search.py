x = [0] * (5)

for i in range(0, 4 + 1, 1):
    x[i] = int(input())
print("enter element to be searched")
n = int(input())
d = 0
t = 4
r = -1
while d <= t:
    m = float(d + t) / 2
    if x[m] <= n:
        d = m + 1
        if x[m] == n:
            r = m
    else:
        t = m - 1
print("index of element is" + str(r))
