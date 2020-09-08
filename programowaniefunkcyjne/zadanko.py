import re
import statistics as st #ta biblioteke musisz zainstalowac
from collections import Counter
with open("ksiazka", "r", encoding="utf8") as file:
    book = file.readlines()
    file.close()
book = str(book)
booksplit=book.split(" ")

booksplit=list(filter(lambda a: a!='', booksplit))

#1
#wyrzucenie the, a, an
book1 = list(filter(lambda slowo: (not re.match("^the$", slowo, re.IGNORECASE)) and (not re.match("^a$", slowo, re.IGNORECASE)) and (not re.match("^an$", slowo, re.IGNORECASE)), booksplit))

dlugosci = list(map(lambda slowo: len(slowo), book1))
print("najczestsza dlugosc slowa", st.mode(dlugosci))

#2
#tworzy tablice z pierwszymi literami slow
book2 = list(map(lambda slowo: slowo[0], booksplit))
t_znakow = {}
for i in book2:
    if i in t_znakow:
        t_znakow[i]+=1
    else:
        t_znakow[i]=1
k=Counter(t_znakow)
high=k.most_common(1)
for i in high:
    print("Najwiecej wyrazow zaczyna sie na: " ,i[0]," :", i[1]," ")

#3
def zmiana(w):
    if not re.match("^the$", w, re.IGNORECASE):
        return w.capitalize()
    else:
        return w
bs3=list(map(zmiana, booksplit))
print(bs3)
