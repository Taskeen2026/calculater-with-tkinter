
import tkinter as tk

window = tk.Tk()
window.title("calculator")
window.geometry("300x400")
window.config(bg="#2D3748")

tk.Label(window, text="Calculator", font=("Arial", 16, "bold"), bg="#e47878").pack(pady=10)

tk.Label(window, text="1 wala number:", bg="#f0f0f0").pack()
entry1 = tk.Entry(window, width=25)
entry1.pack(pady=5)

tk.Label(window, text="2 wala number:", bg="#f0f0f0").pack()
entry2 = tk.Entry(window, width=25)
entry2.pack(pady=5)

result_label = tk.Label(window, text="Result:", bg="#f0f0f0")
result_label.pack(pady=10)

def add():
    result = float(entry1.get()) + float(entry2.get())
    result_label.config(text="Result: " + str(result))

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    result_label.config(text="Result: " + str(result))

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    result_label.config(text="Result: " + str(result))  

def divide():
    result = float(entry1.get()) / float(entry2.get())
    result_label.config(text="Result: " + str(result))

tk.Button(window, text="+ Add", width=10, command=add).pack(pady=2)
tk.Button(window, text="- Subtract", width=10, command=subtract).pack(pady=2)
tk.Button(window, text="* Multiply", width=10, command=multiply).pack(pady=2)
tk.Button(window, text="/ Divide", width=10, command=divide).pack(pady=2)

window.mainloop()

                                                                      