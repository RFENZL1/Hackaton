from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        return str(e)

# Exemple d'utilisation :
text_to_analyze = "Salut"
detected_language = detect_language(text_to_analyze)
print(f"La langue détectée est : {detected_language}")