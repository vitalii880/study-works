import tkinter as tk

# Создание окна
window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x400")
window.resizable(False, False)

# Поле для ввода
entry = tk.Entry(window, font=("Arial", 20), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Функция добавления символов
def add(symbol):
    entry.insert(tk.END, symbol)

# Функция очистки
def clear():
    entry.delete(0, tk.END)

# Функция удаления последнего символа
def delete():
    entry.delete(len(entry.get()) - 1, tk.END)

# Функция вычисления результата
def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, str(result))
    except ZeroDivisionError:
        clear()
        entry.insert(0, "Деление на 0!")
    except:
        clear()
        entry.insert(0, "Ошибка")

# Кнопки калькулятора
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Создание кнопок
for row in buttons:
    frame = tk.Frame(window)
    frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            command = calculate
        else:
            command = lambda x=button: add(x)

        tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=command
        ).pack(side="left", expand=True, fill="both")

# Дополнительные кнопки
frame = tk.Frame(window)
frame.pack(expand=True, fill="both")

tk.Button(
    frame, text="C", font=("Arial", 16),
    command=clear
).pack(side="left", expand=True, fill="both")

tk.Button(
    frame, text="←", font=("Arial", 16),
    command=delete
).pack(side="left", expand=True, fill="both")

# Запуск программы
window.mainloop()