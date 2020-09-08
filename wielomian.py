import math as m
import matplotlib.pyplot as plt
import numpy as np

def wprowadz_liczbe():
    while(True):
        try:
            l = float(input())
        except ValueError:
            print("Podano złą liczbę, wpisz liczbe jeszcze raz: ")
            continue
        else:
           break

    return l
def podaj_zakres():
    print("\nPodaj zakres - poczatek i koniec")
    p = int(input())
    k = int(input())
    i = p
    licznik = 0
    while (i < k):
        i =i+ 0.1
        licznik = licznik + 1

    if licznik < 100:
        quit()

    return p, k;

print(""" Dla wielomianiu W(x) = ax^4 + bx^3 + cx^2 + dx + e "
      podaj kolejno wartości dla współczynników a, b, c, d i e.
      """)

a = wprowadz_liczbe()
if a==0:
    print('a nie może być równe 0')
    a= wprowadz_liczbe()
b = wprowadz_liczbe()
c = wprowadz_liczbe()
d = wprowadz_liczbe()
e = wprowadz_liczbe()
#a, b, c, d = -2, 3, 12, 6

#wyswietlanie
print ('W(x) = ', a, end="")
print ('x^4', end="")
if b>0:
    print('+', end ="" )
    print(b, end="")
elif b<0:
    print('-', end="")
    print(-b, end="")
if b!=0:
    print('x^3', end="")
if c>0:
    print('+', end ="" )
    print(c, end="")
elif c<0:
    print('-', end="")
    print(-c, end="")
if c!=0:
    print('x^2', end="")
if d>0:
    print('+', end ="" )
    print(d, end="")
elif d<0:
    print('-', end="")
    print(-d, end="")
if d!=0:
    print('x', end="")
if e>0:
    print ('+', end="")
    print(e)
elif e<0:
    print ('-', end="")
    print (-e)


m=podaj_zakres()
p=m[0]
k=m[1]


x=np.linspace(p, k, 100)
y=a*x**4+b*x**3+c*x**2+d*x+e

tab = []


plt.axis([p, k, -20, 20]) #zmien zakres

plt.xlabel('x')
plt.ylabel('f(x)')
plt. grid(True)
plt.plot(x, y, 'r')


plt.show()





