import sports
import speech_recognition as sr
import gtts 
from gtts import gTTS
import playsound
import random
from time import ctime
import win32com.client as wincl
import datetime
import time
import os
now = datetime.datetime.now()


r = sr.Recognizer()
speak = wincl.Dispatch("SAPI.SpVoice")

#speak("please tell us which one sport do you want to see")
#pick =  str(input("which one:-------"))
def record_audio(ask = False):
        if ask:
                speak.Speak(ask)
        with sr.Microphone() as source:
                voice_data = " "
                audio = r.listen(source)
                try:
                        voice_data = r.recognize_google(audio)
                        print(voice_data)
                except sr.UnknownValueError:
                        speak.Speak('i did not get what you are saying sorry')
                        speak.Speak('please what are you saying')
                except sr.RequestError:
                        speak.Speak('i did not get what you are saying sorry')
                        speak.Speak('please what are you saying')
                return voice_data  

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
            
def respond(voice_data):
    if "football" in voice_data:
        speak.Speak("is it today match, odds , team or team points")
        if "today match" in voice_data:
            all_matches = sports.all_matches()
            football = all_matches[sports.FOOTBALL]
            speak.Speak(football)
        if "odds" in voice_data:
            speak.Speak("which match odds are you looking for")
            sports = sports.get_sport(sports.FOOTBALL)
            speak.Speak = (sports.ODDS,odd)
        if "odds" in voice_data:
            speak.Speak("which match points are you looking for")
            sports = sports.get_sport(sports.FOOTBALL)
            print = (sports.POINTS,points)
        else:
            if "team" in voice_data:
                speak.Speak("which team")
                voice_data = ''
                football = sports.get_team(sports.FOOTBALL,team)
                speak.Speak(football)
    else:
        if "tennis" in voice_data:
            speak.Speak("is it today match or player name or odds")
        if "today match" in voice_data:
            all_matches = sports.all_matches()
            tennis = all_matches[sports.TENNIS]
            speak.Speak(tennis)
        if "odds" in voice_data:
            speak.Speak("which match odds are you looking for")
            sports = sports.get_sport(sports.TENNIS)
            speak.Speak  = (sports.ODDS,odd)
        else:
            if "player name" in voice_data:
                speak.Speak("which player")
                print("--------------")
                team = input("----")
                print("--------------")
                tennis = sports.get_team(sports.TENNIS,team)
                print(tennis)

    time.sleep(1)
    while 1: 
            voice_data = record_audio()
            respond(voice_data)
    

