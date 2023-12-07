import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            #print("Exception " + str(e))
            speak("Sorry, I did not get that.")
    return said

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


#let try it
#text = get_audio()
#speak(text)
while True:
    print("I am listening...")
    text = get_audio().lower()
    if 'netflix' in text:
        speak("opening netflix")
        ur2l = f"https://www.netflix.com/ca/login?nextpage=https%3A%2F%2Fwww.netflix.com%2FKids"
        webbrowser.get().open(ur2l)
    if 'youtube' in text:
        speak("Opening youtube")
        url = f"https://www.youtube.com"
        webbrowser.get().open(url)
    elif 'friend' in text:
        speak("yes you are")
    elif  'end this program' in text:
        speak("ok bye")
        exit()
    elif 'search' in text:
        speak("Searching Wikipedia...")
        query = text.replace("search", "")
        result = wikipedia.summary(query, sentences=3)
        speak("According to wikipedia")
        print(result)
        speak(result)
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif 'exit' in text:
        speak("Goodbye, till next time")
        exit()






