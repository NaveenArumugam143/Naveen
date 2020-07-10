import speech_recognition as sr
from gtts import gTTS 
import wikipedia as wp
import os 
import webbrowser as wb
#print(dir(wp))
from googletrans import Translator 
import googletrans
r1=sr.Recognizer()
r2=sr.Recognizer()

with sr.Microphone() as source:
    print("What you want to Speak")
    try:
        audio=r1.listen(source)
        text=r1.recognize_google(audio)
        print(text)
        s=wp.search(text)
        summary=wp.summary(s)
        
    except sr.UnknownValueError:
        print("Cannot Understant")
#return source

    #print(s)
    #print(summary)
translator = Translator()
with sr.Microphone() as source1:
    try:
        print("Specify Language")
       
        
        m=googletrans.LANGUAGES
        print(m)
        lan=r2.listen(source1)
        l=r2.recognize_google(lan)
        string=l.replace(" ","")
        print(string)
        trans = translator.translate(summary,dest=string)
        e=[trans]

        print(e)
    except sr.UnknownValueError:
        print("Cannot Understant")

print(summary)
try:
    
    speech=gTTS(text=trans,slow=False)
    speech.save("Speech.mp3")
    os.system("Speech.mp3")
except sr.UnknownValueError:
    print("Cannot Understant")

