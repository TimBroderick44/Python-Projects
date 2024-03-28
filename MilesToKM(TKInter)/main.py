from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Button Function
def button_clicked():
    user_input = miles_input.get()
    converted = round((int(user_input) * 1.60934), 2)
    conversion_label.config(text=converted)


# Labels
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to", font=("Arial", 12))
equal_to_label.grid(row=1, column=0)

conversion_label = Label(text="0", font=("Arial", 12))
conversion_label.grid(row=1, column=1)

KM_label = Label(text="KM", font=("Arial", 12))
KM_label.grid(row=1, column=2)

# Entry

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

# Button

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
