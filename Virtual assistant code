import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import datetime
import pyjokes
from newsapi import NewsApiClient
import winsound
import time
import cv2
import warnings
import requests
import wolframalpha

engine = pyttsx3.init('sapi5') #TTs module
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #0-> Male, 1-> Female

#changing default browser to chrome
webbrowser.register('chrome',	None, 	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

def speak(audio): #audio output function
    engine.say(audio)
    engine.runAndWait()

def wishme(): #function for wishing the user based on time of the day
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("HI, How may I help you.")

def takeCommand(): #Takes microphone input from user & returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #reduces background noises
        print("Listening...")
        winsound.Beep(2000,100)
        r.pause_threshold = 1 #pause time
        audio=r.listen(source)
        
    try:
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in') #google audio recognition 
        print(f"User said: {query}\n") #prints user input

    except Exception as e:
        #print(e) # prints error
        print("Say that again please...")
        #speak("Say that again please")
        query=""

    return query

def logic():
    if __name__== "__main__": #main function
        wishme()
        if 1:
            query=takeCommand().lower() #makes input text in lowercase
            query=" "+query+" "
            #logic for executing task based on query

            if (' open ' in query) and ('.' in query):   #opens any website
                query = query.replace("open", "") #removes open from text
                query = query.replace(" ", "")
                query = query.replace("slash", "/")
                speak("Opening "+query)
                webbrowser.get('chrome').open_new_tab(query)

            elif (' search 'in query) and (' google ' in query):  #searches google 
                query = query.replace("search ", "") #removes search from text
                speak("Searching "+query)
                query = query.replace("google", "") #removes on google from text
                query = query.replace("on ", "")
                webbrowser.get('chrome').open_new_tab("https://www.google.com/search?q="+query)

            elif (' search ' in query) and(' youtube ' in query):  #searches youtube 
                query = query.replace("search ", "") #removes search from text
                speak("Searching "+query)
                query = query.replace("youtube", " ") 
                query = query.replace("on ", " ")
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query="+query)

            elif (' play ' in query) and (' on youtube ' in query):  #plays video on youtube 
                query = query.replace("play ", "") #removes play from 
                query = query.replace(" on youtube ", " ") #removes on youtube from text
                speak("Playing "+ query +"on youtube")
                url = f"https://www.youtube.com/results?q={query}"
                count = 0
                cont = requests.get(url)
                data = cont.content
                data = str(data)
                lst = data.split('"')
                for i in lst:
                    count += 1
                    if i == "WEB_PAGE_TYPE_WATCH":
                        break
                if lst[count - 5] == "/results":
                    print("No Video Found for this Topic!")
                webbrowser.open(f"https://www.youtube.com{lst[count - 5]}")
            
            elif ' wikipedia ' in query: # searches wikipedia and speaks the output 
                speak("Searching Wikipedia...")
                query = query.replace("on wikipedia", "") #removes on wikipedia from text
                result=wikipedia.summary(query, sentences=2) #no. of sentences to be read from wikipedia
                print("According to Wikipedia")
                speak("According to Wikipedia")
                print(result)
                speak(result)
            
            elif ' time ' in query: #tells the current time
                strTime=datetime.datetime.now().strftime('%I:%M %p')
                print("The time is "+strTime)
                speak("The time is "+strTime)

            elif ' date ' in query: #tells todays date
                strDate=datetime.datetime.now().strftime('%B %d,%Y')
                print("Today's date is: "+ strDate)        
                speak("Today's date is: "+ strDate)

            elif ' day ' in query: #tells todays day
                strDay=datetime.datetime.now().strftime('%A')
                print("Today is "+ strDay)        
                speak("Today is "+ strDay)
            
            elif ' screenshot ' in query: #takes screenshot
                speak("Taking screenshot")
                date=datetime.datetime.now().strftime('%d-%m-%Y %I-%M %p')
                img_name=str(date).replace(":","")+"-screenshot.png"
                file_name=('C:\\Users\\USER\\Pictures\\Screenshots\\'+img_name)
                sc=pyautogui.screenshot()
                sc.save(file_name)
                speak("Screenshot Captured")

            elif ' joke ' in query: #tells a joke
                joke=pyjokes.get_joke(language="en",category="all",)
                print(joke)
                speak(joke)

            elif (' news ' in query)or (' headlines ' in query): #tells top 10 headlines (refreshes every 15 minutes)
                newsapi = NewsApiClient(api_key='0b923f88ad8043678cbcc84808217b70')
                data = newsapi.get_top_headlines(language='en',country='in')
                headlines=data['articles']
                for i in range(10):
                    print(i+1,". ",f'{headlines[i]["title"]}')
                    speak(f'{headlines[i]["title"]}')

            elif ' timer ' in query: #sets a timer
                query = query.replace("set", "")
                query = query.replace("a", "")
                query = query.replace("timer", "")
                query = query.replace("for", "")
                query = query.replace(" ", "")
                if 'hour' in query:
                    query = query.replace("hours", "")
                    query = query.replace("hour", "")
                    hour_time = query
                    speak("Setting a timer for: "+hour_time+" hours.")
                    hour=float(hour_time)
                    timer=hour*3600

                elif 'minute' in query:
                    query = query.replace("minutes", "")
                    query = query.replace("minute", "")
                    min_time = query
                    speak("Setting a timer for: "+min_time+" minutes.")
                    min=float(min_time)
                    timer=min*60

                elif 'second' in query:
                    query = query.replace("seconds", "")
                    query = query.replace("second", "")
                    sec_time = query
                    speak("Setting a timer for: "+sec_time+" seconds.")
                    sec=float(sec_time)
                    timer=sec

                time.sleep(timer)
                frequency = 2000 #beep sound
                duration = 100
                for i in range(0,10):
                    winsound.Beep(frequency,duration)
                speak("Time's up")

            elif ((' take 'in query)or(' capture 'in query))and((' image 'in query)or(' photo 'in query)): #takes phto from camera
                cam_port = 0
                cam = cv2.VideoCapture(cam_port)
                # reading the input using the camera
                result, image = cam.read()
                # If image will detected without any error,show result
                if result:
                        # showing result, it take frame name and image
                        speak("Capturing Image")
                        cv2.imshow("Capture", image)
                        # saving image in local storage
                        date=datetime.datetime.now().strftime('%d-%m-%Y %I-%M %p')
                        img_name=str(date).replace(":","")+"-capture.png"
                        cv2.imwrite('C:\\Users\\USER\\Pictures\\Camera Roll\\'+img_name, image)
                        speak("Image saved ")
                        cv2.waitKey(2000)
                        cv2.destroyWindow("Capture")
                        warnings.filterwarnings("ignore")
                # If captured image is corrupted, moving to else part
                else:
                    speak("No image detected. Please! try again") 
            
            elif ' reminder ' in query: #sets a reminder
                speak("Sure,What shall I remind you about?")
                print("What shall I remind you about?")
                text = takeCommand()
                speak("Sure,When shall I remind you?")
                print("When shall I remind you")
                rem_time = takeCommand()
                rem_time = rem_time.replace("in ", "")
                rem_time = rem_time.replace("about ", "")
                rem_time = rem_time.replace(" ", "")
                if 'hour' in rem_time:
                    rem_time = rem_time.replace("hours", "")
                    rem_time = rem_time.replace("hour", "")
                    speak("OK, I shall remind you in "+rem_time+" hours, to "+text)
                    hour=float(rem_time)
                    timer_rem=hour*3600

                elif 'minute' in rem_time:
                    rem_time = rem_time.replace("minutes", "")
                    rem_time = rem_time.replace("minute", "")
                    speak("OK, I shall remind you in "+rem_time+" minutes, to "+text)
                    min=float(rem_time)
                    timer_rem=min*60

                elif 'second' in rem_time:
                    rem_time = rem_time.replace("seconds", "")
                    rem_time = rem_time.replace("second", "")
                    speak("OK, I shall remind you in "+rem_time+" seconds, to "+text)
                    sec=float(rem_time)
                    timer_rem=sec
                time.sleep(timer_rem)
                for i in range(0,10):
                    winsound.Beep(2000,100)
                speak("Its time to "+ text )

            elif (' what ' in query)or(' calculate ' in query)or(' convert ' in query)or(' who ' in query)or (' weather '): #for weather, general questions, conversions and calculations
                question = query
                app_id = '7AQ863-V8KTL6QTVA'
                client = wolframalpha.Client(app_id)
                try:
                    res = client.query(question)
                    answer = next(res.results).text
                    print(answer)
                    speak(answer)
                except:    
                    speak("Sorry I don't know that now")
            
            else:
                pass

logic()      
 

'''
1. Open website (https://docs.python.org/3/library/webbrowser.html)
2. Search google (https://docs.python.org/3/library/webbrowser.html)
3. Seach youtube (https://docs.python.org/3/library/webbrowser.html)
4. Play on youtube (https://pypi.org/project/pywhatkit/)
5. search wikipedia (https://pypi.org/project/wikipedia/)
6. current time (https://docs.python.org/3/library/datetime.html)
7. todays date (https://docs.python.org/3/library/datetime.html)
8. week day (https://docs.python.org/3/library/datetime.html)
9. screenshot (https://pypi.org/project/pywhatkit/)
10. Sending an email ()
11. open any computer application ()
12. tell a joke (https://www.geeksforgeeks.org/python-script-to-create-random-jokes-using-pyjokes/)
13. setting a timer (https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html)
14. setting a reminder (https://hackernoon.com/a-simple-python-reminder-app-m3k42wk)
15. weather, calculations, conversions & questions using wolframalpha api (https://pypi.org/project/wolframalpha/)
16. current news using newsapi(https://www.geeksforgeeks.org/read-latest-news-using-newsapi-python/)
17. mobile messages
18. *Akinator ()
19. *Whatsapp messages ()
20. locating places on google map ()
21. write a note ()
22. play music on computer ()
23. take a photo (https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/)
24. shutdown ()
26. voice recording 
27. open a code vscode
28. to do list
29. google calender
30. ip address
31. 
'''
