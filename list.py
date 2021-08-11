import random


surname = ["Тимофиевич", "Репич", "Стражевич", "Войтович"]
appraisal = []
for i in enumerate(surname):
    appraisal.append(random.randint(1,10))
    print(i[1], appraisal[i[0]])


