import tkinter as tk

Calculation = ""

def add_to_calculation(symbol):
    global Calculation
    Calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, Calculation)

def evaluate_calculation():
    global Calculation
    try:
        result = str(eval(Calculation))  # Store the result of the evaluation
        Calculation = result  # Update Calculation with the result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except Exception as e:  # Catch any exception and print it for debugging
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global Calculation
    Calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Create buttons for numbers and operations
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3),
    ('0', 5, 2), ('+', 2, 4), ('-', 3, 4),
    ('*', 4, 4), ('/', 5, 4), ('(', 5, 1),
    (')', 5, 3), ('C', 6, 1, 2), ('=', 6, 3, 2)
]

for (text, row, col, *args) in buttons:
    if text == 'C':
        btn = tk.Button(root, text=text, command=clear_field, width=11, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=args[0] if args else 1)
    elif text == '=':
        btn = tk.Button(root, text=text, command=evaluate_calculation, width=11, font=("Arial", 14))
        btn.grid(row=row, column=col, columnspan=args[0] if args else 1)
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=("Arial", 14))
        btn.grid(row=row, column=col)

root.mainloop()