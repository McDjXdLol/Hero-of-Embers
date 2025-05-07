import json, os
class GetTexts:
    LANGUAGES_NAMES = {
        "en": "English",
        "pl": "Polski",
        "es": "Español",
        "fr": "Français"

    }
    TEXT = {}

    def get_texts(self):
        with open(f'{os.getcwd()}\\languages\\languages.json', 'r', encoding='utf-8') as f:
            self.TEXT = json.load(f)

    @classmethod
    def load_texts(cls, text, language='en'):
        if not cls.TEXT:
            cls.get_texts(cls)
        return cls.TEXT[language][text]

    @classmethod
    def get_languages_names(cls):
        with open(f'{os.getcwd()}\\languages\\languages.json', "r", encoding="utf-8") as f:
            texts = json.load(f)

        available_languages = []
        languages_codes = list(texts.keys())
        for lang_code in languages_codes:
            available_languages.append(f"{lang_code}. {cls.LANGUAGES_NAMES.get(lang_code, 'Unknown')}")
        return available_languages, languages_codes
