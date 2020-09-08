from copy import copy
import re

ency = dict()
with open('e1', 'r', encoding="utf-8") as f:
    temp = dict()
    current_name = ""
    for line in f:
        value = line.split()
        if re.match(str(value), "Nazwa"):
            if ency is dict():
                ency[current_name] = temp
            p = ""
            for val in range(1, len(value)):
                p += value[val] + (" " if val != len(value) - 1 else "")
            current_name = p
        if re.match(str(value), "Moc"):
            p = ""
            for val in range(1, len(value)):
                p += value[val] + (" " if val != len(value) - 1 else "")
            temp["Moc"] = p
        if re.match(str(value), "Pasazerowie"):
            p = ""
            for val in range(1, len(value)):
                p += value[val]
            temp["Pasazerowie"] = p  + (" " if val != len(value) - 1 else "")
            ency[current_name] = copy(temp)

for id, key in enumerate(ency.keys()):
    print(str(id + 1) + ": " + key)


a = input("Podaj nazwę samochodu, aby uzyskać więcej informacji: ")
a_wzorzec = "\w" + a + "\w"

#for key, result in ency.items():
#    if re.match(str(a_wzorzec), key):
#        print(key, ": ", result)

for key, result in ency.items():
    if a in key:
        print(key, ": ", result)

