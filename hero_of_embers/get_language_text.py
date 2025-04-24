import json
class GetTexts:
    @staticmethod
    def load_texts(text, language='en'):
        with open('languages.json', 'r', encoding='utf-8') as f:
            texts = json.load(f)
        return texts.get(language, {})[text]

