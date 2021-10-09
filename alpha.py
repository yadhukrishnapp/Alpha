import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import sys
import PyPDF2
import os
from PyPDF2 import PdfFileReader


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello Good Morning Sir!, have a great day ahead")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Sir!, I see that you are feeling sleepy; so please stay awake and use your time wisely")

    else:
        speak("Good Evening Sir!.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry sir, can you please repeat that....")
        speak("Sorry sir, can you please repeat that....")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia....", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak(f"I am Alpha, your desktop voice assistant, please tell me how may I help you")

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            speak("Sir, what should I search on google")
            find = takeCommand().lower()
            webbrowser.open(f"{find}")

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com")

        elif 'open my mail' in query:
            speak('opening mail')
            webbrowser.open("https://mail.google.com/mail/")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, time now is {strTime} , anything else you want to know sir")

        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open pdf' in query:
            book = open('sample.pdf', 'rb') # Use any random pdf
            speak('opening pdf')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            speak(f"This pdf contains {pages} pages")
            speaker = pyttsx3.init()
            speak(f"Sir, Please enter the page number from which I should start reading")
            start = int(input("Please enter the page number of starting page : "))
            speak(f"Please enter the page number upto which I should read")
            end = int(input("Enter the page number of end page : "))

            for num in range(start, end):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()

        elif 'creator' in query:
            speak('Mr. Yadhu Krishna P P is my creator')
            print('Mr. Yadhu Krishna P P is my creator')

        elif 'thank you' in query:
            speak('I am always at your service sir, anything else you want to know sir')

        elif 'shutdown' in query:
            speak("Bye sir, have a good day")
            sys.exit()