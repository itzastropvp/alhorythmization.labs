import sys

import customtkinter as ctk
def exit_app():
    sys.exit()
window = ctk.CTk()
window.geometry("400x300")
window.resizable(False, False)
window.title("Моя вітальна картка")
text1 = ctk.CTkLabel(window, text = "Вітаю!", font = ("Arial", 18))
text1.place(x = 176, y = 110)
text2 = ctk.CTkLabel(window, text = "Бодюл Едуард", font = ("Arial", 18))
text2.place(x = 140, y = 130)
text3 = ctk.CTkLabel(window, text = "КН 1/1", font = ("Arial", 18))
text3.place(x = 175, y = 154)
button = ctk.CTkButton(window, text="x", font = ("Arial", 18), width = 40, height = 40, corner_radius=8, fg_color = "#D32F2F", hover_color = "#EF5350", command = exit_app)
button.place(x = 355, y = 2)
window.mainloop()