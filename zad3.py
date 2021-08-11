answer = input("введите текст:")
total = 0
total1 = 0
for i in answer:
    a = i.lower()
    if a == "а" or  a == "у" or a == "е" or a == "ё" or a == "ы" or a == "о" or a == "э" or a == "я" or a == "и" or a == "ю":
        total += 1
    else:
        total1 += 1
print(total)
print(total1)