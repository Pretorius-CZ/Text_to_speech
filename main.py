from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk, font
import tkinter as tk


root = Tk()
root.title("Text na řeč")
root.geometry("400x400")
root.resizable (False, False)
root.iconbitmap("icon.ico")

#Fonty
custom_font_middle = font.Font(family="Helvetica", size=12)
custom_font_big = font.Font(family="Helvetica", size=16)


#Fuknce
def translate(entry, language, audio_filename):
    try:
        text_to_audio = entry
        output = gTTS(text=text_to_audio, lang=language, slow=False)
        output.save(audio_filename + ".mp3")
        os.system(f"start {audio_filename}.mp3")
    except Exception as e:
        print (f"Chyba: {e}")

#Nadpis
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

#Textová sekce
input_label = Label (text="Zadejte text pro převod", font=custom_font_middle)
input_label.grid (row=5, column=0)

input_entry = Text(root, height=10, width=27)
input_entry.grid (row=5, column=1)

empty_label = Label(text=" ")
empty_label.grid(row=6, column=0)

#Audio filename sekce
audio_label = Label (text="Název souboru (MP3): ", font=custom_font_middle)
audio_label.grid(row=7, column=0)

audio_entry = Entry(width = 36)
audio_entry.grid(row=7, column=1)



#Button na převod
button = Button(text="Přečti", font=custom_font_big, command=lambda:translate(input_entry.get("1.0", tk.END).strip(), lang_drop_down.get(), audio_entry.get()))
button.grid(row=9, column=0, columnspan=2, pady=10)



root.mainloop()


