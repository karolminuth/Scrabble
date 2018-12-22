import ScrabbleGame as ScrabbleGameFile
import GenerateWords as GenerateWordsFile

if __name__ == '__main__':
    condition, first_condition = (True,) * 2
    option, choice = (-1,) * 2

    print('\nWpisz 1, aby otrzymać dane z gotowego ze słowami pliku Dictionary.txt')    # gotowe slowa majace znaczenie
    print('Wpisz 2, aby otrzymać dane z wygenerowanego losowymi literami-słowami pliku Generated.txt\n')
    # generowane slowa nieposiadajace znaczenia, generowane losowo na podstawie kluczy slownika
    # Jest to dodatkowa, niestandardowa opcja, umozliwiajaca wiecej zabawy oraz testowanie programu

    try:
        choice = int(input('Podaj opcje: 1 lub 2 -> '))
    except ValueError:
        print('Niepoprawny typ zmiennej')
    except KeyboardInterrupt:
        print('Nagłe zamknięcie programu')

    while choice != 1 and choice != 2:
        print('Podano niepoprawny numer')
        try:
            choice = int(input('Podaj opcje: 1 lub 2 -> '))
        except ValueError:
            print('Niepoprawny typ zmiennej')
        except KeyboardInterrupt:
            print('Nagłe zamknięcie programu')
        if choice == 1 and choice == 2:
            break

    if choice == 1:
        path_file = 'Dictionary.txt'
        scr = ScrabbleGameFile.Scrabble(path_file)
    else:
        g = GenerateWordsFile.Words()
        path_file = 'Generated.txt'
        scr = ScrabbleGameFile.Scrabble(path_file)

    print('\n\nGra Scrabble\n\n')
    print('Wpisz 1, aby otrzymać najwyższy wynik z pliku')
    print('Wpisz 2, aby wpisać słowo oraz otrzymać wynik dla podanego słowa')
    print('Wpisz 3, aby wpisać wartość oraz otrzymać słowo o tej wartości')
    print('Wpisz 0, aby skończyć grę\n')

    while condition:
        word_to_check = ''
        value_to_find_word = 0
        option = -1

        try:
            option = int(input('\nPodaj opcję gry Scrabble: 0, 1, 2 lub 3 -> '))
        except ValueError:
            print('Niepoprawny typ zmiennej')
        except KeyboardInterrupt:
            print('Nagłe zamknięcie programu')

        if option == 0:
            print('Koniec gry')
            condition = False

        elif option == 1:
            print('Najwyższy wynik z wybranego pliku -> ', scr.max_value)

        elif option == 2:
            try:
                word_to_check = str(input('Wpisz słowo aby sprawdzić wartość-> '))
            except ValueError:
                print('Wpisz słowo')
            except KeyboardInterrupt:
                print('Nagłe zamknięcie programu')

            is_number = {True for letter in word_to_check if letter.isdigit()}
            if word_to_check == '':
                is_number = True

            while is_number:
                word_to_check = str(input('Wpisz słowo (nie liczbę lub brak znaku) aby sprawdzić wartość-> '))
                is_number = {True for letter in word_to_check if letter.isdigit()}
                if word_to_check == '':
                    is_number = True

            print('Wynik dla podanego słowa to', scr.check_value_of_entered_word(word_to_check))

        elif option == 3:
            print('Wpisz wartość aby otrzymać słowo')
            print('Pomoc: max value to ', scr.max_value, ' oraz min value to ', scr.min_value)
            is_letter = True
            while is_letter:
                try:
                    value_to_find_word = str(input('Wpisz wartość -> '))
                except KeyboardInterrupt:
                    print('Nagłe zamknięcie programu')

                is_letter = not str(value_to_find_word).isnumeric()
                if value_to_find_word == '':
                    is_letter = True

            while is_letter:
                value_to_find_word = str(input('Wpisz wartość (nie słowo lub brak znaku) aby otrzymać słowo-> '))
                is_letter = not value_to_find_word.isnumeric()
                if value_to_find_word == '':
                    is_letter = True

            word = scr.find_word_equal_searched_value(int(value_to_find_word))
            if len(word) > 0:
                print('Słowo o podanej wartości to', word)

        else:
            print('Niepoprawny numer - nie z 0-3 opcji gry Scrabble')
