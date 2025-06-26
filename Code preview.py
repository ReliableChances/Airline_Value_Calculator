from tkinter import *
from tkcalendar import Calendar

window1 = Tk()
window1.title("Airline Value Calc")
window1.geometry('1000x500')
window1.resizable(0,0)

dates = []

def calc():
    ()
input_frame = Frame(window1)
input_frame.grid(row=0, column=0, sticky="w", padx=20, pady=20)

button = Button(window1, text="Calculate", font=("Arial", 15), command=calc)
button.grid(row=1, column=0, columnspan=1, pady=2)
# Destination

dates_view = Label(input_frame, text="Travel Dates:", font=("Arial", 25))
dates_view.grid(column=0, row=3, columnspan=2, sticky="w", pady=5)

Label(input_frame, text="Origin:", font=("Arial", 25)).grid(column=0, row=0, sticky="w", pady=1)
Origin = Entry(input_frame, width=20)
Origin.grid(column=1, row=0, pady=1)

Label(input_frame, text="Destination:", font=("Arial", 25)).grid(column=0, row=5, sticky="w", pady=1)
Destination = Entry(input_frame, width=20)
Destination.grid(column=1, row=5, pady=1)


Label(input_frame, text="Miles Available:", font=("Arial", 25)).grid(column=0, row=2, sticky="w", pady=5)
mile_num = Entry(input_frame, width=20)
mile_num.grid(column=1, row=2, pady=5)


calendar_frame = Frame(window1)
calendar_frame.grid(row=0, column=1, sticky="n", padx=40, pady=20)

calendar = Calendar(calendar_frame, selectmode='day', year=2025, month=6, day=25)
calendar.grid(row=0, column=0, columnspan=2, pady=10)


label = Label(calendar_frame, text="Selected\ndate:", font=("Arial", 20))
label.grid(row=1, column=0, columnspan=2, pady=10)


def get_date():
    selected_date = calendar.get_date()
    if selected_date not in dates:
        if len(dates) < 2:
            dates.append(selected_date)
        elif len(dates) == 2:
            dates.append('\n' + selected_date + '\n')
        else:
            dates.append(selected_date)
    label.config(text=f"{selected_date}")

    dates_view.configure(text=f"Travel Dates: {', '.join(dates)}")


button = Button(calendar_frame, text="Add Date", font=("Arial", 15), command=get_date)
button.grid(row=2, column=0, columnspan=2, pady=5)



extra_frame = Frame(window1)
extra_frame.grid(row=1, column=0, columnspan=2, sticky="w", padx=20, pady=10)




window1.grid_columnconfigure(0, weight=1, minsize=400)
window1.grid_columnconfigure(1, weight=0)

# Run the app
window1.mainloop()
