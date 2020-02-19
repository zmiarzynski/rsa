import math

class Prime:
    """ Klasa reprezentująca liczbę pierwszą """

    def __init__(self, number):
        """ Konstruktor, wywołujący enter_authenticated dla liczby. """
        try:
            if self.is_prime(number) is False:
                self.primeNumber = 2
            else:
                self.primeNumber = int(number)
        except ValueError:
            print("Invalid number")
            self.primeNumber = 2

    def __mul__(self, other):
        """ Mnozenie dwoch liczb pierwszych"""
        multiply = self.primeNumber*other.primeNumber
        return multiply

    def __sub__(self, other):
        substitute = self.primeNumber-other
        return substitute

    def enter_prime(self):
        """ Funkcja, która pobiera liczbę od użytkownika """
        pierwsza = input("Podaj liczbę pierwszą:")

        try:
            pierwsza = int(pierwsza)
        except ValueError:
            print("Invalid number")
        return pierwsza

    def is_prime(self,num):
        """ Funkcja sprawdzająca czy liczba jest liczbą pierwszą  """
        num = int(num)
        if (num < 2):
            return False

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def enter_authenticated(self, num):
        """ Funkcja pobierająca od użytkownika liczbę do momentu pobrania właściwej ( liczbypierwszej)"""
        while self.is_prime(num) == False:
            num = self.enter_prime()
        return num
