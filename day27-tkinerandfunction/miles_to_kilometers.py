from tkinter import *
FONT = ("Arial", 24)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

def convert_miles_to_km():
  miles = float(input.get())
  km = round(miles * 1.609,2)
  km_calculate_label.config(text=f"{km}")


input = Entry(width=7)
input.insert(0, "0")
input.focus()
input.grid(column=1,row=0)

miles_label = Label(text="Miles", font = FONT)
miles_label.grid(column=2,row=0)

equal_to_label = Label(text="is equal to", font = FONT)
equal_to_label.config(padx=40)
equal_to_label.grid(column=0,row=1)

km_calculate_label = Label(text="0", font = FONT)
km_calculate_label.grid(column=1,row=1)

km_label = Label(text="Km", font = FONT)
km_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", font=FONT, command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()