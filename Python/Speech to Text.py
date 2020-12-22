# To use this I have to install pyaudio - download the correct whl file, see pyaudio installation errors.
# Then run the code pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl and it will install.
# Next I installed python-docx


# Speech to Text

import speech_recognition as sr
import docx, pyttsx3

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    # Time extension is of 1.5 minutes.
    try:
        # using google speech recognition
        data = r.recognize_google(audio_text)
        print("Text: " + data)
        print()
        # print("Text: " + r.recognize_google(audio_text), language = 'ta-IN') text is in tamil.
    except:
        print("Sorry, I did not get that")


mydocx = docx.Document()
mydocx.add_paragraph(data)
mydocx.save(r"C:\Users\KIIT\Desktop\Audio_saved.docx")




