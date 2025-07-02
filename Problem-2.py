a = int(input("Enter (a) Value: "))

for i in range(a):
    number = 2 * i + 1
    if i == a - 1:
        print(number)  
    else:
        print(number, end=", ")

