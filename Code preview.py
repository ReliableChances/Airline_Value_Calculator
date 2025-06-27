from tkinter import *
from tkcalendar import Calendar

window1 = Tk()
window1.title("Airline Value Calc")
window1.geometry('1000x500')
window1.resizable(0,0)



def calc():

    num_mile = int(miles.get())
    tax = float(taxes.get())
    price = float(cost.get())
    value_per_mile = ((price - ((tax/100)*price)))/num_mile
    end.configure(text=f"Value per mile: {round(value_per_mile, 4)}")

input_frame = Frame(window1)
input_frame.grid(row=0, column=0, sticky="w", padx=20, pady=20)

button = Button(window1, text="Calculate", font=("Arial", 40), command=calc)
button.grid(row=1, column=0, columnspan=1, pady=2)
# Destination

Label(input_frame, text="Taxes (in % taken):", font=("Arial", 25)).grid(column=0, row=0, sticky="w", pady=1)
taxes = Entry(input_frame, width=20, font=("Arial", 20))
taxes.grid(column=1, row=0, pady=1)

Label(input_frame, text="Miles needed:", font=("Arial", 25)).grid(column=0, row=4, sticky="w", pady=1)
miles = Entry(input_frame, width=20, font=("Arial", 20))
miles.grid(column=1, row=4, pady=1)


Label(input_frame, text="Cash price:", font=("Arial", 25)).grid(column=0, row=2, sticky="w", pady=5)
cost = Entry(input_frame, width=20, font=("Arial", 20))
cost.grid(column=1, row=2, pady=5)

end = Label(input_frame, text="Value per mile: ", font=("Arial", 25))
end.grid(column=0, row=5, sticky="w", pady=5)








window1.grid_columnconfigure(0, weight=1, minsize=400)
window1.grid_columnconfigure(1, weight=0)

# Run the app
window1.mainloop()
