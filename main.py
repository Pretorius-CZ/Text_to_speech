
from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk, font
import tkinter as tk


#Main window
root = Tk()
root.title("Text na řeč")
root.geometry("400x400")
root.resizable (False, False)
root.iconbitmap("icon.ico")

#Fonts
custom_font_middle = font.Font(family="Helvetica", size=12)
custom_font_big = font.Font(family="Helvetica", size=16)

#Header
main_label = Label (text="Konvertor z řeči na text", font=custom_font_big)
main_label.grid(row=0, column=0, columnspan=2, pady=10)

empty_label = Label(text=" ")
empty_label.grid(row=1, column=0)

#Language section
lang_label = Label (text="Vyberte jazyk výstupu: ", font=custom_font_middle)
lang_label.grid (row=2, column=0)

#Roletka
lang_drop_down = ttk.Combobox(state="readonly",
                              values=["cs", "en"],
                              width = 33)
lang_drop_down.grid (row=2, column=1)

empty_label = Label(text=" ")
empty_label.grid(row=4, column=0)

#Text section
input_label = Label (text="Zadejte text pro převod", font=custom_font_middle)
input_label.grid (row=5, column=0)

input_entry = Text(root, height=10, width=27)
input_entry.grid (row=5, column=1)

empty_label = Label(text=" ")
empty_label.grid(row=6, column=0)

#Audio filename section
audio_label = Label (text="Název souboru (MP3): ", font=custom_font_middle)
audio_label.grid(row=7, column=0)

audio_entry = Entry(width = 36)
audio_entry.grid(row=7, column=1)
