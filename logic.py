# Задание №3
import requests
from collections import defaultdict
from translate import Translator

# Задание №5
question = {
    "Как тебя зовут?": "Я супер крутой бот,я должен тебе помогать",
    "Сколько тебе лет?": "Это слишком философский вопрос"
}

class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)

    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text in question.keys():
            self.response = question[self.text]
        esle:
            self.response = self.get_answer()
        

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang = from_lang, to_lang = to_lang )
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"
