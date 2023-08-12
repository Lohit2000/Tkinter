import tkinter
from tkinter import *
from tkinter.ttk import *
root = tkinter.Tk()

#root.geometry("1000x1050")  #width x height

#root.configure(bg="#cb92de") #background color

def linux():
    #linux commands
    import subprocess
    cmd = input("Enter your command: ")
    x = subprocess.getoutput(cmd)
    print(x)
    
def whatsapp():
    #pip install pywhatkit
    import pywhatkit as pw
    phone = input("enter phn num: ")
    mesg = input("enter mesg")
    pw.sendwhatmsg_instantly(phone,mesg)
    
def email1():
    import smtplib # simple mail transfer protocol

    server = smtplib.SMTP('smtp.gmail.com',587) 

    server.starttls()  #tls = transport layer security

    # input all the details
    sender_email = input("enter sender email : ")
    password = input("enter the password : ")

    reciever_email = input("enter the reciever email : ")
    message = input("enter the message to be sent : ")

    #login
    server.login(sender_email , password)

    server.sendmail(sender_email, reciever_email , message)

    print("mail sent successfully")    

def speech():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic:
        print("Say Anything!!!!!!!!")
        audio = r.listen(mic)
    print(r.recognize_google(audio))
    
def search():
    from googlesearch import search
    q = input("What You Want to Search: ")
    for j in search(q, tld="com", num=10, stop=10, pause=2):
        print(j)

def photo():
    import cv2
    cam = cv2.VideoCapture(0)
    status, photo = cam.read()
    cv2.imshow("photo",photo)
    cv2.waitKey()
    cv2.destroyAllWindows()
    if cv2.waitKey()==13:
        cam.release()
        
def video():
    import cv2
    cam = cv2.VideoCapture(0)
    while True:
        status, photo = cam.read()
        cv2.imshow("Video",photo)
        if cv2.waitKey(100) == 13:
            break
    cv2.destroyAllWindows()
    cam.release()
    
def grey_video():
    import cv2
    cam = cv2.VideoCapture(0)
    while True:
        status, photo = cam.read()
        grey_pht = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Video",grey_pht)
        if cv2.waitKey(100) == 13:
            break
    cv2.destroyAllWindows()
    cam.release()
    

heading = tkinter.Label(root,text = "!!!!!!!! WELCOME TO PYTHON MENU !!!!!!!!",fg="white",bg = "#911769",height=4, width=70,
               font= ("comicsansms",10,"bold"), relief=SUNKEN)
heading.grid(row=0,pady=20,column=0,columnspan=2)


b1 = tkinter.Button(root, text = "Linux Commands",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, 
                    width=40,height=1,command=linux)
b1.grid(row=1,pady=20,column=0,padx=40)


b2 = tkinter.Button(root, text = "WhatsApp Message",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=whatsapp)
b2.grid(row=2,pady=20)


b3 = tkinter.Button(root, text = "Email Message",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=email1)
b3.grid(row=3,pady=20)

b4 = tkinter.Button(root, text = "Speech To Text",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=speech)
b4.grid(row=4,pady=20)

b5 = tkinter.Button(root, text = "Google Search",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=search)
b5.grid(row=4,pady=20,column=1)

b6 = tkinter.Button(root, text = "Click Photo",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=photo)
b6.grid(row=3,pady=20,column=1)

b7 = tkinter.Button(root, text = "Video Streaming",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=video)
b7.grid(row=2,pady=20,column=1)

b8 = tkinter.Button(root, text = "Black & White Video Streaming",font=("comicsansms",12,"bold"),bg="#cb92de", padx=8,pady=10, width=40,height=1,
                   command=grey_video)
b8.grid(row=1,pady=20,column=1,padx=40)

root.mainloop()
