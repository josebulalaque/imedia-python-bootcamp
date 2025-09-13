import tkinter

root = tkinter.Tk()
root.title("My Application")
root.geometry("1100x180")
root.configure(background="yellow")

label = tkinter.Label(root, text="Enter your password:")
label.pack(side="top")

entry = tkinter.Entry(root, show="*")
entry.pack()

user_input = tkinter.StringVar(root, value="")
bground = "white"
label = tkinter.Label(root, textvariable=user_input, font=("Arial", 35, "bold"), bg="yellow")
label.pack()

def check_password(event):
    given_text = entry.get()

    if given_text == "admin":
        user_input.set("Password Correct! Access Granted!")
        label.configure(bg="green")
        root.configure(background="green")
    else:
        user_input.set("Incorrect Password. Try again!")
        label.configure(bg="red")
        root.configure(background="red")

root.bind("<Return>", check_password)
root.mainloop()
