import json, os

lang_file = ""
def check_for_file():
    global lang_file
    cwd = os.getcwd()
    if cwd.endswith("hero_of_embers"):
        lang_file = os.path.join(cwd, "languages", "languages.json")
    else:
        lang_file = os.path.join(cwd, "hero_of_embers", "languages", "languages.json")

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
        with open(lang_file, 'r', encoding='utf-8') as f:
            self.TEXT = json.load(f)

    @classmethod
    def load_texts(cls, text, language='en'):
        if not cls.TEXT:
            cls.get_texts(cls)
        return cls.TEXT[language][text]

    @classmethod
    def get_languages_names(cls):
        with open(lang_file, "r", encoding="utf-8") as f:
            texts = json.load(f)

        available_languages = []
        languages_codes = list(texts.keys())
        for lang_code in languages_codes:
            available_languages.append(f"{lang_code}. {cls.LANGUAGES_NAMES.get(lang_code, 'Unknown')}")
        return available_languages, languages_codes
