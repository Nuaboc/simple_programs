# Glossary Project

from tkinter import *


# Key down function

def click():
    """This will collect the text from the text entry box."""
    entered_text = text_entry.get()
    output.delete(0.0, END)
    try:
        definition = dictionary[entered_text]
    except:
        definition = "Sorry, that word is not in our dictionary. We will add it soon."
        output.insert(END, definition)


# MAIN...

window = Tk()
window.title("Computer Science Glossary")
window.configure(background='black')
# The next line of code prevent the user form change the window size, so it don't look weird.
# window.resizable(0, 0)

# image
photo1 = PhotoImage(file='men_train.gif')
Label(window, image=photo1, bg='black') .grid(row=0, column=0, sticky=E)

# Label
Label(window, text="Enter the word you would like  definition for:", bg='black', fg='white', font='none 12 bold')\
    .grid(row=1, column=0, sticky=W)

# Text entry box
text_entry = Entry(window, width=20, bg='white')
text_entry.grid(row=2, column=0, sticky=W)

# Summit button
Button(window, text="Submit", width=6, command=click) .grid(row=3, column=0, sticky=W)

# Label
Label(window, text='\nDefinition:', bg='black', fg='white', font='none 12 bold') .grid(row=4, column=0, sticky=W)

# Text box
output = Text(window, width=105, height=5, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

# The Dictionary
dictionary = {
    'algorithm': "Step by step instructions to complete a task. In simple words, like a recipe.",
    'bug': "Piece of code that cause a program to fail"
}
# Exit label
Label(window, text="Click to exit:", bg='black', fg='red', font="none 14 bold") .grid(row=6, column=0, sticky=E)


# Exit function

def close_window():
    """End the program."""
    exit()


# Exit button
Button(window, text="Exit", width=14, command=close_window) .grid(row=6, column=1, sticky=E)

# MAIN LOOP...

window.mainloop()
