import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y.:' + audio)
    friday.say(audio)
    friday.runAndWait()


def comand():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Tulee" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the comand")
        query=str(input('Your older is: '))
    return query
def time():
    Time=datetime.datetime.now().strftime("%I : %M : %p")
    speak(Time)

time()    

def welcome():
    hour=datetime.datetime.now().hour 
    if hour >=6 and hour <12:
        speak("Good moring Tú")
    elif hour >=12 and hour <18:
        speak("Good afternoon Tú")
    elif hour >=18 and hour <6:
        speak("Good evening Tú")
    
    speak('How can I help You')    

if __name__ == "__main__":
    welcome()  
    while True:
        query=comand().lower()
        if "google" in query:
            speak ("What should I search boss?")
            search=comand().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')