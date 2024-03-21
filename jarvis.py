import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia, webbrowser, os,time
from mygpt import mygpt



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Empowering You with Jarvis, Your Ultimate Assistant ")
    time.sleep(1)
    speak("Hello Ritik, I've successfully recognized you. You're looking quite handsome today! How can I assist you further?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

time.sleep(3)
wishMe()
while True:
# if 1:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results.encode("utf-8"))
        speak(results.encode("utf-8"))

    elif "exam" in query:
        speak("You should head off and get ready for your exam.")

    elif "stack" in query:
        speak("A stack is a data structure that stores elements in a Last-In-First-Out (LIFO) manner, primarily used for function call management, expression evaluation, and backtracking algorithms.")
        notesss = takeCommand().lower()
        if "elaborate" in notesss:
            speak("I am providing notes for you")
            time.sleep(1)
            speak("opening notes")
            os.system("start chrome https://www.geeksforgeeks.org/stack-data-structure/")

    
    elif "open chrome" in query:
        speak("opening chrome")
        os.system("start chrome")
        

    elif "close" in query:
        os.system("taskkill /f /im chrome.exe")
        speak("closing chrome")

    elif "stop music" in query:
        speak("closing music player")
        os.system("taskkill /f /im Microsoft.Media.Player.exe")

    elif 'open youtube' in query:
        speak("opening youtube")
        os.system("start chrome https://www.youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")   


    elif 'play music' in query:
        music_dir = 'D:\\ai club\\Projects\\Songs'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'coding' in query:
        codePath = "D:\\Microsoft VS Code\\Code.exe"
        speak("opening vscode paawan")
        os.startfile(codePath)

    elif 'artificial' in query:
        query = query.replace('artificial', '')
        speak('Open ai Activated')
        time.sleep(1)
        ans = mygpt(query)
        speak(str(ans))
