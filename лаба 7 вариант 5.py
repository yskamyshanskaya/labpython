#лаб 7 вариант 5
#Написать класс UserLanguagePreference, который в
#конструкторе принимает список языков в виде строки, которые
#использует пользователей и содержит метод add_lang(lang_str),
#который добавляет язык в список, если его там не существует.
#Данный класс использует инкапсуляцию, для получения используемого списка.

class UserLanguagePreference:
    def __init__(self):
        self._languages = ["Английский", "Французский"]

    def get_languages(self):
        return [w for w in self._languages]

    def add_lang(self, lang_str):
        if lang_str not in self.get_languages():
            self._languages.append(lang_str)

        # Пример использования класса:


user_prefs = UserLanguagePreference()

# Вывод первоначального списка:
print("языки пользователя: " + str(user_prefs.get_languages()))

# Проверка при добавлении нового языка:
user_prefs.add_lang("Испанский")

# Вывод списка с добавленным языком:
print("добавлен новый язык: " + str(user_prefs.get_languages()))

# Проверка при добавлении нового языка:
user_prefs.add_lang("Французский")

# Этот язык уже существует, поэтому не добавит его
print("не добавлен новый язык, потому что он уже был: " + str(user_prefs.get_languages()))