from gtts import gTTS
import os

mytext = 'Bienvenue chez toi'

langue = 'fr'

textSpeech = gTTS(text=mytext, lang=langue, slow=False)

textSpeech.save("Bienvenue test1")
os.popen("Bienvenue test1.mp3")