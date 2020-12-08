# open in pycharm community --- completed
import pyttsx3
import os
import datetime
import pyaudio
import wikipedia
import webbrowser
import smtplib
import datetime
import datetime
import random
from tkinter import *
from Email import *
from speakFun import *
from wishFun import *
from commandFromAudio import *
from battery import *

if __name__ == "__main__":
    WishMe()
    count=0
    while True:
        query=takeCommand().lower()
        #logic for executing task--

        if 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            speak('Searching'+query+'in wikipedia')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'change speaker' in query:
            speak("Sure Nice to have you I am going for now!")
            i=random.randint(0,40)
            engine.setProperty('voice', voices[i].id)
            speak("Changed speaker successfully"+"I am "+ voices[i].name +" Nice to meet you !")

        elif 'open youtube' in query:
            speak("Sure")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Sure")
            webbrowser.open("https://www.google.com")

        elif 'codeforces contest' in query:
            speak("Sure")
            webbrowser.get('chrome').open("https://www.codeforces.com")
            webbrowser.open("https://10xiitian.ibhubs.co/code-playground")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H %M")
            speak("The time is" + strTime)

        elif 'music' in query:
            speak("Sure")
            os.system("open //Applications//Spotify.app")

        elif ('bye' in query) or ('thank' in query):
            speak('okay Bye')
            break

        elif 'email' in query:
            #email ids of targets stored in dictionary--
            d={'adarsh':"adarsh.adarsh.agrawal@gmail.com",'divya':"divyaagrawal8484@gmail.com"}
            try:
                speak("Whom to send Email Adarsh ?")
                name= takeCommand().lower()
                to = d[name]
                speak("What to write in Email ?")
                content =takeCommand()
                SendEmail(to,content) #function declared in new file
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Cant send Email now")
                
        elif 'shut down' in query:
            speak("Are you sure that you want to shut down your PC? Say only YES or NO")
            confirmation = takeCommand().lower()
            if confirmation != 'yes':
                exit()
            else:
                speak("System is shutting down")
                os.system("shutdown /s /t 1")

        elif 'restart' in query:
            speak("Are you sure that you want to restart your PC? Say only YES or NO")
            confirmation = takeCommand().lower()
            if confirmation != 'yes':
                exit()
            else:
                speak("System is restarting")
                os.system("shutdown /r /t 1")

        elif query=='':
            count=count+1
            speak("I am not getting any response from your side . Say Bye to exit")
        elif 'battery' in query:
            speak("sure")
            batteryLife()
        elif 'memory' in query:
            speak("sure")
            memory()
        elif 'network' in query:
            ip()
            
        else:
            speak("I cant answer your query right now")


        if (count>=3):
            speak("Okay Bye for now ")
            break
    pass
