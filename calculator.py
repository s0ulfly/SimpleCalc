import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = float(entry.get())
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = first_number
    entry.delete(0, tk.END)

def button_subtract():
    first_number = float(entry.get())
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = first_number
    entry.delete(0, tk.END)

def button_multiply():
    first_number = float(entry.get())
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = first_number
    entry.delete(0, tk.END)

def button_divide():
    first_number = float(entry.get())
    global f_num
    global math_operation
    math_operation = "division"
    f_num = first_number
    entry.delete(0, tk.END)

def button_equal(event=None):  # Modified function to accept event parameter
    second_number = float(entry.get())
    entry.delete(0, tk.END)
    if math_operation == "addition":
        entry.insert(tk.END, f_num + second_number)
    elif math_operation == "subtraction":
        entry.insert(tk.END, f_num - second_number)
    elif math_operation == "multiplication":
        entry.insert(tk.END, f_num * second_number)
    elif math_operation == "division":
        if second_number != 0:
            entry.insert(tk.END, f_num / second_number)
        else:
            entry.insert(tk.END, "Error: Cannot divide by zero")

# Create the GUI window
window = tk.Tk()
window.title("Calculator")

# Create entry field
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons (0 to 9)
button_1 = tk.Button(window, text="1", padx=30, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=30, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=30, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=30, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=30, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=30, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=30, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=30, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=30, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=30, pady=20, command=lambda: button_click(0))

# Create command buttons
button_add = tk.Button(window, text="+", padx=30, pady=20, command=button_add)
button_subtract = tk.Button(window, text="-", padx=30, pady=20, command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=30, pady=20, command=button_multiply)
button_divide = tk.Button(window, text="/", padx=30, pady=20, command=button_divide)
button_equal = tk.Button(window, text="=", padx=30, pady=20, command=button_equal)
button_clear = tk.Button(window, text="C", padx=30, pady=20, command=button_clear)

# Grid placement for number buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)

# Grid placement for command buttons
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)



# Start the GUI event loop
window.mainloop()
