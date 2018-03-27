import speech_recognition as sr
import webb
from tkinter import *

window=Tk()
window.title('Speech Recognition')
window.geometry('600x400')
window.configure(bg='gold')

def Window():
    # Recognizer method
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        print('Done')

    try:
        text = r.recognize_google(audio)
        print("You said:\n" + text)
        fp = open("TextOutpuFile.txt", "w")
        fp.write(text)
    except Exception as e:
        print(e)

entry_label = Label(window, text="Press the Button to start recording!!!", font=('arial', 12))
entry_label.pack()
entry_label.place(x=230,y=70)

B1=Button(window,text="Click to speak",font=('arial',13,'bold'),command=Window)
B1.pack()
B1.place(x=260,y=140)

window.mainloop()