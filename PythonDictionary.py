

import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *
from PyDictionary import PyDictionary


def CreateWidgets():
    inputLabel = Label(root, text="Word: ", bg="skyblue4")
    inputLabel.grid(row=0, column=0, padx=10, pady=5)

    wordEntry = Entry(root, width=25, bg='snow3', textvariable=inputWord)
    wordEntry.grid(row=0, column=1, padx=10, pady=5)

    searchButton = Button(root, text="Search", command=findMeaning)
    searchButton.grid(row=0, column=2, padx=10, pady=5)

    resultsLabel = Label(root, text="Meaning: ", bg="skyblue4")
    resultsLabel.grid(row=1, column=0, padx=10, pady=5)

    root.meaningDetails = sb_text.ScrolledText(root, width=40, height=20, bg='snow3')
    root.meaningDetails.grid(row=2, column=0, rowspan=10, columnspan=3, padx=10, pady=5)
    
    root.meaningDetails.config(state=DISABLED, font = "Calibri 15", wrap="word")

# Defining the findMeaning() to get the meaning of user-entered word
def findMeaning():
    # Creating object of PyDictionary Class of PyDictionary Library
    dictionaryObject = PyDictionary()
    # Finding meaning of user-entered word using meaning() of dictionaryObject
    wordMeaning = dictionaryObject.meaning(inputWord.get())
    # Creating an empty string variable called meaningDetails
    meaningDetails = ""
    # Checking if "Noun" keyword is there in the meaning result
    if "Noun" in wordMeaning:
        # Concatenating the list of meanings in the meaningDetails variable
        meaningDetails += "Noun:\n- " + "\n- ".join(wordMeaning['Noun'])
    # Checking if "Verb" keyword is there in the meaning result
    if "Verb" in wordMeaning:
        # Concatenating the list of meanings in the meaningDetails variable
        meaningDetails += "\n\nVerb:\n- " + "\n- ".join(wordMeaning['Verb'])
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.meaningDetails.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.meaningDetails.delete('1.0', END)
    # Displaying user-entered word meaning details in the meaningDetails Widget
    root.meaningDetails.insert("end", meaningDetails)
    # Making Widget uneditable again after the displaying list of news from feed
    root.meaningDetails.config(state=DISABLED)

root = tk.Tk()


root.title("PythonDictionary")
root.geometry("442x460")
root.config(background="skyblue4")
root.resizable(False, False)

inputWord = StringVar()


CreateWidgets()

root.mainloop()
