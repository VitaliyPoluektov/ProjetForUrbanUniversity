class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding = 'utf-8') as file:
                file = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')
                words = file.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        result = {}
        for i, word_ in self.get_all_words().items():
            for j, wd in enumerate(word_, 1):
                if wd == word.lower():
                    result[i] = j
                    break
        return result

    def count(self, word):
        result={}
        for i, word_ in self.get_all_words().items():
            result[i] = word_.count(word.lower())
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder2 = WordsFinder('test_file.txt', 'child.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print(finder2.find('ChiLd'))
print(finder2.count('ChIlD'))

