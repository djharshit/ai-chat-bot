#!/home/djharshit/Videos/chat/bin/python3

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import webbrowser
from datetime import date

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1])
engine.setProperty('rate', 150)
