import speech_recognition as sr
import pyttsx3
import os
from os import startfile
import pyautogui
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
from open_firefox_urls_chrome import open_chrome
import pywikihow
from pywikihow import search_wikihow
import time
from time import sleep
import requests
import keyboard
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from bs4 import BeautifulSoup
import googlesearch
from playsound import playsound
import sys
from plyer import notification

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

print(voices)

engine.setProperty("voice", voices[1].id)
engine.runAndWait()
engine.setProperty("rate", 170)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greeting():
    time = datetime.datetime.now().strftime("%I %M %p")
    search = "temperature"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    # print("data:",data)
    temp = (data.find("div", class_="BNeawe").text)
    temp = temp[:2]
    print("Temp is", temp)
    
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        talk(("Good morning Sir!"))
        talk(f"The time is {time}")
        talk(f"The {search} is {temp} degree celsius")
    
    elif hour >=12 and hour <18:
        talk(("Good afternoon Sir!"))
        talk(f"The time is {time}")
        talk(f"The {search} is {temp} degree celsius")
    
    else:
        talk(("Good evening Sir!"))
        talk(f"The time is {time}")
        talk(f"The {search} is {temp} degree celsius")
        
    talk("")
        
def talkcommand():
    r = sr.Recognizer()
    with sr.Microphone() as sources:
        print("Listening...")
        r.pause_threshold = 1
        
        audio = r.listen(sources)

    try:
        print("Just a second sir!")
        # command = r.recognize_ibm(audio, language="en-UK", username="ziad Hegazi", password="EZnwuWMlF4F9tY_rMI2clbBlLUqiSheXrYzWzmUeMIbs")
        command = r.recognize_google(audio, language="en-US")
        print(f"user said: {command}")
        
    except Exception as e:
        print(f"error is {e}")
        command = "nothing"
    
    return command

if __name__ == "__main__":
    # greeting()
    while True:
        command = talkcommand().lower()
        if "friday" in command:
            talk("Hello sir, how may I help you?")
            while True:
                command = talkcommand().lower()
                if "hello" in command:
                    talk("Hello sir!")