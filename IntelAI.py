'''
This my Ai model V.1.0.0.1
This is taken using various sources like :-
'''
import speech_recognition as sr #For user speech to text
import pyttsx3 #For text to speech
import datetime #for telling the date and time
import wikipedia # for acessing info from wikipedia
import webbrowser #for accessing web
import time #for time display
import playsound
import os #some os(Operating System) functions
import subprocess #spawn new processes, connect to their input/output/error pipe
import json #work with JSON(JavaScript Object Notation) data
import requests #proccessing requests
import smtplib #Sending emails



print('Loading your AI personal assistant - IntelAI....')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello , Good Morning , how may I help you ?")
        print("Hello , Good Morning , how may I help you ?")
    elif hour>=12 and hour<18:
        speak("Hello , Good Afternoon ,  how may I help you ?")
        print("Hello , Good Afternoon ,  how may I help you ?")
    else:
        speak("Hello , Good Evening ,  how may I help you ?")
        print("Hello , Good Evening ,  how may I help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")

        except Exception as e:
            speak("Pardon me, I didn't get that , please say that again")
            return "None"
        return query



speak("Loading your AI  assistant IntelAI")
wishMe()


if __name__=='__main__':


    while True:
        query = takeCommand().lower()
        if query==0:
            continue

        if  "stop" in query:
            speak('IntelAI V1.0.0.1 closing....')
            print('IntelAI V1.0.0.1 closing....')
            break



        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube opened !")
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome opened !")
            time.sleep(5)

        elif "python documentation" in query:    
            webbrowser.open_new_tab("https://docs.python.org")
            print("The Official Python Documentation is opened!")
            speak("The Official Python Documentation is opened!")


        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif 'who are you' in query or 'what can you do' in query:
            speak("I am IntelAI V1.0.0.1  , your persoanl assistant.")

        elif "open stackoverflow" in query:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stack overflow opened !")
            
         elif "open stocks" in query:
            webbrowser.open_new_tab("https://in.finance.yahoo.com/")
            speak("Stonks!")    

        elif 'open code' in query:
            codePath = "C:\\Users\\sn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)  
            print("Visual Studio Code's instance opened !")   
            speak("Visual Studio Code's instance opened !")
    
        elif 'open white hat' in query:
            webbrowser.open_new_tab("https://code.whitehatjr.com/s/dashboard")  
  

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://www.republicworld.com")
            speak('Here are some news')
            time.sleep(6)

        elif 'ipl points table' in query:
             webbrowser.open_new_tab("https://www.iplt20.com/points-table/2020")  


        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)

        
        elif 'open school portal' in query:
            webbrowser.open_new_tab("https://aisn.amizone.net/hometemplate/hometemplate")     

        elif "log off" in query or "shut down" in query:
            speak("Ok , your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
     

time.sleep(3)
