import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="Text", font=("Arial", 24, "bold") )
my_label.grid(column=0, row=0)

def button_clicked():
    print("I got clicked!")
    new_text = my_input.get()
    my_label.config(text = new_text)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Another Button
button_2 = tkinter.Button(text="Hello World")
button_2.grid(column=2, row=0)

#Entry Component - Basically Input
my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)

window.mainloop()