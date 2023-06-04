from tkinter import *
from tkinter import messagebox
import pyshorteners
import pyperclip
import requests

bgcolor = 'light green'

def short_url():
    try:
        en_url_short.delete(0,END)
        long_url = en_url.get()
        type_tiny = pyshorteners.Shortener()
        short_url = type_tiny.tinyurl.short(long_url)
        en_url_short.insert(0,short_url)
        
    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet Error', 'Connect to internet')
    except:
        messagebox.showwarning('URL', 'Enter a link or URL')
    

def copy():
    pyperclip.copy(en_url_short.get())
    messagebox.showinfo('URL Copy', "Link/URL Copy successfully")

def clear():
    en_url_short.delete(0,END)
    en_url.delete(0,END)



root = Tk()
root.title("URL Shortener")
root.geometry('650x560+420+50')
root.resizable(0,0)
root.config(bg=bgcolor)

Label(root, text='URL Shortener', font=('OCR A Extended', 30, 'bold'), bg=bgcolor, fg='black').pack(pady=(10,10))

Label(root, text='Paste link/URL', font=('Times', 15), bg=bgcolor).pack(pady=(40,10))

en_url = Entry(root, font=('', 13), fg='blue')
en_url.place(x=80, y=140, width=500, height=28)

btn_short = Button(root, text='Submit', font=('', 15),relief=RAISED, command=short_url)
btn_short.place(x=260, y=190, width=130, height=40)

Label(root, text='Short link/URL', font=('Times', 15), bg=bgcolor).pack(pady=(130,10))

en_url_short = Entry(root, font=('', 13), fg='blue', justify=CENTER)
en_url_short.place(x=80, y=310, width=500, height=28)

btn_copy = Button(root, text='Copy', font=('', 15),relief=RAISED, command=copy)
btn_copy.place(x=260, y=360, width=130, height=40)

btn_clear = Button(root, text='Clear', font=('', 15),relief=RAISED, command=clear)
btn_clear.place(x=260, y=450, width=130, height=40)

root.mainloop()