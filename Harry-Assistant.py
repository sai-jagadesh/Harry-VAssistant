import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import winsound
import psutil
import time as t
import random as r
import webbrowser as w
from email.message import EmailMessage
import smtplib
from docx import Document
import pyautogui
import wolframalpha
import sys
import requests
import os
import json
from requests import get
from keyboard import press
from keyboard import write
from keyboard import press_and_release
import platform
from tkinter import *
import time as t
from tkinter import ttk
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.0)
engine.setProperty('rate',150)
def talk(audio):
    print("Harry:",audio)
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('-'*50)
        print("Listening...")
        winsound.PlaySound("beep_short.wav",winsound.SND_ASYNC)
        r.pause_threshold = 1
        r.energy_threshold = 50
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        formatn = command.capitalize()
        print("User said:",formatn)
    except Exception as e:
        return "None"
    return command

def take_command1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('*'*52)
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 50
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        formatn = command.capitalize()
        print("User said:",formatn)
    except Exception as e:
        return "None"
    return command

def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    talk(name+f" ,it is {battery_percentage} percent.")
    if plugged:
        talk("and It is charging....")
    if not plugged:
        if battery_percentage <= "35%":
            talk(name+" ,plug charger.")

def wish():
    print("\t\t^^^^^^^ASSISTANT ACTIVATED^^^^^^^") 
    winsound.PlaySound("Merged1.wav",winsound.SND_FILENAME) #Audio Credits : YouTube  
    winsound.PlaySound("Intro.wav",winsound.SND_FILENAME)   #Audio Credits : YouTube
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        talk("Good morning "+name+" !")
    elif hour>12 and hour<18:
        talk("Good Afternoon "+name+" !")
    else:
        talk("Good Evening "+name+" !")
    talk("Wishing you a wonderful day... How can I help you ? But, Before that let me check battery")
    battery()
    talk("Ask me what can you do, I will provide you my exciting features !")

def motivation(): #Motivating quotes
    stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
    highMsgs = ['Dont worry dude,every hard time comes to an end']
    talk(r.choice(stMsgs))
    talk('I think this Motivated You ... if Not')
    talk(r.choice(highMsgs))

def time(): #Time
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)

def date(): #Date
    today = datetime.datetime.now()
    talk(today.strftime("%B %d, %Y"))
    now = datetime.datetime.now()
    talk("And it is " + now.strftime("%A"))
    talk("Wishing you a wonderful day")

def developer(): #Developer Info
    talk("My developer is Sai Jagadesh. He created me to use assistants on desktops and laptops that is 64 bit devices")

def joke(): #Jokes
    talk(pyjokes.get_joke())

def Chrome(): #Open chrome
    talk("Opening")
    talk("GOOGLE CHROME")
    try:
        os.startfile("chrome.exe")
    except:
        talk("An error occurred")

def calendar(): #Google Calendar
    talk("Opening")
    talk("GOOGLE CALENDAR")
    w.open("https://calendar.google.com")

def excel(): #MS Excel
    talk("Opening")
    talk("MICROSOFT EXCEL")
    try:
        os.startfile("EXCEL.exe")
    except:
        talk("An error occurred")

def ofile(): #File Explorer
    talk("Opening")
    talk("FILE EXPLORER")
    os.startfile("explorer.exe")

def emailv(): #Sending Email
    try:
        msg = EmailMessage()
        talk("What should I say ?")
        content = take_command()
        talk("What is the subject ?")
        Subj = take_command()
        msg.set_content(content.capitalize())
        talk("Enter your recipient email address")
        to = input("Enter the email id: ")
        msg['Subject'] = Subj.capitalize()
        msg['From'] = "harry.assistant@yahoo.com"
        msg['To'] = to
        talk("Email Sent successfully !")
                
        server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        server.login("harry.assistant@yahoo.com", "qxuaheizmefrkoqy")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(e)
        talk("Sorry my friend. I am not able to send this email")

def emailt(): #Sending Email
    try:
        msg = EmailMessage()
        talk("What should I say ?")
        content = input("Your content: ")
        talk("What is the subject ?")
        Subj = input("Your Subject: ")
        msg.set_content(content.capitalize())
        talk("Enter your recipient email address")
        to = input("Enter the email id: ")
        msg['Subject'] = Subj.capitalize()
        msg['From'] = "harry.assistant@yahoo.com"
        msg['To'] = to
        talk("Email Sent successfully !")
                
        server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
        server.login("harry.assistant@yahoo.com", "qxuaheizmefrkoqy")
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(e)
        talk("Sorry my friend. I am not able to send this email")

def user(): #User name
    username = psutil.users()
    for user_name in username:
        global first_name
        first_name = user_name[0]
        talk(f"This computer is signed to {first_name} as a username.")
        
def system():
    my_system = platform.uname()
    talk(f"The operating system used in your computer is {my_system.system}")
    talk(f"The version of the operating system is {my_system.version}")
    talk(f"The processor used in this system is {my_system.processor}")

def edge(): #MS Edge
    talk("Opening")
    talk("MICROSOFT EDGE")
    os.startfile("msedge.exe")

def calculator(): #Calculator
    talk("Opening")
    talk("CALCULATOR")
    os.startfile("calc.exe")
def map1(): #G Maps
    w.open("https://maps.google.com")
    talk("Opening Maps...")
def close_w(): #Close window
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    talk('Current window is closed.')
def Insta(): #Instagram
    talk("Opening Instagram")
    w.open("https://www.instagram.com")
def IP(): #IP Adress
    ip = get("https://api.ipify.org").text
    talk(f"Your IP address is {ip}")
def per(): #Personalization
    talk("Taking you to personalization interface")
    w.open("https://forms.gle/GVZmsXvF761z6yfDA")
def screenshot():
    talk("Please tell me the name for this screenshot")
    name = take_command()
    talk("Please hold the screen")
    t.sleep(2.0)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    talk("Completed and ready for next command")

def image():
    ws = Tk()
    ws.title('Harry - The AI Assistant')
    img = PhotoImage(file='imagenew1.png')
    Label(
        ws,
        image=img
    ).pack()
    ws.after(4000,lambda:ws.destroy())
    ws.mainloop()

def feature():
    talk("When you say the following task, I will work my best !")
    print("\t\tThing that I can do !!")
    t.sleep(2.0)
    print("1. Open Notepad")
    print("2. What is the time now")
    print("3. What is the Date Today")
    print("4. Who is [person here] ")
    print("5. Tell me something about [something here]")
    print("6. Volume Up")
    print("7. Volume Down")
    print("8. Volume Mute")
    print("9. Keep Timer")
    print("10. Switch Window")
    print("11. Shutdown the system")
    print("12. Restart the system")
    print("13. Sleep the system")
    print("14. Tell me a joke")
    print("15. Who developed you")
    print("16. Tell me the weather in [your state here]")
    print("17. Open Google")
    print("18. Open YouTube")
    print("19. Open Calendar")
    print("20. Open File Explorer")
    print("21. I want to type a document")
    print("22. I want to email")
    print("23. What is the username for this device")
    print("24. Calculate [your math problem here]")
    print("25. Open Calculator")
    print("26. Open Maps")
    print("27. Close this window")
    print("28. Open Instagram")
    print("29. My IP Address")
    print("30. What is [your question here]")
    print("31. I want to personalize you")
    print("32. Take Screen Shot")
    print("33. Auotomation of Google Chrome(Show History, Downloads, Incognito & Open New Tab")
    print("34. Tell me about my system")
    print("35. Sleep [This will sleep the assistant. After sleeping assistant wont respond until you say wake up again !]")
    print("36. Goodbye [After sleeping the assistant & to terminate assistant")
    print("37. Wake Up [To enjoy & make fun with my assistant :)")
    talk("Redirecting to my website for more features !")
    w.open("https://sites.google.com/view/harry-the-assistant")
    t.sleep(2.0)
    print("\t\tHappy Conversation ! Happy People !")
    talk("I will give you a beep, if I am listening to you !")
    t.sleep(5.0)
def tasks():
    wish()
    while True:
        command = take_command()
        if "open Notepad" in command:
            talk("Opening Notepad")
            os.startfile("notepad.exe")
        elif 'what can you do' in command or 'features' in command or 'what can we do' in command:
            feature()
        elif 'harry' in command or 'hey assistant' in command or 'hi assistant' in command or 'assistant' in command or 'How are you' in command:
            talk("Yes, I am fine. How are you ?")
        elif 'I am also fine' in command:
            talk("Glad to hear that !")
        elif 'motivate me' in command or 'motivation' in command:
            motivation()
        elif 'play' in command or 'Play' in command: #Play video on Youtube
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'Time' in command or 'what is the time now' in command:
            time()
        elif 'date' in command or 'day today' in command or 'what is the date today' in command or 'is the date today' in command:
            date()
        elif 'who is' in command: #Search on wikipedia
            person = command.replace('who is', ' ')
            info = wikipedia.summary(person, 2)
            talk("According to wikipedia")
            talk(info)
        elif 'tell me something about' in command:
            whatis = command.replace('tell me something about',' ')
            info = wikipedia.summary(whatis, 2)
            talk("According to wikipedia")
            talk(info)
        elif 'volume up' in command:
            pyautogui.press("volumeup")
        elif 'volume down' in command:
            pyautogui.press("volumedown")
        elif 'volume mute' in command or 'mute' in command:
            pyautogui.press("volumemute")
        elif 'timer' in command or 'stopwatch' in command:
            talk("For how many minutes?")
            timing = take_command()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            talk(f'I will remind you in {timing} seconds')
            t.sleep(timing)
            winsound.PlaySound("Alarm.wav",winsound.SND_FILENAME) #Audio Credits : apple.in
            talk('Your time has been finished '+name)
        elif 'new tab' in command:
            press_and_release('ctrl + t')
            talk("Done "+name)
        elif 'history' in command:
            press_and_release('ctrl + h')
            talk("Done "+name)
        elif 'downloads' in command:
            press_and_release('ctrl + j')
            talk("Done "+name)
        elif 'bookmark' in command:
            press_and_release('ctrl + d')
            press('enter')
            talk("Done "+name)
        elif 'close chrome tab' in command:
            press_and_release('ctrl + w')
            talk("Done "+name)
        elif 'open incognito' in command:
            press_and_release('ctrl + shift + n')
            talk("Done "+name)
        elif 'switch window' in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            t.sleep(1)
            pyautogui.keyUp("alt")
        elif "shut down the system" in command:
            os.system("shutdown /s /t 1")
        elif "restart the system" in command:
            talk("System restarting")
            os.system("shutdown /r /t 1")
        elif "sleep the system" in command:
            talk("The system will sleep in 2 seconds")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'developer' in command or 'who are you' in command or 'who developed you' in command:
            developer()
        elif 'joke' in command or 'tell me a joke' in command:
            joke()
        elif 'my system' in command or 'tell me about my system' in command:
            system()
        elif 'tell me the weather in' in command: #Weather API
            api_key = "e38e4036e53611bc0b64489dbbad51ab"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = command.replace('tell me the weather in', ' ')
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                talk("The temperature in" + city_name + " is " + str(current_temperature) + " in kelvin")
                talk("The atmospheric pressure in" + city_name + " is " + str(current_pressure) + " in Hectopascal Pressure Unit")
                talk("The Humudity in" + city_name + " is " + str(current_humidity) + " percentage")
                talk("The weather condition is currently " + str(weather_description))
            else:
                talk("City Not Found")
        elif 'open youtube' in command or 'youtube' in command or 'can you open youtube' in command or 'open YouTube' in command:
            talk("Opening Youtube")
            w.open_new("https://www.youtube.com")
        elif 'chrome' in command or 'open chrome' in command or 'open Google' in command or 'open google chrome' in command or 'open Google Chrome' in command:
            Chrome()
        elif 'online class' in command or 'teams' in command or 'open teams' in command or 'i want to attend online class' in command or 'open team' in command:
            talk("Opening")
            talk("TEAMS WEB APPLICATION")
            w.open("https://teams.microsoft.com")
        elif 'calendar' in command or 'open calendar' in command or 'open Google calendar' in command:
            calendar()
        elif 'open Excel' in command or 'Excel' in command or 'open Excel' in command or 'i want to work with Excel' in command:
            excel()
        elif 'file explorer' in command or 'files' in command or 'open file explorer' in command:
            ofile()
        elif 'Microsoft Word' in command or 'I want to type a document' in command: #MS Word
            talk("Opening")
            talk("MICROSOFT WORD")
            talk("What is the title ?")
            title = take_command()
            talk("What is the content ?")
            cont = take_command()
            dire = title+".docx"
            doc = Document()
            doc.add_paragraph(cont)
            doc.save(dire)
            talk("Successfully created file.Your document is saved where this assistant is running")
        elif 'email' in command or 'i want to email' in command or 'send email' in command:
            talk("You would like to proceed with voice mail or text mail ? Enter your option below")
            ch = int(input("Voice[1]/Text[2]: "))
            if ch == 1:
                emailv()
            elif ch == 2:
                emailt()
            else:
                talk("Incorrect choice")
        elif 'what is the username for this device' in command or 'user' in command or 'username' in command:
            user()
        elif 'calculate' in command: #Simple math problems
            app_id = '8REQUG-YQ7JGY96T8'
            client = wolframalpha.Client(app_id)
            com = command.replace("Calculate",' ')
            res = client.query(com)
            answer = next(res.results).text
            talk(answer)
        elif 'calculator' in command or 'open calculator' in command:
            calculator()
        elif 'open maps' in command:
            map1()
        elif 'close this window' in command or 'close window' in command or 'close this' in command or 'close' in command:
            close_w()
        elif 'instagram' in command or 'open Instagram' in command:
            Insta()
        elif 'my IP address' in command or 'IP address' in command:
            IP()
        elif 'what is' in command: #Google search
            cont = command.replace('what is', ' ')
            talk("Here are the results for " + cont)
            pywhatkit.search(cont)
        elif 'I want to personalize you' in command or 'personalize yourself' in command or 'edit' in command:
            per()
        elif 'Microsoft edge' in command or 'open Edge browser' in command:
            edge()
        elif 'take screenshot' in command:
            screenshot()
        elif 'goodbye' in command or 'you can close now' in command or 'close' in command:
            talk("Bye "+name)
            winsound.PlaySound("end.wav",winsound.SND_FILENAME)
            print("\t\t---HARRY ALWAYS AT YOUR SERVICE---")
            os._exit(0)
        elif "no thanks" in command or 'sleep' in command:
            talk("You can say wake up, whenever you need me. I am sleeping")
            print("\t\t^^^^^^^ASSISTANT SLEEPING^^^^^^^^")
            break


if __name__ == "__main__":
    image()
    name = input("Harry: What is your name?\nEnter here: ")
    talk("Say hello to activate me !")
    while True:
        permission = take_command1()
        if 'wake up' in permission or 'hello' in permission or 'start' in permission:
            tasks()
        elif 'goodbye' in permission or 'bye' in permission or 'you can close now' in permission or 'close' in permission:
            talk("Bye "+name)
            winsound.PlaySound("end.wav",winsound.SND_FILENAME)
            print("\t\t---HARRY ALWAYS AT YOUR SERVICE---")
            os._exit(0)
