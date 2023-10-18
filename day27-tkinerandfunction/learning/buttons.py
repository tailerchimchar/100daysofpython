from tkinter import *

# how to get button to work
def button_clicked():
  my_label.config(text = input.get())

window = Tk()
window.title("Buttons")
window.minsize(width=500, height=300)

#label
my_label = Label(text="I am a label", font=("Arial", 24,"bold"))

# how to edit inside (2 ways)
my_label["text"] = "New Text"
my_label.config(text = "new Text")
my_label.pack()

button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


window.mainloop()