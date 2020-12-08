import pyttsx3

engine = pyttsx3.init()
voices=engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''speak audio'''
    engine.say(audio)
    engine.runAndWait()
    pass
