import speech_recognition as sr
from speakFun import *
def takeCommand():
    '''Microphone input to string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold =1
        audio= r.listen(source)

    try:
        print("Recognizing ...")
        query =r.recognize_google(audio,language="en-in")
        print("user said -",query)
        return query

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return("none")

