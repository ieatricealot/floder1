import tkinter as tk
class Timer :
    def __init__(self,root):
        self.root=root
        self.root.title("Timer")
if __name__=="__main__":
    root = tk.Tk()
    timer=Timer(root)
    root.mainloop()