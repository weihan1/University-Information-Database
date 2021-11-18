import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
import winning_project


def answerToQuestion(name: str, char: str) -> None:
    output: str = winning_project.final_return(name, char)
    answer.config(text=output)


root = Tk()
root.title("interU Search Engine")
root.geometry("1200x620")
# wordVariable.config(width, font = ("fontName",fontsize))

# load image
uoftCampus = ImageTk.PhotoImage(Image.open("UofT.png"))  # image is 1200x630
backGround = Label(root, image=uoftCampus)
backGround.place(x=0, y=0, relwidth=1, relheight=1)
logo = Image.open("InterUlogo.png")
logo = logo.resize((150, 150), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
interUlogo = Label(root, image=logo)
interUlogo.place(x=0, y=0)

# Show Answer
answerFrame = Frame(root, borderwidth=5, highlightbackground="black",
                    highlightthickness=1, bg="green")
answer = Label(answerFrame, text="What would you like to know?", pady=2.5,
               padx=1.5, wraplength=800)
answer.grid()
answerFrame.place(relx=0.5, rely=0.6, anchor=CENTER)
answer.config(font=("Times New Roman", 12))

# GUI design
GUIFrame = Frame(root, borderwidth=5, highlightbackground="black",
                 highlightthickness=1)
name = StringVar(GUIFrame)
questionForInput1 = Label(GUIFrame, text="Enter University Name:")
questionForInput2 = Label(GUIFrame, text="Select one information:")
userInput = Entry(GUIFrame, width=30, textvariable=name)
userChoices = ["[Select Choice]", "Website", "Number of students",
               "World Ranking", "Province", "Fact"]
selection = StringVar(GUIFrame)
selection.set(userChoices[0])
userSelect = OptionMenu(GUIFrame, selection,
                        *userChoices[1:])  # selection.get to return the string
searchButton = Button(GUIFrame, text="Search",
                      command=lambda: answerToQuestion(name.get(),
                                                       selection.get()))

questionForInput1.grid(row=0, column=0, sticky=E)
questionForInput2.grid(row=1, column=0, sticky=E)
userInput.grid(row=0, column=1)
searchButton.grid(row=1, column=2)
userSelect.grid(row=1, column=1)
GUIFrame.place(relx=0.5, rely=0.3, anchor=CENTER)

# login information
loginFrame = Frame(root, borderwidth=5, highlightbackground="black",
                   highlightthickness=1)

username = Label(loginFrame, text="Username:")
password = Label(loginFrame, text="Password:")
keepMe = Checkbutton(loginFrame, text="Keep me logged in!")
login = Button(loginFrame, text="login")
userInputName = Entry(loginFrame)
userPass = Entry(loginFrame)

username.grid(row=0, sticky=E)
password.grid(row=1, sticky=E)
userInputName.grid(row=0, column=1)
userPass.grid(row=1, column=1)
keepMe.grid(columnspan=2)
login.grid(columnspan=2)
loginFrame.place(relx=1, anchor="ne")

root.mainloop()
