import re

class WordsFinder:
    file_names = []

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = re.sub(r'[^\w\s]','', line)
                    line = str.split(line)
                    words.extend(line)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.count(word)
        return result

finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

print(finder2.get_all_words())
print(finder2.find('captain'))
print(finder2.count('captain'))
