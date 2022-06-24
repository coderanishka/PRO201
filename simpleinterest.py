from tkinter import *
from unittest import result

window = Tk() 
window.title('SIMPLE INTEREST CALCULATOR')
window.geometry('400x500') 
window.configure(bg = 'purple')

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rateOfInterest_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    result_label.destroy()
    output_msg = Label(result_frame, text = 'Simple Interest is ' + str(i), bg = 'Pink', font = ('Calibri', 18), width = 42)
    output_msg.place(x = 20, y = 40)
    output_msg.pack()


heading_label = Label(window, text = 'Simple Interest Calculator', fg = 'black', bg = 'purple', font = ('Calibri', 20), bd = 5)
heading_label.place(x = 50, y = 20)

principal_label = Label(window, text = 'Principal: ', fg = 'black', bg = 'purple', font = ('Calibri', 15), bd = 1)
principal_label.place(x = 20, y = 90)

principal_entry = Entry(window, text = '', bd = 2, width = 22)
principal_entry.place(x = 110, y = 95)

rateOfInterest_label = Label(window, text = 'Rate of Interest: ', bg = 'purple', font = ('Calibri', 15))
rateOfInterest_label.place(x = 20, y = 140)

rateOfInterest_entry = Entry(window, text = '', bd = 2, width = 22)
rateOfInterest_entry.place(x = 170, y = 145)

time_label = Label(window, text = 'Time: ', bg = 'purple', font = ('Calibri', 15))
time_label.place(x = 20, y = 190)
time_entry = Entry(window, text = '', bd = 2)
time_entry.place(x = 80, y = 195)

result_frame = LabelFrame(window, text = 'Result', bg = 'Purple', font = ('Calibri', 15))
result_frame.pack(padx = 20, pady = 20)
result_frame.place(x = 20, y = 300)

result_label = Label(result_frame, text = '', bg = 'Purple', font = ('Calibri', 15))
result_label.place(x = 20, y = 20)
result_label.pack()

calculate_button = Button(window, text = 'Calculate', fg = 'black', bg = 'cyan', bd = 4, command = calculate_interest)
calculate_button.place(x = 20, y = 250)

window.mainloop()