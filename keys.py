import math
import random
from primes import Prime



class Keys:
    """ Klasa reprezentująca klucze publiczny oraz prywatny
        Zawiera wszystkie funkcje niezbędne do obliczenia obu kluczów
        Korzysta z klasy liczb pierwszych, pomocnej przy wprowadzeniu wartosci
        Klucz publiczny (N,E) jest to N- moduł dwóch liczb pierwszych oraz E -liczba względnie pierwsza z funkcją eulera
        (moduł liczb pierwszych pomniejszonych o 1)
         - okazuje się że bardzo trudno odnaleźć liczby pierwsze, znając jedynie ich moduł (ale nie znając funkcji Eulera)
        Klucz prywatny (N,D) jest  to N - ten sam moduł oraz D - d*e=1(mod(Eulera))
        """
    def __init__(self,p,q):
        """Konstruktor klucza przyjmuje dwie liczby pierwsze"""
        p = Prime(p)
        q = Prime(q)
        self.prime1=p
        self.prime2=q
        self.n = 0
        self.e = 0
        self.d = 0
        self.h = 0


    def modul(self):
        """ Zwraca n =moduł liczb pierwszych"""
        return self.prime1 * self.prime2

    def func_euler(self):
        """ Zwraca T(n) - funkcję Eulera liczb pierwszych"""
        return (self.prime1 - 1) * (self.prime2 - 1)

    def look_for_e(self):
        """ Zwraca pseudoloswa liczbe wzglednie pierwszą z funkcją eulera
        argumenty: n- modul, h - f. eulera
        """
        self.n = self.modul()
        self.h = self.func_euler()
        number = random.randint(1, (self.n // 2))
        for j in range(number, self.n):
            if (j % 2 != 0) and (j > 1):
                a = self.h
                c = 0
                bufor_j = j
                if self.h < j:
                    a = j
                    j = self.h
                while j != 0:
                    c = a % j
                    a = j
                    j = c
                if a == 1:
                    self.e = bufor_j
                    return bufor_j
                else:
                    return self.look_for_e();

    def inverse_modulo(self):

        """ Zwraca liczbę d, gdzie jej różnica z odwrotnością modularną liczby e jest
        podzielna przez funkcje Eulera  """

        for d in range(1, self.h):
            r = (d * self.e) % self.h
            if r == 1:
                break
        else:
            raise ValueError('%dNie ma odwrotnosci mod %d' % (self.e, self.h))
        self.d = d
        return d

    def get_tab_keys(self):
        "Funkcja zwraca tablicę złożoną z klucza publicznego i prywatnego"
        tab=[]
        tab.append(self.look_for_e())
        tab.append(self.inverse_modulo())
        tab.append(self.modul())
        return tab
