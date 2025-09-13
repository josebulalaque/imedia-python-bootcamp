import tkinter

message = """
Loops within loops again
A silent function returns
The logic is clear
"""

root = tkinter.Tk()
root.title("Python Haiku")
root.geometry("300x300")

label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()
