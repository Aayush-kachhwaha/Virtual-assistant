from tkinter import *
from PIL import ImageTk, Image
import keyboard
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

#Main Window
root= Tk()
root.title('Voice Assistant')
root.iconbitmap("icon example.ico")
#root.configure(bg='Black')

#reading assistant name
name_file = open("Assistant_name",'r')
Assistant_name = name_file.read()
name_file.close()

#TTS module initialization.
VA_voice_file = open("Assistant_voice",'r')
VA_voice = VA_voice_file.read()
VA_voice_file.close()
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[int(VA_voice)].id) #0-> Male, 1-> Female//

#changing default browser to chrome
webbrowser.register('chrome',	None, 	webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))

def input(): #Text input
    text_input=text_inputbox.get()
    l2=Label(frame,text=text_input,font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN)
    l2.grid(row=0,column=1,padx=2,pady=2,sticky=N+SW+E)
    text_inputbox.delete(0,END)
    logic(text_input)

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
    name_file = open("Assistant_name",'r')
    Assistant_name = name_file.read()
    name_file.close()
    speak("HI, I am "+Assistant_name+". How may I help you.")

def takeCommand(): #Takes microphone input from user & returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) #reduces background noises
        display("Listening...")
        print("Listening...")
        winsound.Beep(2000,100)
        r.pause_threshold = 1 #pause time
        audio=r.listen(source)
        
    try:
        display("Recognising...")
        print("Recognising...")
        query=r.recognize_google(audio, language='en-in') #google audio recognition 
        print(f"User : {query}") #prints user input

    except Exception as e:
        #print(e) # prints error
        print("Say that again please...")
        display("Say that again please...")
        speak("Say that again please...")
        query="e101"  
    return query

def mic_input(): #Voice input
    VA_voice_file2 = open("Assistant_mode",'r')
    mode=VA_voice_file2.read()
    VA_voice_file2.close()
    if mode=='0':
        while True:
            voice_input=takeCommand()
            l2=Label(frame,text=voice_input,font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN)
            l2.grid(row=0,column=1,padx=2,pady=2,sticky=N+SW+E)
            logic(voice_input)
    else:     
        voice_input=takeCommand()
        l2=Label(frame,text=voice_input,font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN)
        l2.grid(row=0,column=1,padx=2,pady=2,sticky=N+SW+E)
        logic(voice_input)

def logic(input_command):
    if __name__== "__main__": #main function
        if 1:
            query=input_command
            query.lower() #makes input text in lowercase
            query=" "+query+" "
            #logic for executing task based on query

            if (' open ' in query) and ('.' in query):   #opens any website
                query = query.replace("open", "") #removes open from text
                query = query.replace(" ", "")
                query = query.replace("slash", "/")
                display("Opening "+query)
                speak("Opening "+query)
                webbrowser.get('chrome').open_new_tab(query)

            elif (' search 'in query) and (' google ' in query):  #searches google 
                query = query.replace("search ", "") #removes search from text
                display("Searching "+query)
                speak("Searching "+query)
                query = query.replace("google", "") #removes on google from text
                query = query.replace("on ", "")
                webbrowser.get('chrome').open_new_tab("https://www.google.com/search?q="+query)

            elif (' search ' in query) and(' youtube ' in query):  #searches youtube 
                query = query.replace("search ", "") #removes search from text
                display("Searching "+query)
                speak("Searching "+query)
                query = query.replace("youtube", " ") 
                query = query.replace("on ", " ")
                webbrowser.get('chrome').open_new_tab("https://www.youtube.com/results?search_query="+query)

            elif (' play ' in query) and (' on youtube ' in query):  #plays video on youtube 
                query = query.replace("play ", "") #removes play from 
                query = query.replace(" on youtube ", " ") #removes on youtube from text
                display("Playing "+ query +"on youtube")
                speak("Playing "+ query +"on youtube")
                url = f"https://www.youtube.com/results?q={query}"
                count = 0
                cont = requests.get(url)
                data1 = cont.content
                data1 = str(data1)
                lst = data1.split('"')
                for i in lst:
                    count += 1
                    if i == "WEB_PAGE_TYPE_WATCH":
                        break
                if lst[count - 5] == "/results":
                    display("No Video Found for this Topic!")
                    print("No Video Found for this Topic!")
                webbrowser.open(f"https://www.youtube.com{lst[count - 5]}")
            
            elif ' wikipedia ' in query: # searches wikipedia and speaks the output 
                speak("Searching Wikipedia...")
                query = query.replace("on wikipedia", "") #removes on wikipedia from text
                result=wikipedia.summary(query, sentences=2) #no. of sentences to be read from wikipedia
                print("According to Wikipedia")
                display("According to Wikipedia")
                speak("According to Wikipedia")
                print(result)
                display(result)
                speak(result)
            
            elif ' time ' in query: #tells the current time
                strTime=datetime.datetime.now().strftime('%I:%M %p')
                display("The time is "+strTime)
                speak("The time is "+strTime)

            elif ' date ' in query: #tells todays date
                strDate=datetime.datetime.now().strftime('%B %d,%Y')
                display("Today's date is: "+ strDate)        
                speak("Today's date is: "+ strDate)

            elif ' day ' in query: #tells todays day
                strDay=datetime.datetime.now().strftime('%A')
                display("Today is "+ strDay)        
                speak("Today is "+ strDay)
            
            elif ' screenshot ' in query: #takes screenshot
                display("Taking screenshot")
                speak("Taking screenshot")
                date=datetime.datetime.now().strftime('%d-%m-%Y %I-%M %p')
                img_name=str(date).replace(":","")+"-screenshot.png"
                file_name=('C:\\Users\\USER\\Pictures\\Screenshots\\'+img_name)
                sc=pyautogui.screenshot()
                sc.save(file_name)
                display("Screenshot Captured")
                speak("Screenshot Captured")

            elif ' joke ' in query: #tells a joke
                joke=pyjokes.get_joke(language="en",category="all",)
                display(joke)
                speak(joke)

            elif (' news ' in query)or (' headlines ' in query): #tells top 10 headlines (refreshes every 15 minutes)
                newsapi = NewsApiClient(api_key='0b923f88ad8043678cbcc84808217b70')
                data = newsapi.get_top_headlines(language='en',country='in')
                headlines=data['articles']
                for i in range(5):
                    print(i+1,". ",f'{headlines[i]["title"]}')
                    display(headlines[i]["title"])
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
                    display("Setting a timer for: "+hour_time+" hours.")
                    speak("Setting a timer for: "+hour_time+" hours.")
                    hour=float(hour_time)
                    timer=hour*3600

                elif 'minute' in query:
                    query = query.replace("minutes", "")
                    query = query.replace("minute", "")
                    min_time = query
                    display("Setting a timer for: "+min_time+" minutes.")
                    speak("Setting a timer for: "+min_time+" minutes.")
                    min=float(min_time)
                    timer=min*60

                elif 'second' in query:
                    query = query.replace("seconds", "")
                    query = query.replace("second", "")
                    sec_time = query
                    display("Setting a timer for: "+sec_time+" seconds.")
                    speak("Setting a timer for: "+sec_time+" seconds.")
                    sec=float(sec_time)
                    timer=sec

                time.sleep(timer)
                frequency = 2000 #beep sound0
                duration = 100
                for i in range(0,10):
                    winsound.Beep(frequency,duration)
                display("Time's up")
                speak("Time's up")

            elif ((' take 'in query)or(' capture 'in query))and((' image 'in query)or(' photo 'in query)): #takes phto from camera
                cam_port = 0
                cam = cv2.VideoCapture(cam_port)
                # reading the input using the camera
                result, image = cam.read()
                # If image will detected without any error,show result
                if result:
                        # showing result, it take frame name and image
                        display("Capturing Image")
                        speak("Capturing Image")
                        cv2.imshow("Capture", image)
                        # saving image in local storage
                        date=datetime.datetime.now().strftime('%d-%m-%Y %I-%M %p')
                        img_name=str(date).replace(":","")+"-capture.png"
                        cv2.imwrite('C:\\Users\\USER\\Pictures\\Camera Roll\\'+img_name, image)
                        display("Image saved ")
                        speak("Image saved ")
                        cv2.waitKey(2000)
                        cv2.destroyWindow("Capture")
                        warnings.filterwarnings("ignore")
                # If captured image is corrupted, moving to else part
                else:
                    display("No image detected. Please! try again")
                    speak("No image detected. Please! try again") 
            
            elif ' reminder ' in query: #sets a reminder
                try:
                    speak("Sure,What shall I remind you about?")
                    print("What shall I remind you about?")
                    text = takeCommand()
                    speak("Sure,When shall I remind you?")
                    print("When shall I remind you")
                    #rem_time = takeCommand()
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
                except Exception as e:
                    display("Wrong Input")
                    speak("Wrong Input")

            elif (' exit ' in query) or (" bye " in query):
                display("Thank you! Have a good day")
                speak("Thank you! Have a good day")
                root.destroy()

            elif "e101" in query:
                mic_input()

            elif (' what ' in query)or(' calculate ' in query)or(' convert ' in query)or(' who ' in query)or (' weather '): #for weather, general questions, conversions and calculations
                question = query
                app_id = '7AQ863-V8KTL6QTVA'
                client = wolframalpha.Client(app_id)
                try:
                    res = client.query(question)
                    answer = next(res.results).text
                    display(answer)
                    speak(answer)
                except:    
                    display("Sorry I don't know that now")
                    speak("Sorry I don't know that now")

#Output Frame
frame=LabelFrame(root)#,bg='#444444'
frame.grid(row=0,column=0,columnspan=3,sticky=W+E+N+S)

#Input Frame
frame2=LabelFrame(root)#,bg='#444444'
frame2.grid(row=1,column=0,columnspan=3,sticky=W+E+N+S)

#Text Input Box 
text_inputbox=Entry(frame2,width=27,font=('Arial',15),borderwidth=2)
text_inputbox.grid(row=1,column=0,padx=5,ipady=13)

#Microphone button
mic_img=ImageTk.PhotoImage(Image.open('icon_microphone.ico').resize((50,50)))
mic_button=Button(frame2,image=mic_img,padx=10,pady=10,borderwidth=2,command=mic_input)
mic_button.grid(row=1,column=1,padx=2,pady=2)

#User: label
l1=Label(frame,text='User :',font=('Arial', 13),anchor=N+E).grid(row=0,column=0,padx=2,pady=2,sticky=W+E+N+S)

#user input display label
l2=Label(frame,text='',font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN).grid(row=0,column=1,padx=2,pady=2,sticky=N+SW+E)

#Assistant name display label    
l3=Label(frame,text=Assistant_name+' :',font=('Arial', 13),anchor=N+E).grid(row=1,column=0,padx=2,ipadx=14,pady=2,sticky=W+E+N+S)

#Assistant output display label
l4=Label(frame,text='',font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN).grid(row=1,column=1,padx=2,pady=2,sticky=W+E,ipady=137,ipadx=167)

#Settings Window
def settings():
    top=Toplevel()
    top.title('Settings')
    top.geometry("340x200")
    top.iconbitmap("icon_settings.ico")

    #Settings to be changed    
    def changes(Assistant_name):
        #1. Changng Assistant name
        file=open("Assistant_name", "w")
        file.write(Assistant_name)
        file.close()
        
        if click.get()=='Male':
            VA_value='0'
        else:
            VA_value='1'
        VA_voice_file = open("Assistant_voice",'w')
        VA_voice_file.write(VA_value)
        VA_voice_file.close()

        if click2.get()=='Auto':
            VA_value2='0'
        else:
            VA_value2='1'
        VA_voice_file2 = open("Assistant_mode",'w')
        VA_voice_file2.write(VA_value2)
        VA_voice_file2.close()

        top.destroy()

        root.destroy()

    #Top Settings Label            
    label1=Label(top,text='--------------SETTINGS--------------',font=('Arial', 15, 'bold')).grid(row=0,column=0,columnspan=2)

    # 1. VA name setting label
    label2=Label(top,text='Voice Assistant Name :',font=('Arial', 13, 'bold')).grid(row=1,column=0,padx=2,pady=2)
    text_inputbox1=Entry(top,width=15,font=('Arial',13),justify='center')
    text_inputbox1.grid(row=1,column=1,padx=2,pady=2,ipady=3)
    name_file = open("Assistant_name",'r')
    Assistant_name = name_file.read()
    text_inputbox1.insert(0,Assistant_name)    
    name_file.close()    

    # 2. VA voice setting label
    label3=Label(top,text='Voice Assistant Voice :',font=('Arial', 13, 'bold')).grid(row=2,column=0,padx=2,pady=2)
   
    voice_list=["Male","Female"]
    click=StringVar()

    VA_voice_file = open("Assistant_voice",'r')
    value = VA_voice_file.read()
    VA_voice_file.close()
    
    click.set(voice_list[int(value)])

    #creating a drop down box
    drop=OptionMenu(top,click,*voice_list).grid(row=2,column=1,padx=2,pady=2,sticky=W+E)

    # 3. VA name setting label
    label4=Label(top,text='Voice mode :',font=('Arial', 13, 'bold')).grid(row=4,column=0,padx=2,pady=2)

    voice_list2=["Auto","Click"]
    click2=StringVar()

    VA_voice_file2 = open("Assistant_mode",'r')
    value2 = VA_voice_file2.read()
    VA_voice_file2.close()
    
    click2.set(voice_list2[int(value2)])

    #creating a drop down box
    drop2=OptionMenu(top,click2,*voice_list2).grid(row=4,column=1,padx=2,pady=2,sticky=W+E)
    
    # 4. VA name setting label
    label5=Label(top,text='*Restart the program to apply changes*',font=('Arial', 13, 'bold')).grid(row=6,column=0,padx=2,pady=2,columnspan=2)
    
    # 5. VA setting label
    #label5=Label(top,text='Settings 5 :',font=('Arial', 13, 'bold')).grid(row=6,column=0,padx=2,pady=2)
    
    # ok button
    b1=Button(top,text='OK',padx=10,pady=5,command=lambda: changes(text_inputbox1.get())).grid(row=7,column=0,columnspan=2)

#Settings button
settings_img=ImageTk.PhotoImage(Image.open('icon_settings.ico').resize((50,50),Image.ANTIALIAS))
settings_button=Button(frame2,image=settings_img,padx=10,pady=10,borderwidth=2,command=settings)
settings_button.grid(row=1,column=2,padx=2,pady=2)

keyboard.add_hotkey("enter",lambda: input())
keyboard.add_hotkey("F10",lambda: mic_input())

wishme()

def display(disp_text):
    l4=Label(frame,text=disp_text,font=('Arial', 13),anchor=N+W,bg="White",wraplength=340,borderwidth=1,relief=SUNKEN,justify='left')
    l4.grid(row=1,column=1,padx=2,pady=2,sticky=N+W+E+S)

root.mainloop()