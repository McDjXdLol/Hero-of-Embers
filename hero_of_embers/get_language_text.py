import json
class GetTexts:
    LANGUAGES_NAMES = {
        "en": "English",
        "pl": "Polski",
        "es": "Español",
        "fr": "Français"

    }
    @staticmethod
    def load_texts(text, language='en'):
        with open('languages.json', 'r', encoding='utf-8') as f:
            texts = json.load(f)
        return texts.get(language, {})[text]

    @classmethod
    def get_languages_names(cls):
        with open("languages.json", "r", encoding="utf-8") as f:
            texts = json.load(f)

        available_languages = []
        languages_codes = list(texts.keys())
        for lang_code in languages_codes:
            available_languages.append(f"{lang_code}. {cls.LANGUAGES_NAMES.get(lang_code, 'Unknown')}")
        return available_languages, languages_codes
