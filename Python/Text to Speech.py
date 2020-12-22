# Installed gtts for speech patterns - requires Internet connection.
# Text to Speech
# So here we use something different called  gTTS and os library.

# Function to convert text to speech

from gtts import gTTS
import os

# Latin-1 works but UTF-8 encoding doens't.
f = open(r'C:\Users\KIIT\Desktop\Audio_saved.docx', "r", encoding='UTF-8')
print(f.read())
text_ = str(f)

speech = gTTS(text=text_, lang='en', slow=False)

speech.save("text_to_speech.mp3")
os.system("start text_to_speech.mp3")