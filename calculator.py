from tkinter import *

root = Tk()
root.title("Simple Calculator")


#---------- FUNCTIONS ----------

def btn_click(numbers):
    current = display_box.get()
    display_box.delete(0, END)
    display_box.insert(0, str(current) + str(numbers))


def btn_clear():
    display_box.delete(0, END)


def btn_add():
    first_number = display_box.get()
    global f_num
    global num_str
    f_num = float(first_number)
    num_str = str(f_num) + "+"
    display_box.delete(0, END)


def btn_subtract():
    first_number = display_box.get()
    global f_num
    global num_str
    f_num = float(first_number)
    num_str = str(f_num) + "-"
    display_box.delete(0, END)


def btn_multiply():
    first_number = display_box.get()
    global f_num
    global num_str
    f_num = float(first_number)
    num_str = str(f_num) + "*"
    display_box.delete(0, END)


def btn_divide():
    first_number = display_box.get()
    global f_num
    global num_str
    f_num = float(first_number)
    num_str = str(f_num) + "/"
    display_box.delete(0, END)


def btn_modulus():
    first_number = display_box.get()
    global f_num
    global num_str
    f_num = float(first_number)
    num_str = str(f_num) + "%"
    display_box.delete(0, END)


def btn_equal():
    second_number = display_box.get()
    display_box.delete(0, END)
    if '+' in num_str:
        display_box.insert(0, f_num + float(second_number))
    elif '-' in num_str:
        display_box.insert(0, f_num - float(second_number))
    elif '*' in num_str:
        display_box.insert(0, f_num * float(second_number))
    elif '/' in num_str:
        display_box.insert(0, f_num / float(second_number))
    else:
        display_box.insert(0, f_num % float(second_number))


#---------- TITLE ----------

head = Label(root, text="Simple Calculator", font=("Times New Roman", 25, "bold"))
head.pack(side=TOP, fill=X)

#---------- ENTRY and DISPLAY ----------

entry_frame = Frame(root)
entry_frame.pack()

display_box = Entry(entry_frame, width=40, borderwidth=20, justify="right", font=("Times New Roman", 20))
display_box.pack(fill=X)

#---------- BUTTONS ----------

button_frame = Frame(root)
button_frame.pack()

button_9 = Button(button_frame, text="9", padx=40, pady=20, command=lambda: btn_click(9))
button_8 = Button(button_frame, text="8", padx=40, pady=20, command=lambda: btn_click(8))
button_7 = Button(button_frame, text="7", padx=40, pady=20, command=lambda: btn_click(7))
button_6 = Button(button_frame, text="6", padx=40, pady=20, command=lambda: btn_click(6))
button_5 = Button(button_frame, text="5", padx=40, pady=20, command=lambda: btn_click(5))
button_4 = Button(button_frame, text="4", padx=40, pady=20, command=lambda: btn_click(4))
button_3 = Button(button_frame, text="3", padx=40, pady=20, command=lambda: btn_click(3))
button_2 = Button(button_frame, text="2", padx=40, pady=20, command=lambda: btn_click(2))
button_1 = Button(button_frame, text="1", padx=40, pady=20, command=lambda: btn_click(1))
button_0 = Button(button_frame, text="0", padx=87, pady=20, command=lambda: btn_click(0))
button_dot = Button(button_frame, text=".", padx=41, pady=20, command=lambda: btn_click('.'))

button_del = Button(button_frame, text="DEL", padx=34, pady=20)
button_clear = Button(button_frame, text="CLEAR", padx=25, pady=20, command=btn_clear)
button_plus = Button(button_frame, text="+", padx=40, pady=20, command=btn_add)
button_minus = Button(button_frame, text="-", padx=40, pady=20, command=btn_subtract)
button_asterik = Button(button_frame, text="*", padx=41, pady=20, command=btn_multiply)
button_slash = Button(button_frame, text="/", padx=40, pady=20, command=btn_divide)
button_mod = Button(button_frame, text="MOD", padx=29, pady=20, command=btn_modulus)
button_equal = Button(button_frame, text="=", padx=38, pady=20, command=btn_equal)

button_9.grid(row=0, column=2)
button_8.grid(row=0, column=1)
button_7.grid(row=0, column=0)
button_6.grid(row=1, column=2)
button_5.grid(row=1, column=1)
button_4.grid(row=1, column=0)
button_3.grid(row=2, column=2)
button_2.grid(row=2, column=1)
button_1.grid(row=2, column=0)
button_0.grid(row=3, column=0, columnspan=2)
button_dot.grid(row=3, column=2)

button_del.grid(row=0, column=3)
button_clear.grid(row=0, column=4)
button_plus.grid(row=1, column=3)
button_minus.grid(row=1, column=4)
button_asterik.grid(row=2, column=3)
button_slash.grid(row=2, column=4)
button_mod.grid(row=3, column=3)
button_equal.grid(row=3, column=4)


root.mainloop()
