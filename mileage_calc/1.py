n = int(input("How many numbers do you want to check:"))
x = 0

def tribonnaci(n):
    sequence = (0, 1, 2, 3)
    a, b, c, d = sequence
    while n > d:
        d = a + b + c
        a = b
        b = c
        c = d
    return d

while x < n:
    num = input("Number to check:")
    if num == "":
        print("FAIL. Give number:")
    elif int(num) <= -1:
        print(num+"\tFAIL. Number is minus")
    elif int(num) == 0:
        print(num+"\tYES")
    elif int(num) == 1:
        print(num+"\tYES")
    elif int(num) == 2:
        print(num+"\tYES")
    else:
        if tribonnaci(int(num)) == int(num):
            print(num+"\tYES")
        else:
            print(num+"\tNO")
    x = x + 1

