from tkinter import *

#know about pack, place, and grid


# how to get button to work
def button_clicked():
  my_label.config(text = input.get())

window = Tk()
window.title("Buttons")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label
my_label = Label(text="I am a label", font=("Arial", 24,"bold"))

# how to edit inside (2 ways)
#my_label["text"] = "New Text"
my_label.config(text = "new Text")
my_label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New button", command=button_clicked)
button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()