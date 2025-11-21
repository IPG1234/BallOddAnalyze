from tkinter import *
from tracemalloc import Frame
import requests
import threading

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
        form_data={"time":"2025-05-25"}
        response = requests.post("http://127.0.0.1:5000/500Data/GetData")
        # print(123)

class TKThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        window = Tk()
        appui=AppUI(master=window)
        window.mainloop()


class CreateTK():
    def __init__(self):
        self.TKThread=TKThread()
        self.TKThread.start()



