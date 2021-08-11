answer = input("введите число:")
total = 0
total1 = 0
a = int(answer)
while a != 0:
    hel = a % 10
    a //= 10
    print(a)
    if hel % 2 == 0:
        total += 1
    else:
        total1 += 1
sum1 = 0
if total > total1:
    for i in answer:
        sum1 += i
else:
    k = 1
    sum1 = 1
    for i in answer:
        if k == 1 or k == 3 or k == 6:
            sum1 *= k
print(sum1)

