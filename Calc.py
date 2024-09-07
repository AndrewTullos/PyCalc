import tkinter

root = tkinter.Tk()
root.title("Calc")

# Create functions
def add(value):
   print(value)

def clear():
   pass

def calculate():
   pass


# Create GUI 
label_result = tkinter.Label(root, text="99")
label_result.grid(row=0, column=0, columnspan=4)

button_clear = tkinter.Button(root, text="AC", command=lambda: clear())
button_clear.grid(row=1, column=0)

button_negative = tkinter.Button(root, text="+/-", command=lambda: add)
button_negative.grid(row=1, column=1)

button_percent = tkinter.Button(root, text="%", command=lambda: add)
button_percent.grid(row=1, column=2)

button_divide = tkinter.Button(root, text="/", command=lambda: add("/"))
button_divide.grid(row=1, column=3)

# # Row 2
button_7 = tkinter.Button(root, text="7", command=lambda: add("7"))
button_7.grid(row=2, column=0)

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"))
button_8.grid(row=2, column=1)

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"))
button_9.grid(row=2, column=2)

button_multiply = tkinter.Button(root, text="X", command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

# Row 3
button_4 = tkinter.Button(root, text="4", command=lambda: add("4"))
button_4.grid(row=3, column=0)

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"))
button_5.grid(row=3, column=1)

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"))
button_6.grid(row=3, column=2)

button_minus = tkinter.Button(root, text="-", command=lambda: add("-"))
button_minus.grid(row=3, column=3)

# Row 4
button_1 = tkinter.Button(root, text="1", command=lambda: add("1"))
button_1.grid(row=4, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"))
button_2.grid(row=4, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"))
button_3.grid(row=4, column=2)

button_add = tkinter.Button(root, text="+", command=lambda: add("+"))
button_add.grid(row=4, column=3)

# Row 5
button_0 = tkinter.Button(root, text="0", width=8, command=lambda: add("0"))
button_0.grid(row=5, column=0, columnspan=2)

button_dot = tkinter.Button(root, text=".", command=lambda: add("."))
button_dot.grid(row=5, column=2)

button_equal = tkinter.Button(root, text="=", command=lambda: calculate())
button_equal.grid(row=5, column=3)

root.mainloop()