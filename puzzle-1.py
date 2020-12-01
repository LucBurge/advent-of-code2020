expenses = open('input.txt')
arr = []
for a in expenses:
    clean_a = a.rstrip()
    num1 = int(clean_a)
    arr.append(num1)

for i in arr:
    for j in arr:
        for k in arr:
            if i + j + k == 2020:
                num1 = i
                num2 = j
                num3 = k
        

print(f"The product is: {num1*num2*num3}")

