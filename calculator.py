import tkinter as tk


# Function to perform calculations
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except ZeroDivisionError:
        data.set("Error:Division by zero")

    except SyntaxError:
        data.set("Error: Invalid expression")


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

# Entry widget for user input
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, command=lambda: entry.delete(0, tk.END)).grid(row=row_val,
                                                                                                       column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20,
                  command=lambda btn=button: entry.insert(tk.END, btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Label to display the result
result_label = tk.Label(window, text="", padx=20, pady=20)
result_label.grid(row=row_val, column=col_val, columnspan=4)

# Run the Tkinter main loop
window.mainloop()
