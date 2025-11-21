from tkinter import *
from tracemalloc import Frame
import requests

class AppUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Ball Odd")
        self.master.geometry("300x100+300+200")
        # self.master.pack()
        self.create_widget()

    def create_widget(self):
        self.btn01=Button(text="获取数据",command=self.GetData)
        self.btn01.pack()

    def GetData(self):
        response = requests.get("http://127.0.0.1:8080/odd500")

class CreateTK():
    window = Tk()
    appui = AppUI(master=window)
    window.mainloop()




