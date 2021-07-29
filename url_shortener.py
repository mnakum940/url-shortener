from tkinter import *
import pyshorteners as ps
import pyperclip
from PIL import Image, ImageTk

root = Tk()
root.geometry("633x333")
root.title("URL Shortener")
root.resizable(False, False)

photo = Image.open("back.jpg")
photo = photo.resize((633,333))
img = ImageTk.PhotoImage(photo)

back = Label( image=img).place(x=0,y=0)


s = StringVar(root)
r = StringVar(root)


def shorten():
    n = str(s.get())
    k = ps.Shortener()
    m = k.tinyurl.short(n)
    global r
    r.set(str(m))


def copy_to_clipboard():
    pyperclip.copy(r.get())

title = Label(root, text="Url Shortener", font=("Comic Sans MS",20,"bold"), pady=20).grid(row=0,column =1)
label1 = Label(root, text="Enter the URL: ",pady=10)
text1 = Entry(root, textvariable=s, width=70, relief=SUNKEN)
button1 = Button(root, text="Shorten", command=shorten)
label2 = Label(root, text="Shortened URL: ", pady=10)
text2 = Entry(root, textvariable=r, width=40)
button2 = Button(root, text="Copy", command=copy_to_clipboard)
button3 = Button(root, text="Quit", command=root.destroy,fg="red")

label1.grid(row=1, column=0, sticky=W)
text1.grid(row=1, column=1)
button1.grid(row=2, column=1) # sticky=N + S + E + W
label2.grid(row=3, column=0, sticky=W)
text2.grid(row=3, column=1)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)

root.mainloop()