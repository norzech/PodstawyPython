import math as m

def wprowadz_liczbe():
    while(True):
        x= float(input())
        if(x<0):
            print("Podano zla liczbe, sprobuj ponownie")
            continue
        else:
            break
    return x
#wprowadz_liczbe()
#wielkosci dla kuli
def v_kuli():               #objetosc kuli
    print(("Podaj promień kuli: "))
    R = wprowadz_liczbe()
    V= (4*m.pi*R**3)/3
    print("objetosc = ", V)
    return V
def m_kuli():               #masa kuli
    print("Podaj promien kuli: ")
    R = wprowadz_liczbe()
    print("Podaj gestosc kuli: ")
    d = wprowadz_liczbe()

    M= d*(4*m.pi*R**3)/3
    print("Masa = ", M)
    return M
def pp_kuli():              #pole powierzchni kuli
    print("Podaj promien kuli: ")
    R=wprowadz_liczbe()
    P = 4*m.pi*R**2
    print("Pole powierzchni = ", P)
    return P
#wielkosci dla czworoscianu
def v_czworoscian():
    print("Podaj bok czworoscianu: ")
    a=wprowadz_liczbe()
    V=(a**3*m.sqrt(2))/12
    print("objetosc = ", V)
    return V
def m_czworoscian():
    print("Podaj bok czworoscianu: ")
    a = wprowadz_liczbe()
    print ("Podaj gęstosc czworoscianu: ")
    d=wprowadz_liczbe()
    H = (a * m.sqrt(6)) / 3
    Pp = (a ** 2 * m.sqrt(3)) / 2
    V = (H * Pp) / 3
    M=V*d
    print("Masa = ", M)
    return M
def pp_czworoscian():
    print("Podaj bok czworoscianu: ")
    a = wprowadz_liczbe()
    Pp=a**2*m.sqrt(3)
    print("Pole powierzchni = ", Pp)
    return Pp
#wielkosci dla ostroslupa prostego o podstawie prostokata
def v_ostros_prosty():
    print("Podaj dlugosc pierwsszego boku: ")
    a=wprowadz_liczbe()
    print("Podaj dlugosc drugiego boku: ")
    b=wprowadz_liczbe()
    print("Podaj wysokosc ostroslupa: ")
    h=wprowadz_liczbe()
    V=(a*b*h)/3
    print("objetosc = ", V)
    return V
def m_ostros_prosty():
    print("Podaj dlugosc pierwszego boku podstawy: ")
    a = wprowadz_liczbe()
    print("Podaj dlugosc drugiego boku podstawy: ")
    b = wprowadz_liczbe()
    print("Podaj wysokosc ostroslupa: ")
    h = wprowadz_liczbe()
    print("Podaj gestosc ostroslupa: ")
    d=wprowadz_liczbe()
    V=(a*b*h)/3
    M=V*d
    print("Masa = ", M)
    return M
def pp_ostros_prosty():
    print("Podaj dlugosc pierwszego boku podstawy: ")
    a = wprowadz_liczbe()
    print("Podaj dlugosc drugiego boku podstawy: ")
    b = wprowadz_liczbe()
    print("Podaj dlugosc boku trojkata bocznego: ")
    c=wprowadz_liczbe()
    h1=m.sqrt(c**2-a**2)
    h2=m.sqrt(c**2-b**2)
    Pp=a*b+a*h1+b*h2
    print("Pole powierzchni = ", Pp)
    return Pp
#wielkosci dla stozka
def v_stozek():
    print("Podaj promien podstawy stozka: ")
    R=wprowadz_liczbe()
    print("Podaj wysokosc stozka: ")
    H=wprowadz_liczbe()
    V=(m.pi*R**2*H)/3
    print("objetosc = ", V)
    return V
def m_stozek():
    print("Podaj promien podstawy stozka: ")
    R = wprowadz_liczbe()
    print("Podaj wysokosc stozka: ")
    H = wprowadz_liczbe()
    print("Podaj gestosc stozka: ")
    d=wprowadz_liczbe()
    V = (m.pi * R ** 2 * H) / 3
    M=V*d
    print("Masa = ", M)
    return M
def pp_stozek():
    print("Podaj promien podstawy stozka: ")
    R = wprowadz_liczbe()
    print("Podaj dlugosc tworzacej stozka: ")
    l = wprowadz_liczbe()
    Pp=m.pi*R*(R+l)
    print("Pole powierzchni = ", Pp)
    return Pp
#wielkosci dla walca
def v_walec():
    print("Podaj promien podstawy walca: ")
    R = wprowadz_liczbe()
    print("Podaj wysokosc walca: ")
    H = wprowadz_liczbe()
    V=m.pi*R**2*H
    print("objetosc = ", V)
    return V
def m_walec():
    print("Podaj promien podstawy walca: ")
    R = wprowadz_liczbe()
    print("Podaj wysokosc walca: ")
    H = wprowadz_liczbe()
    print("Podaj gestosc walca: ")
    d = wprowadz_liczbe()
    V = m.pi * R ** 2 * H
    M=V*d
    print("Masa = ", M)
    return M
def pp_walec():
    print("Podaj promien podstawy walca: ")
    R = wprowadz_liczbe()
    print("Podaj wysokosc walca: ")
    H = wprowadz_liczbe()
    Pp=2*m.pi*R*(R+H)
    print("Pole powierzchni = ", Pp)
    return Pp

#switch case dla wybrania wielkosci
def kula(n):
    if n == 1:
        v_kuli()
    elif n == 2:
        m_kuli()
    elif n == 3:
        pp_kuli()
    else:
        print("Do tej liczby nie jest przypisana zadna wielkosc")
def czworoscian(n):
    if n == 1:
        v_czworoscian()
    elif n == 2:
        m_czworoscian()
    elif n == 3:
        pp_czworoscian()
    else:
        print("Do tej liczby nie jest przypisana zadna wielkosc")
def ostros_prosty(n):
    if n == 1:
        v_ostros_prosty()
    elif n == 2:
        m_ostros_prosty()
    elif n == 3:
        pp_ostros_prosty()
    else:
        print("Do tej liczby nie jest przypisana zadna wielkosc")
def stozek(n):
    if n == 1:
        v_stozek()
    elif n == 2:
        m_stozek()
    elif n == 3:
        pp_stozek()
    else:
        print("Do tej liczby nie jest przypisana zadna wielkosc")
def walec(n):
    if n == 1:
        v_walec()
    elif n == 2:
        m_walec()
    elif n == 3:
        pp_walec()
    else:
        print("Do tej liczby nie jest przypisana zadna wielkosc")

def wybor_wielkosc():
    print("""
    Wybierz wielkosc, ktora cie interesuje:
    objetosc  ---  1
    masa  ---  2
    pole powierzchni --- 3
    
    Pamietaj by pozniej przy podawaniu odpowiednich danych zachowac jednostki!
    """)
    while (True):
        try:
            a = int(input("Podaj numer wielkosci ktora chcesz policzyc: "))
            if a < 0:
                print("Wpisano zle dane, sprobuj jeszcze raz")
                continue
            if a == 0:
                print("Wpisano zle dane, sprobuj jeszcze raz")
                continue
            elif a > 3:
                print("Wpisano zle dane, sprobuj jeszcze raz")
                continue
            else:
                break
        except (TypeError, ValueError):
            print("wpisano znak, sprobuj ponownie")
            continue
    return a

def l_kula():
    n = wybor_wielkosc()
    kula(n)
def l_czworoscian():
    n = wybor_wielkosc()
    czworoscian(n)
def l_ostros_protsty():
    n = wybor_wielkosc()
    ostros_prosty(n)
def l_stozek():
    n = wybor_wielkosc()
    stozek(n)
def l_walec():
    n = wybor_wielkosc()
    walec(n)

def wybor_figury():
    print("""
       Wybierz figure, ktora cie interesuje:
       kula  ---  1
       czworoscian  ---  2
       ostroslup prosty i podstawie prostakatu  ---  3
       stozek  ---  4
       walec  ---  5
       """)
    while (True):
        try:
            a = int(input("Podaj numer figury: "))
            if a > 5:
                print("Wpisano zle dane, sprobuj jeszcze raz")
                continue
            else:
                break
        except (TypeError, ValueError):
            print("wpisano znak, sprobuj ponownie")
            continue
    return a

def s_wybor_figury(n):
    if n == 1:
        l_kula()
    elif n == 2:
        l_czworoscian()
    elif n == 3:
        l_ostros_protsty()
    elif n == 4:
        l_stozek()
    elif n == 5:
        l_walec()
    else:
        print("Do tej liczby nie jest przypisana zadna figura")

def program():
    print("""
    Witaj w programie!
    Możesz w nim policzyć objetosc, mase i pole powierzchni wybranych figury
    do kazdej z nich przypisana jest odpowiednia liczba, ktora musisz wpisac,
    aby przejsc do fukcji, ktora po otrzymaniu od ciebie odpowiednich danych 
    wyswietli ci wynik
    Zacznijmy! 
    PS 
    Aby zakonczyc program wpisz 0\n df
    """)
    while(True):
        n = wybor_figury()
        if n == 0:
            print("Do zobaczenia")
            break
        else:
            s_wybor_figury(n)
            continue


program()