import socket
from requests import get
import tkinter as tk
import tkinter.messagebox as mb
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get('http://api.ipify.org').text
#print(f'Хост: {hostname}')
#print(f'Локальный IP: {local_ip}')
#print(f'Публичный IP: {public_ip}')

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_info = tk.Button(self, text="Нажми сюда",
                             command=self.show_info)
        btn_warn = tk.Button(self, text="Предупреждение!",
                             command=self.show_warning)
        btn_error = tk.Button(self, text="?",
                              command=self.show_error)

        opts = {'padx': 40, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_info.pack(**opts)
        btn_warn.pack(**opts)
        btn_error.pack(**opts)

    def show_info(self):
        msg = ("№1 by Monalith")
        mb.showinfo("Твой IP", msg)

    def show_warning(self):
        msg = "Прошу, не нажимай на вопросительный знак"
        mb.showwarning("Предупреждение", msg)

    def show_error(self):
        msg = (f' Твой локальный IP: {local_ip}')
        mb.showerror("Локальный IP", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()
