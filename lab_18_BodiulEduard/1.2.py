import customtkinter as ctk

def convert():
    try:
        celsius = float(entry1.get())
        fahrenheit = (celsius * 1.8) + 32
        result_label.configure(text=f"{round(fahrenheit, 1)} °F", text_color="white")
    except ValueError:
        result_label.configure(text="Введите число!", text_color="#FF6666")

app = ctk.CTk()
app.title("Конвертер")
app.geometry("500x200")
app.resizable(False, False)
text1 = ctk.CTkLabel(app, text="°C", font=("Arial", 24))
text1.place(x=233, y=10)
entry1 = ctk.CTkEntry(app, width=100, height=35, font=("Arial", 18))
entry1.place(x=200, y=40)
button = ctk.CTkButton(app,width=160,height=40,text="Конвертувати",font=("Arial", 20),fg_color="#2E7D32",hover_color="#388E3C",command=convert)
button.place(x=168, y=85)
result_label = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
result_label.place(x=228, y=130)
app.mainloop()