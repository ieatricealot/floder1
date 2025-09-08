import tkinter as tk 
import time as tm
class Timer :
    def __init__(self,root):
        self.root=root
        self.root.title("Timer")
        self.start = tk.Button(root, fg="black", bg="green" , text="Start")
        self.start.pack(pady=20)

        self.start = tk.Button(root, fg="black", bg="red" , text="Hello", justify=['left'])
        self.start.pack(pady=20)

       #67
# self.start = tk.wraplength:ScreenUnits = 0self.start.pack(pady=67)




if __name__=="__main__":
    root = tk.Tk()
    timer=Timer(root)
    root.mainloop()

