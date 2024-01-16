from gradio_client import Client
client = Client("https://facebook-seamless-m4t.hf.space/")
from langdetect import detect


## Translate to english
def arabic_to_eng(text):
    result = client.predict(
        "T2TT (Text to Text translation)",
        "file",
        "",
        "",
        text,
        "Modern Standard Arabic",
        "English",
        api_name="/run"
    )
    return result[1]

def french_to_eng(text):
    result = client.predict(
        "T2TT (Text to Text translation)",
        "file",
        "",
        "",
        text,
        "French",
        "English",
        api_name="/run"
    )
    return result[1]

def translate_to_english(text):
    try:
        language = detect(text)
    except Exception as e:  # Catch a specific exception if possible
        return f"Language detection failed: {e}"

    if language == 'ar':
        return arabic_to_eng(text)
    elif language == 'fr':
        return french_to_eng(text)
    elif language == 'en':  # Corrected language code for English
        return text
    else:
        return "Unsupported language"