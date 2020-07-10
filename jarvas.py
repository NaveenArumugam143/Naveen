import os
import speech_recognition as sr
#import pyaudio
#from gtts import gTTS
import pyttsx3
s=sr.Recognizer()
a={"I am Naveen":["Hi Sir","Welcome","What You Want"],"how are you":["I m Fine Sir"],"system work":"You Are Selecting Working with System"}
b={"control panel":"cmd /c control"}

def speech():
    def fun(voice):
        for i in a:
            engine = pyttsx3.init()
            if i==voice:
                engine.say(a[voice])
                engine.runAndWait()
                voi()
            elif voice=="exit":
                engine.stop()
        for j in b:
            if j==voice:
                os.system(j)
                voi()
                        
                    
            elif voice=="exit":
                engine.stop()
    def voi():
        

        with sr.Microphone() as source:
            try:
                
                print("Please Say Something")
                listen=s.listen(source)
                voice=s.recognize_google(listen)
                print(voice)
                fun(voice)
            except sr.UnknownValueError as e:
                print(e)
            except sr.RequestError as e:
                print(e)
    
    voi()

speech()

