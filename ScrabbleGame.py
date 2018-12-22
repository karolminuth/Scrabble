import random


class Scrabble:
    def __init__(self, f):
        self.SCRABBLES_SCORES = [(1, "E A O I N R T L S U"),
                                 (2, "D G"),
                                 (3, "B C M P"),
                                 (4, "F H V W Y"),
                                 (5, "K"),
                                 (8, "J X"),
                                 (10, "Q Z")]

        self.LETTER_SCORES = {letter: score for score, letters in self.SCRABBLES_SCORES for letter in letters.split()}

        self.file_path = f
        self.words = self.read_file_and_change_for_big_letters()
        self.values_of_each_word = self.count_value_of_each_word()
        self.dict_word_and_value = dict(zip(self.words, self.values_of_each_word))
        self.max_value = max(self.values_of_each_word)
        self.min_value = min(self.values_of_each_word)

    def read_file_and_change_for_big_letters(self):
        with open(self.file_path, "r") as read:
            lines = read.readlines()
            words = []
            for i in lines:
                words.append(i.strip().upper())

            return words

    def count_value_of_each_word(self):
        values_of_each_word = []
        sum_single_word = 0
        for word in self.words:
            for letter in word:
                sum_single_word += self.LETTER_SCORES[letter]
            values_of_each_word.append(sum_single_word)
            sum_single_word = 0

        return values_of_each_word

    def check_value_of_entered_word(self, word):
        word = word.upper()
        sum_of_word = 0

        for single_letter in word:
            sum_of_word += self.LETTER_SCORES[single_letter]

        return sum_of_word

    def find_word_equal_searched_value(self, value_of_searched_word):
        searched_words = []
        for key, value in self.dict_word_and_value.items():
            if value == value_of_searched_word:
                searched_words.append(key)

        searched_word = ''
        if len(searched_words) > 0:
            random_index_value = random.randrange(len(searched_words))
            searched_word = searched_words[random_index_value]
        else:
            print('There isn\'t a word on this value, nothing to show')
        return searched_word
