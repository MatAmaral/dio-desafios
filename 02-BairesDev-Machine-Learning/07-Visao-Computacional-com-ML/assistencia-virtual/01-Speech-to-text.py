import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer
import time

#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            speak("Sorry, the service is not available")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    
    mixer.music.load(filename)
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(0.1)
    
    mixer.music.unload()

#function to respond to commands
def respond(text):
    print("Text from get audio: " + text)
    if 'youtube' in text:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword:
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on youtube")
    elif 'search' in text:
        speak("What do you want to search for?")
        query = get_audio()
        if query:
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif 'empty recycle bin' in text:
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle bin emptied")
        except:
            speak("Could not empty the recycle bin.")
    elif 'what time' in text:
        strTime = datetime.today().strftime("%H:%M")
        print(strTime)
        speak(f"The time is {strTime}")
    elif 'play music' in text or 'play song' in text:
        speak("Now playing...")
        music_dir = "C:\\Users\\UserName\\Downloads\\Music\\"  # Change to your music directory
        songs = os.listdir(music_dir)
        if songs:
            playmusic(os.path.join(music_dir, songs[0]))
    elif 'stop music' in text:
        speak("Stopping playback.")
        stopmusic()
    elif 'exit' in text:
        speak("Goodbye, till next time")
        exit(0)

def playmusic(song):
    mixer.music.load(song)
    mixer.music.play()

#stop music
def stopmusic():
    mixer.music.stop()


mixer.init() 

while True:
    print("I am listening...")
    text = get_audio()
    if text:
        respond(text)