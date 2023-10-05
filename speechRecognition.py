import speech_recognition as sr
# Créez une instance du recognizer (reconnaissance vocale)
recognizer = sr.Recognizer()

# Spécifiez le chemin vers votre fichier audio (remplacez "audio.wav" par le chemin de votre fichier)
class speechRecognition():
    def music(nameMusic):
        audio_file_path = nameMusic
        # "5_-4_-3_-2_-1.wav"
        # "/Hackaton/fichier/"+ nameMusic

# Ouvrez le fichier audio
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)  # Enregistrez l'audio depuis le fichier

        try:
    # Utilisez un moteur de reconnaissance vocale approprié
            text = recognizer.recognize_google(audio_data, language="fr-FR")
            return text
        except sr.UnknownValueError:
            print("Impossible de comprendre l'audio.")
        except sr.RequestError as e:
            print("Impossible de demander des résultats ; {0}".format(e))
