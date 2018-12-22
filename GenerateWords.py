import random


class Words:
    def __init__(self):
        self.SCRABBLES_SCORES = [(1, "E A O I N R T L S U"),
                                 (2, "D G"),
                                 (3, "B C M P"),
                                 (4, "F H V W Y"),
                                 (5, "K"),
                                 (8, "J X"),
                                 (10, "Q Z")]

        self.LETTER_SCORES = {letter: score for score, letters in self.SCRABBLES_SCORES for letter in letters.split()}

        self.create_words()

    def create_words(self):
        with open('Generated.txt', 'w') as words_file:
            for i in range(1000):
                length_of_word = random.randint(3, 14)
                word = ''
                for x in range(length_of_word):
                    letter = random.choice(list(self.LETTER_SCORES.keys()))
                    word += letter
                word += '\n'
                words_file.write(word)
