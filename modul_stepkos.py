'''Modul zawiera Szyfr Vigenère'a opracowany przez Jakub Stępkowskiego na potrzeby projektu aplikacji wykonanej w grupie na lekcje praktyki programowania aplikacji lokanych prowadzoną przez Ilonę Nowosad.'''

''' MODUL WERSJA V1.0 Obejmuje:
        - szyfrowanie malych liter alfabetu angielskiego a-z
        - rozszyfrowywanie malych liter alfabetu angielskiego a-z
'''

#Szyfr Vigenère’a
'''Metoda encrypt() sluzy do szyfrowania w argumantach przyjmuje kolejno klucz i tekst do zaszyfrowania'''
'''Metoda decipher() sluzy do rozszyfrowawywania w argumantach przyjmuje kolejno klucz i tekst do rozszyfrowania'''



class Vigenere:
    @staticmethod
    def encrypt(key, text):
        '''Metoda szyfrująca'''
        # Usuniencie spacji na koncach i zamana liter na male
        key = key.strip()
        text = text.strip()
        text = text.lower()

        # Utworznie alfabetu
        # Tablica ASCII - male litery
        alphabet = [chr(l) for l in range(97, 123)]
        
        # Deklaracja niebednych zmiennych
        answer = []
        t = 0

        # Iteracja w celu kodowania
        while True:
            for k in key:
                # Mechanizm pomijajacy spacje
                while text[t] == ' ':
                    answer.append(' ')
                    t += 1

                # Sprawdzanie o ile miejsc przesunac
                bufor1 = alphabet.index(k)
                bufor2 = alphabet.index(text[t])
                bufor3 = bufor1 + bufor2

                # Gdy index jest poza zasiegiem
                if bufor3 > len(alphabet)-1:
                    bufor3 = bufor3 - len(alphabet)

                # Dodanie litery do listy
                answer.append(alphabet[bufor3])
                t+=1

                # Przerwanie petli zwracajac wartosc
                if t > len(text)-1:
                    return ''.join(answer)
  

    @staticmethod
    def decipher(key, text):
        '''Metoda deszyfrowywujaca'''
        # Usuniencie spacji na koncach i zamana liter na male
        key = key.strip()
        text = text.strip()
        text = text.lower()

        # Utworznie alfabetu
        # Tablica ASCII - male litery
        alphabet = [chr(l) for l in range(97, 123)]
        
        # Deklaracja niebednych zmiennych
        answer = []
        t = 0

        # Iteracja w celu dekodowania
        while True:
            for k in key:
                # Mechanizm pomijajcy spacje
                while text[t] == ' ':
                    answer.append(' ')
                    t += 1

                # Sprawdzanie o ile miejsc przesunac
                bufor1 = alphabet.index(k)
                bufor2 = alphabet.index(text[t])
                bufor3 = bufor2 - bufor1

                # Dodanie litery do listy
                answer.append(alphabet[bufor3])
                t+=1

                # Przerwanie petli zwracajac wartosc
                if t > len(text)-1:
                    return ''.join(answer)
  