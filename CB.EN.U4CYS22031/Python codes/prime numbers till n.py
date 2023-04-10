# input till which number
print("input till which number")
n = int(input())
print("the prime numbers till n are: ")

# first loop for number from 1 to n
for u in range(1, n + 1, 1):
    x = True
    
    # second loop for numbers from 2 to the number we check
    for i in range(2, u - 1 + 1, 1):
        
        # mod function to find if prime number
        if u % i == 0:
            x = False
    if x == True:
        print(u)
