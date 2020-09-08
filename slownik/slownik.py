slownik = dict()
with open("slownik.txt", "r", encoding="utf-8") as di:
    for line in di:
        line = line.split(" ")
        slownik[line[0]] = line[1].strip()
    print(slownik)

out = str()
with open("source.txt", "r") as file:
    for line in file:
        line = line.split(" ")
        for word in line:
            for key in slownik.keys():
                if key in word:
                    word = word.replace(key, slownik[key])
            out += word
            out += " "

with open("wynik1.txt", "w") as file:
    file.write(out)