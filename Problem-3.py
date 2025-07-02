def odd_numbers(a):
    
    if a % 2 == 0:
        modify_odd = a - 1
    else:
        modify_odd = a

    result = []
    for i in range(modify_odd):
        result.append(2 * i + 1)

    return result

a = int(input("Enter (a) value: "))
output = odd_numbers(a)
print("Output:", ', '.join(map(str, output)))

