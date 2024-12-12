from collections import Counter
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(sym, '')
                all_words[name] = info.split()
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():  #прошлись по ключам и значениям словаря
            if word.lower() in words: # если искомое слово в нижнем регистре есть в значениях
                dict_[name] = words.index(word.lower())+1 # формируем словарь, где ключ - это то, что на себя берет name,
        return  dict_                                     # а значение, индекс слова +1 (т.к. индексация с 0

    def count(self, word):
        dict1 = {}
        for name, words in self.get_all_words().items():
            counter = words.count(word.lower()) # запустили счетчик и посчитали заданное слово в ниж. регистре в значениях
            dict1[name] = counter
        return  dict1
             


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

