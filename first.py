#!usr/bin/python3

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def run_chatbot():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print()
        print('Start speaking..')
        speak_text('Listening..')
        recordedaudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recordedaudio, language='en-in')
        command = command.lower()

        if 'alexa' in command:
            command = command.replace('alexa', '')
            print('You said', command)

        else:
            print('You said:', command)

        if 'hello' in command:
            print('Hello how can i helpp you ??')
            speak_text('Hello, how can i help you ??')

        elif 'who are you' in command:
            print('I am mini alexa a k a your virtual assistant master')
            speak_text('I am mini alexa a k a your virtual assistant master\
                        how can i help you')

        elif 'can you do' in command:
            print('''I can play songs on youtube , tell you a joke, search on wikipedia,
                  tell date and time,find your location, locate area on map,
                  open different websites like instagram, youtube,gmail, git hub, stackoverflow and
                  searches on google.How may i help you ??''')

            speak_text('''I can play songs on youtube , tell you a joke, search on wikipedia,
                  tell date and time,find your location, locate area on map,
                  open different websites like instagram, youtube,gmail, git hub, stackoverflow and
                  searches on google.How may i help you ??''')

        elif 'play' in command:
            song = command.replace('play', '')
            print(f'Playing {song}')
            speak_text(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'date and time' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            d2 = today.strftime("%B %d, %Y")        # Textual month, day and year
            print(f'Today date is {d2} current time is {time}')
            speak_text(f'Today date is {d2} current time is {time}')

        elif 'time and date' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
            d2 = today.strftime("%B %d, %Y")        # Textual month, day and year
            print(f'Today date is {d2} current time is {time}')
            speak_text(f'Today date is {d2} current time is {time}')

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(f'The current time is {time}')
            speak_text(f'The current time is {time}')

        elif 'date' in command:
            today = date.today()
            print(f'Today date: {today}')
            d2 = today.strftime("%B %d, %Y")        # Textual month, day and year
            print(f'Today date: {today}')
            speak_text(f'Today date: {today}')

        elif 'tell me about' in command:
            name = command.replace('tell me about', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak_text(info)

        elif 'wikipedia' in command:
            name = command.replace('wikipedia', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak_text(info)

        elif 'what is' in command:
            name = command.replace('what is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak_text(info)

        elif 'who is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            speak_text(info)

        elif 'what is' in command:
            search = f'https://www.google.com/search?q={command}'
            print('Here is what i found on the internet..')
            speak_text('searching... Here is what i found on the internet..')
            webbrowser.open(search)

        elif 'joke' in command:
            _joke = pyjokes.get_joke()
            print(_joke)
            speak_text(_joke)

        elif 'search' in command:
            search = f'https://www.google.com/search?q={command}'
            speak_text('searching...')
            webbrowser.open(search)

        elif 'my location' in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak_text("You must be somewhere near here, as per Google maps")

        elif 'locate' in command:
            speak_text('locating ...')
            loc = command.replace('locate', '')

            if 'on map' in loc:
                loc = loc.replace('on map', '')
                url = f'https://google.nl/maps/place/{loc}/&amp;'
                webbrowser.get().open(url)
                print(f'Here is the location of {loc}')
                speak_text(f'Here is the location of {loc}')

        elif 'on map' in command:
            speak_text('locating ...')
            loc = command.split()
            print(loc[1])

            url = f'https://google.nl/maps/place/{loc[1]}/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of {loc[1]}')
            speak_text('Here is the location of {loc[1]}')

        elif 'location of' in command:
            speak_text('locating ...')
            loc = command.replace('find location of', '')
            url = f'https://google.nl/maps/place/{loc[1]}/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of {loc[1]}')
            speak_text('Here is the location of {loc[1]}')

        elif 'where is ' in command:
            speak_text('locating ...')
            loc = command.replace('where is', '')
            url = f'https://google.nl/maps/place/{loc[1]}/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of {loc[1]}')
            speak_text('Here is the location of {loc[1]}')

        elif 'bootcamps' in command:
            search = 'http://tathastu.twowaits.in/index.html#courses'
            speak_text('opening boot camps')
            webbrowser.open(search)

        elif 'boot camps' in command:
            search = 'http://tathastu.twowaits.in/index.html#courses'
            speak_text('opening boot camps')
            webbrowser.open(search)

        elif 'python bootcamp' in command:
            search = 'http://tathastu.twowaits.in/kickstart_python.html'
            speak_text('showing pythonboot camp')
            webbrowser.open(search)

        elif 'data science bootcamp' in command:
            search = 'http://tathastu.twowaits.in/kickstart_data_science.html'
            speak_text('showing data science and ml bootcamp')
            webbrowser.open(search)

        elif 'open google' in command:
            print('opening google ...')
            speak_text('opening google..')
            webbrowser.open_new('https://www.google.co.in/')

        elif 'gmail' in command:
            print('opening gmail ...')
            speak_text('opening gmail..')
            webbrowser.open_new('https://mail.google.com/')

        elif 'open youtube' in command:
            print('opening you tube ...')
            speak_text('opening you tube..')
            webbrowser.open_new('https://www.youtube.com/')

        elif 'open instagram' in command:
            print('opening instagram ...')
            speak_text('opening insta gram...')
            webbrowser.open_new('https://www.instagram.com/')

        elif 'open stack overflow' in command:
            print('opening stackoverflow ...')
            speak_text('opening stack overflow...')
            webbrowser.open_new('https://stackoverflow.com/')

        elif 'open github' in command:
            print('opening git hub ...')
            speak_text('opening git hub...')
            webbrowser.open_new('https://github.com/')

        elif 'bye' in command:
            print('good bye, have a nice day !!')
            speak_text('good bye, have a nice day !!')
            sys.exit()

        elif 'thank you' in command:
            print("your welcome")
            speak_text('your welcome')

        elif 'stop' in command:
            print('good bye, have a nice day !!')
            speak_text('good bye, have a nice day !!')
            sys.exit()

        elif 'tata' in command:
            print('good bye, have a nice day !!')
            speak_text('good bye, have a nice day !!')
            sys.exit()

        else:
            print(' Here is what i found on the internet..')
            speak_text('Here is what i found on the internet..')
            search = f'https://www.google.com/search?q={command}'
            webbrowser.open(search)

    except Exception as ex:
        print(ex)

print('Clearing background noise...Please wait')
speak_text('Clearing background noise...Please wait')

print("hello, i am mini alexa how can i help you ??")
speak_text("hello i am mini alexa how can i help you ")

while True:
    run_chatbot()
