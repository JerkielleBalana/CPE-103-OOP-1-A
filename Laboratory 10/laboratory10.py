import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title('Jerkielle Balana')
window.geometry('500x500')

month_var = tk.StringVar()
day_var = tk.StringVar()
year_var = tk.StringVar()

def show_birth_info():
    selected_month = month_var.get()
    selected_day = day_var.get()
    selected_year = year_var.get()

    showinfo(title_='Birth Info', message=f'Jerkielle Balana were born on {selected_month} {selected_day}, {selected_year}.')

def choice(event):
    selected_month = event.widget.get()
    print('Your birth month:', selected_month)

ttk.Label(window, text='Choose your birth month:', background='green', foreground='white', font=('Times New Roman', 15)).grid(row=0, column=1, pady=10)

month = ttk.Combobox(window, width=27, textvariable=month_var)
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
month.grid(column=1, row=1)
month.bind('<<ComboboxSelected>>', choice)

ttk.Label(window, text='Choose your birth day:', background = 'green', foreground = 'white',  font=('Times New Roman', 15)).grid(row=2, column=1, pady=10)

day = ttk.Combobox(window, width=5, textvariable=day_var)
day['values'] = [str(i).zfill(2) for i in range(1, 32)]  # Days 01 to 31
day.grid(row=3, column=1)

ttk.Label(window, text='Choose your birth year:', background = 'green', foreground= 'white', font=('Times New Roman', 15)).grid(row=5, column=1, pady=10)

year = ttk.Combobox(window, width=10, textvariable=year_var)
year['values'] = [str(i) for i in range(1900, 2026)]  # Years 1900 to 2025
year.grid(row=6, column=1)

ttk.Button(window, text="Show Birth Info", command=show_birth_info).grid(row=7, column=1, pady=20)

window.mainloop()