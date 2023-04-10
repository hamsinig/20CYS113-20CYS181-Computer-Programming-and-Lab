def gradesteel(conditions):
    if conditions[0] > 50:
        h = True
    else:
        h = False
    if conditions[1] > 5600:
        t = True
    else:
        t = False
    if conditions[2] < 0.7:
        c = True
    else:
        c = False
    if h == True and t == True and c == True:
        grade = 10
    else:
        if h == True and t == False and c == True:
            grade = 9
        else:
            if h == False and t == True and c == True:
                grade = 8
            else:
                if h == True and t == True and c == False:
                    grade = 7
                else:
                    if h == True or t == True or c == True:
                        grade = 6
                    else:
                        if h == False and t == False and c == False:
                            grade = 5
    
    return grade

# Main
print("enter number of steels that you would like to grade.")
n = int(input())
conditions = [0] * (3)

for i in range(0, n - 1 + 1, 1):
    print("enter the hardness of steel " + str(i + 1))
    hardness = int(input())
    while hardness <= 0:
        print("hardness of steel is always greater than 0. please enter valid hardness of steel.")
        hardness = int(input())
    conditions[0] = hardness
    print("enter the tensile strength of steel " + str(i + 1))
    tensile = int(input())
    while tensile <= 0:
        print("tensile strength of steel is always greater than 0. please enter valid tensile strength of steel.")
        tensile = int(input())
    conditions[1] = tensile
    print("enter the carbon content of steel " + str(i + 1))
    carbon = float(input())
    while carbon < 0 or carbon > 100:
        print("carbon content of steel always lies between 0 and 100. please enter valid tensile strength of steel.")
        carbon = float(input())
    conditions[2] = carbon
    grade = gradesteel(conditions)
    print("Grade of steel " + str(i + 1) + "is " + str(grade))
