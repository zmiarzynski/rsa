import math
import random
from primes import Prime
from keys import Keys


class Cipher:
    """ Klasa odpowiedzialna za przeprowadzenie szyfrowania.
        Korzysta z dwoch kluczy będacych jedną instancja klasy Keys"""

    def __init__(self, p,q):
        """ Zapamiętuje wartości liczb pierwszych oraz wyliczone wartosci klucza"""
        self.key = Keys(p,q)
        self.tab =self.key.get_tab_keys()
        self.klucz_pub = self.tab[0]
        self.klucz_pryw = self.tab[1]
        self.n = self.tab[2]

    def encode(self, tekst):
        """Dla każdego znaku z tekstu, zamienionego na liczbę naturalną (ASCII) przeprowadza obliczenia:
        zaszyfrowany_znak=(znak)^ klucz mod n
        metoda binarnego kwadratu i mnozenia - operacja potęgowania złączona z modulo nie jest trudną operacją
         """

        szyfr = [(ord(char) ** self.klucz_pub) % self.n for char in tekst]
        return szyfr

    def decode(self, zaszyfrowany):
        """Dla każdego znaku z tekstu, zamienionego na liczbę naturalną (ASCII) przeprowadza obliczenia:
                zaszyfrowany_znak=(znak)^ klucz mod n
                Tym razem używamy innego klucza - klucza asymetrycznego
                 """
        tekst = [chr((char ** self.klucz_pryw) % self.n) for char in zaszyfrowany]
        return ''.join(tekst)



