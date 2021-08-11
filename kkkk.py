BUSINESSMAN1 = ["142 Apple Inc", "2500 Google Inc"]
BUSINESSMAN2 = ["125 Samsung Electronics Co., Ltd", "35 MSFT"]
general = BUSINESSMAN1 + BUSINESSMAN2
sortedgeneral = sorted(general, key = lambda stock: int(stock.split()[0]))
print(sortedgeneral)

