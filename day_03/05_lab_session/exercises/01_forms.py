import tkinter
import json

# TODO: Create StringVar for name
# TODO: Create StringVar for name
root = tkinter.Tk()
root.title("My Application")
root.geometry("400x450")

name_var = tkinter.StringVar()
age_var = tkinter.StringVar()
theme_var = tkinter.StringVar(value="Light")
subscribe_var = tkinter.BooleanVar()
rating_var = tkinter.IntVar(value=3)


lbl_Name = tkinter.Label(root, text="Name: ", width=15, height=2, justify="left")
lbl_Name.grid(row=0, column=0, rowspan=1, sticky="nsew")

entry_Name = tkinter.Entry(root)
entry_Name.grid(row=0, column=1, columnspan=2)

lbl_Age = tkinter.Label(root, text="Age: ", width=15, height=2)
lbl_Age.grid(row=1, column=0, rowspan=1, sticky="nsew")

entry_Age = tkinter.Entry(root)
entry_Age.grid(row=1, column=1, columnspan=2)

lbl_Theme = tkinter.Label(root, text="Preferred Theme: ", width=15, height=2)
lbl_Theme.grid(row=2, column=0, rowspan=1, sticky="nsew")

radio_var = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(root, text="Light", variable=radio_var, value="Light")
radio1.grid(row=2, column=1, sticky="nsew")

radio2 = tkinter.Radiobutton(root, text="Dark", variable=radio_var, value="Dark")
radio2.grid(row=2, column=2, sticky="nsew")

chk_value = tkinter.BooleanVar()
chk_subscribe = tkinter.Checkbutton(
                root,
                text="Subscribe to Newsletter",
                variable=chk_value,
                height=3,
            )
chk_subscribe.grid(row=3, column=0, columnspan=3, sticky="nesw")

lbl_Rate = tkinter.Label(root, text="Rate us: ", width=15)
lbl_Rate.grid(row=4, column=0, rowspan=2, sticky="nsew")

slider_value = tkinter.IntVar(value=3)
slider_rate = tkinter.Scale(
    root,
    from_=1,
    to=5,
    orient="horizontal",
    variable=slider_value
)
slider_rate.grid(row=5, column=1, columnspan=2, sticky="nsew", pady=15)

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

def submit_form():
    # print("Name: ", entry_Name.get())
    # print("Age: ", entry_Age.get())
    # print("Theme: ", theme_var.get())
    # print("Subscribe: ", chk_value.get())
    # print("Rating: ", slider_value.get())
    data = [
        {'Name': entry_Name.get(),
         'Age': entry_Age.get(),
         'Theme': theme_var.get(),
         'Subscribe': chk_value.get(),
         'Rating': slider_value.get()
         }
    ]

    with open('feedback.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("data saved to feedback.json")
    root.destroy()

btn_submit = tkinter.Button(root, text="Submit", command=submit_form)
btn_submit.grid(row=6, column=1, sticky="nsew")








root.mainloop()
