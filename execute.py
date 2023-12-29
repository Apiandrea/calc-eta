import tkinter as tk
import datetime
from PIL import Image,ImageTk

window = tk.Tk()
window.geometry("360x620")
window.title(" Calcola Età ")
window.configure(background="white")

# INDICHIAMO CHE L'UTENTE NON PUO' RIDIMENSIONARE LA FINESTRA
window.resizable(False, False)

name = tk.Label(text = "Nome", font=("Helvetica", 16))
name.grid(column = 0, row = 1, pady=20, sticky="W")
#                                   /\       /\
#                                   |         |
#                                   |      LO STICKY SERVE PER ALLINEARE 
#                                   |      IN BASE ALLA ROSA DEI VENTI 
# IL PADDING QUI SULL'ASSE DELLE ASCISSE 
# (LA DISTANZA TRA GLI ALTRI COMPONENTI GRAFICI)

year = tk.Label(text = "Anno", font=("Helvetica", 16))
year.grid(column = 0, row = 2, sticky="W")

month = tk.Label(text = "Mese", font=("Helvetica", 16))
month.grid(column = 0, row = 3, sticky="W")

date = tk.Label(text = "Giorno", font=("Helvetica", 16))
date.grid(column = 0, row = 4, sticky="W")

nameEntry = tk.Entry()
nameEntry.grid(column = 1, row = 1)

yearEntry = tk.Entry()
yearEntry.grid(column = 1, row = 2)
monthEntry = tk.Entry()
monthEntry.grid(column = 1, row = 3)

dateEntry = tk.Entry()
dateEntry.grid(column = 1, row = 4)


# FUNCTION TO GET THE INPUT 
def getInput():
    name = nameEntry.get()
    try:
        monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
        textArea = tk.Text(master = window, height=3, width=35)
        textArea.grid(column = 1, row = 6)
        answer = " {monkey} hai {age} anni ".format(monkey = name, age = monkey.age())
        textArea.insert(tk.END, answer)
    except ValueError as e:
        print("Error: ", e)
        warning = " ERROR: {err}".format(err = e)
        textArea = tk.Text(master = window, height = 3, width = 35)
        textArea.grid(column = 1, row = 6)
        textArea.insert(tk.END, warning)

# FUNCTION TO CHANGE THE BACKGROUND COLOR
def switch():
    current_bg = window.cget("bg")
    if current_bg == "black":
        window.configure(bg="white")
    else:
        window.configure(bg="black")

# SETTING THE CALC BUTTON
button = tk.Button(window, text = "Calcola Età", command = getInput, bg = "red", font=("Helvetica", 16))
button.grid(column = 1, row = 5)

# SETTING THE SWITCH BUTTON
switch_bg = tk.Button(window, text = "Cambia Tema", command = switch, bg = "red", font=("Helvetica", 16))
switch_bg.grid(column = 1, row = 7)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

image = Image.open("logo.png")
image.thumbnail((300, 300))
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image = photo)
label_image.grid(column = 1, row = 0, sticky="S")
window.mainloop()


