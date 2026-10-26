def localized_value(value_en, value_bg=None, value_ru=None, value_de=None, language='en'):
    values = {
        'en': value_en,
        'bg': value_bg or value_en,
        'ru': value_ru or value_en,
        'de': value_de or value_en,
    }
    return values.get(language, value_en) or ''
