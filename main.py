# Author: SiriusLatte
# Version: 1.0.0
# Web scrapper for wiki articles which is incredibly stupid and overcomplicated for nothing using custom made
# GUI elements using customtkinter (modern GUI looking) for no reason at all!


# Imports
import customtkinter as ctk
import tkinter as tk

import webbrowser as web
import requests as req
import bs4 as bs  # I didn't like the 4 being there, ok?


# Functions
def createdisplay(obj):
    displayframe = tk.Frame(obj.window, bg='#ebebeb', height=60)
    displayframe.pack(expand=True, fill='both')

    titlelabel = tk.Label(
        displayframe,
        text="",
        font=('Arial', 20, 'bold'),
        fg='#575757',
        bg='#ebebeb'
    )
    titlelabel.place(x=200, y=60, anchor=tk.CENTER)

    return titlelabel


def createbuttons(obj, nextfunc, readfunc):
    buttonsframe = tk.Frame(obj.window, bg='#f5f5f5')
    buttonsframe.pack(expand=True, fill='both')

    nextbutton = ctk.CTkButton(
        master=buttonsframe,
        corner_radius=100,
        command=nextfunc,
        text='Next article',
        text_font=('Arial', 12, 'bold'),
        fg_color='#dedede',
        text_color='#575757'
    )
    nextbutton.place(relx=.6, rely=.3)

    read = ctk.CTkButton(
        master=buttonsframe,
        corner_radius=100,
        command=readfunc,
        text='Read article',
        text_font=('Arial', 12, 'bold'),
        fg_color='#dedede',
        text_color='#575757'
    )
    read.place(relx=.1, rely=.3)


# Class
class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x200')
        self.window.resizable(width=False, height=False)
        self.window.title('Wikipedia article reader')
        ctk.set_appearance_mode("Dark")  # Optional

        self.title = ""

        self.label = createdisplay(self)
        createbuttons(self, nextfunc=self.nextarticle, readfunc=self.readarticle)

    def nextarticle(self):
        url = req.get('https://en.wikipedia.org/wiki/Special:Random')
        soup = bs.BeautifulSoup(url.content, 'html.parser')
        titletodisplay = soup.find(class_='firstHeading').text

        self.label.configure(text=titletodisplay)
        self.title = titletodisplay

    def readarticle(self):
        web.open("https://en.wikipedia.org/wiki/%s" % self.title)

    def runapp(self):
        self.window.mainloop()


if __name__ == "__main__":
    Application().runapp()
