import math
import random


def wpisz_p():
    pierwsza=input("Podaj liczbe pierwsza:" )

    try:
        pierwsza = int(pierwsza)
    except ValueError:
        print("Invalid number")
    return pierwsza

# tutaj zmiana. zamiast szukania az do znalezienia, trzeba w kolko wywolywac te funkcje gdize indziej
def czy_pierwsza(n):
    n=int(n)
    if (n < 2):
        return False

   # for i in numpy.arange(2,math.sqrt(n)+1,1):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def sprawdz_czy_pierwsza(n):

    while(czy_pierwsza(n)==False):
        n=wpisz_p()


def modul(p,q):
    return p*q

def func_euler(p,q):
    return (p-1)*(q-1)


def szuka_e(n,h):
    number=random.randint(1,(n//2))
    for j in range(number,n):
        if (j%2!=0)and(j>1):
            a=h
            c=0
            bufor_j=j
            if(h<j):
                a=j
                j=h
            while(j!=0):
                c=a%j
                a=j
                j=c
            if(a==1):
                return bufor_j
            else:
                return szuka_e(n,h);





def odwrotnosc_modulo(e, h):
    #szukam d
    for d in range(1, h):
        r = (d * e) % h
        if r == 1:
            break
    else:
        raise ValueError('%dNie ma odwrotnosci mod %d' % (e, h))
    return d


def obliczanie_klucza(p,q):
    tab=[]
    n=modul(p,q)
    h=func_euler(p,q)
    e=szuka_e(n,h)
    tab.append(e)
    d=odwrotnosc_modulo(e,h)
    tab.append(d)
    tab.append(n)
    return tab



def szyfrowanie(klucz_pub,n, tekst):
    # metoda binarnego kwadratu i mnozenia
    szyfr= [(ord(char) ** klucz_pub) % n for char in tekst]
    return szyfr



def deszyfr(klucz_pryw,n, zaszyfrowany):
    tekst = [chr((char ** klucz_pryw) % n) for char in zaszyfrowany]
    return ''.join(tekst)


tab=obliczanie_klucza(17,13)

print(tab[0])

print(tab[1])

print(tab[2])
# e d n
#text="Tekst przed i po zaszyfrowaniu"
#text2=szyfrowanie(tab[0],tab[2],text)
#print(text2)

#print(deszyfr(tab[1],tab[2],text2))

plik= open("tekst.txt","r")

if plik.mode=='r':
    contents=plik.read()
    #print(contents)
    text2 = szyfrowanie(tab[0], tab[2],contents)
    print(text2)
    plik.close()
    with open("nowytekst.txt","w") as nowy_plik:
        for listitem in text2:
            nowy_plik.write('%i ' % listitem)
    nowy_plik.close()


theInts = []
with open("nowytekst.txt","r") as theFile:
    for val in theFile.read().split():
        theInts.append(int(val))
    theFile.close()

print(theInts)

print(deszyfr(tab[1],tab[2],theInts))