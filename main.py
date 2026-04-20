class TextStatistics:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def character_count(self):
        return len(self.text)

    def sentence_count(self):
        return self.text.count('.') + self.text.count('!') + self.text.count('?')

    def average_word_length(self):
        words = self.text.split()
        return sum(len(word) for word in words) / len(words)

    def most_common_word(self):
        words = self.text.split()
        word_count = {}
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return max(word_count, key=word_count.get)

    def text_statistics(self):
        print(f"Sozlar soni: {self.word_count()}")
        print(f"Harflar soni: {self.character_count()}")
        print(f"Fikr yurituvchi birliklar soni: {self.sentence_count()}")
        print(f"O'rtacha so'z uzunligi: {self.average_word_length()}")
        print(f"Eng ko'p ishlatilgan so'z: {self.most_common_word()}")


text = "Bu matn uchun statistika chiqarish kerak. Matnning sozlar soni, harflar soni, fikr yurituvchi birliklar soni, o'rtacha so'z uzunligi va eng ko'p ishlatilgan so'zni chiqarish kerak."
statistics = TextStatistics(text)
statistics.text_statistics()
