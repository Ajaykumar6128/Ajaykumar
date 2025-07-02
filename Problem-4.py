l=[1,2,3,4,5,6,7,8,9]
a = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = {}

for i in l:
    count = 0
    for j in a:
        if j % i == 0:
            count = count+1
    result[i] = count


print(result)

