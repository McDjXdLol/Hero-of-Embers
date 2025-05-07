import json, os


def check_for_file():
    curr_dir = os.path.dirname(__file__)
    data_dir = os.path.join(curr_dir, "data")
    lang_dir = os.path.join(data_dir, "languages")
    lang_file = os.path.join(lang_dir, f"languages.json")
    return lang_file

class GetTexts:
    LANGUAGES_NAMES = {
        "en": "English",
        "pl": "Polski",
        "es": "Español",
        "fr": "Français"

    }
    TEXT = {}
    check_for_file()

    def get_texts(self):
        with open(check_for_file(), 'r', encoding='utf-8') as f:
            self.TEXT = json.load(f)


    def load_texts(self, text, language='en'):
        if not self.TEXT:
            self.get_texts()
        return self.TEXT[language][text]

    @classmethod
    def get_languages_names(cls):
        with open(check_for_file(), "r", encoding="utf-8") as f:
            texts = json.load(f)

        available_languages = []
        languages_codes = list(texts.keys())
        for lang_code in languages_codes:
            available_languages.append(f"{lang_code}. {cls.LANGUAGES_NAMES.get(lang_code, 'Unknown')}")
        return available_languages, languages_codes
