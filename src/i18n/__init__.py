import sys
sys.path.append('../') # src/

import gettext


LANGUAGES = ["en", "ru"]

translations = {
    lang: gettext.translation(
        "messages", localedir="i18n/translations", languages=[lang], fallback=True)
    for lang in LANGUAGES
}


def getTranslator(lang: str):
    default_lang = translations["en"]
    return translations.get(lang, default_lang).gettext


def language_detector(func):
    "Returns the appropriate translator function, depending on the user's Telegram interface language"

    async def wrapper(*args):
        event = args[0]
        user = event.from_user
        language_code = user.language_code
        if language_code not in ["en", "ru"]:
            language_code = "en"
        translator = getTranslator(lang=language_code)
        return (await func(*args, _ = translator))
    return wrapper
