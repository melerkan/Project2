from tkinter import *
import tkinter as tk

base = tk.Tk()

base.geometry("312x324")
base.resizable(0,0)
base.title("Calculator")

def btn_click(item):
	global formula
	formula = formula + str(item)
	input_text.set(formula)

def btn_clear():
	global formula
	formula = ""
	input_text.set("")

def btn_equal():
	global formula
	result = str(eval(formula))
	input_text.set(result)
	formula = ""

formula = ""
input_text = StringVar()

input_frame = Frame(base, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 22, 'bold'), textvariable=input_text, width=50, bg="white", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(base, width=312, height=272, bg="grey")
btns_frame.pack()

clear = Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="white", width=10, height=3, bd=0, bg="mediumorchid", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="white", width=10, height=3, bd=0, bg="gold", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
subtract = Button(btns_frame, text="-", fg="white", width=10, height=3, bd=0, bg="cornflowerblue", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
add = Button(btns_frame, text="+", fg="white", width=10, height=3, bd=0, bg="coral", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
decimal = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="white", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equal = Button(btns_frame, text="=", fg="white", width=10, height=3, bd=0, bg="mediumseagreen", cursor="hand2", command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

base.mainloop()














