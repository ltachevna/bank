# a = [1, 2, 2, 3]
# d = set(a)
# if len(a) == len(d):
#     print("yes")
# else:
#     print("no")


#
# spis = {"s" : 1, "d" : 2, "f" : 3}
# b = spis.update({"g" : 4})
# a = b.update({("z", "x", "c") : [6, 7, 8]})
# print(a.get("s"))
# a.pop("d")
# print(a.keys)

setik = {'я', 'ты', 'мы'}
a = frozenset(setik)
setik.update(a)
print(setik)
print(a.intersection(setik))
