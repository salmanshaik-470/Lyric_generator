# from PyLyrics import *
# print(PyLyrics.getLyrics("sid sriram","Emai Poyave"))

from tkinter import *
from lyrics_extractor import SongLyrics



def get_lyrics():
    extract_lyrics = SongLyrics("AIzaSyADb6D9eE6LKFxyzNpNtqygB88jrQIZgqY", "a8c760db89c37a5f8")


    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result.set(res)



master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name : ",bg="light grey").grid(row=0, sticky=W)

Label(master, text="Result :",bg="light grey").grid(row=3, sticky=W)

# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=result,bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creating a button using the widget
b = Button(master, text="Show",command=get_lyrics, bg="green")

b.grid(row=0, column=2, columnspan=2,rowspan=2, padx=5, pady=5, )
mainloop()
