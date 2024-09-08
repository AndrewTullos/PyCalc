import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme='yaru')
root.title("Calc")
style = ttk.Style(root)
style.theme_use('clam')

expression = ""


# Create functions
def add(value):
   global expression
   expression += value
   label_result.config(text=expression)

def clear():
   global expression
   expression = ""
   label_result.config(text=expression)

def calculate():
   global expression
   result = " "
   if expression != "":
      try:
         result = eval(expression)
      except:
         result = "ERROR"
         expression = ""
   label_result.config(text=result)


# Configure grid weights for responsiveness
for i in range(6):  # Number of rows in the layout
   root.grid_rowconfigure(i, weight=1)
for j in range(4):  # Number of columns in the layout
   root.grid_columnconfigure(j, weight=1)

# Create GUI
label_result = tkinter.Label(root, text="", anchor='e', font=("Arial", 24), bg="#020122", fg="#FF6542", padx=20, pady=20)
label_result.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define button properties for consistent styling
button_config = {
   'padx': 20, 'pady': 20, 'font': ('Arial', 24), 'bg': '#0C0A3E', 'fg': '#FF6542'
}

button_clear = tkinter.Button(root, text="AC", command=lambda: clear(), **button_config)
button_clear.grid(row=1, column=0, sticky="nsew")

button_negative = tkinter.Button(root, text="+/-", command=lambda: add('-'), **button_config)
button_negative.grid(row=1, column=1, sticky="nsew")

button_percent = tkinter.Button(root, text="%", command=lambda: add('%'), **button_config)
button_percent.grid(row=1, column=2, sticky="nsew")

button_divide = tkinter.Button(root, text="/", command=lambda: add("/"), **button_config)
button_divide.grid(row=1, column=3, sticky="nsew")

# Row 2
button_7 = tkinter.Button(root, text="7", command=lambda: add("7"), **button_config)
button_7.grid(row=2, column=0, sticky="nsew")

button_8 = tkinter.Button(root, text="8", command=lambda: add("8"), **button_config)
button_8.grid(row=2, column=1, sticky="nsew")

button_9 = tkinter.Button(root, text="9", command=lambda: add("9"), **button_config)
button_9.grid(row=2, column=2, sticky="nsew")

button_multiply = tkinter.Button(root, text="*", command=lambda: add("*"), **button_config)
button_multiply.grid(row=2, column=3, sticky="nsew")

# Row 3
button_4 = tkinter.Button(root, text="4", command=lambda: add("4"), **button_config)
button_4.grid(row=3, column=0, sticky="nsew")

button_5 = tkinter.Button(root, text="5", command=lambda: add("5"), **button_config)
button_5.grid(row=3, column=1, sticky="nsew")

button_6 = tkinter.Button(root, text="6", command=lambda: add("6"), **button_config)
button_6.grid(row=3, column=2, sticky="nsew")

button_minus = tkinter.Button(root, text="-", command=lambda: add("-"), **button_config)
button_minus.grid(row=3, column=3, sticky="nsew")

# Row 4
button_1 = tkinter.Button(root, text="1", command=lambda: add("1"), **button_config)
button_1.grid(row=4, column=0, sticky="nsew")

button_2 = tkinter.Button(root, text="2", command=lambda: add("2"), **button_config)
button_2.grid(row=4, column=1, sticky="nsew")

button_3 = tkinter.Button(root, text="3", command=lambda: add("3"), **button_config)
button_3.grid(row=4, column=2, sticky="nsew")

button_add = tkinter.Button(root, text="+", command=lambda: add("+"), **button_config)
button_add.grid(row=4, column=3, sticky="nsew")

# Row 5
button_0 = tkinter.Button(root, text="0", command=lambda: add("0"), **button_config)
button_0.grid(row=5, column=0, columnspan=2, sticky="nsew")

button_dot = tkinter.Button(root, text=".", command=lambda: add("."), **button_config)
button_dot.grid(row=5, column=2, sticky="nsew")

button_equal = tkinter.Button(root, text="=", command=lambda: calculate(), **button_config)
button_equal.grid(row=5, column=3, sticky="nsew")

root.mainloop()
