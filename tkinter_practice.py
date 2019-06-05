# Glossary Project

from tkinter import *

# Key down function

# MAIN...

window = Tk()
window.title("Computer Science Glossary")
window.configure(background='teal')

# image
photo1 = PhotoImage(file='men_train.gif')
Label(window, image=photo1, bg='black') .grid(row=0, column=0, sticky=E)

# Label
Label(window, text="Enter the word you would like  definition for:", bg='black', fg='white', font='none 12 bold')\
    .grid(row=1, column=0, sticky=W)

# Text entry box

# Summit button

# Label

# Text box

# The Dictionary

# MAIN LOOP...

window.mainloop()
