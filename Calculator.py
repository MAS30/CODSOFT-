import tkinter as tk
from tkinter import *


calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0, "end")

root=Tk()
root.title("Calculator by Affan")
root.geometry("338x500+950+120")
root.resizable(False,False)
root.configure(bg="#efedf5")

text_result=tk.Text(root, bg="#ede9bb", width=9, height=1, font=("arial", 50))
text_result.grid()
#root.mainloop()

Button(root,text="C",width=3,height=1,font=("Arial",25,"bold"),bd=4,fg="#fff",bg="black",command=lambda: clear_field()).place(x=8,y=105)
Button(root,text="/",width=3,height=1,font=("Arial",25,"bold"),bd=3,fg="#fff",bg="#035199",command=lambda: add_to_calculation("/")).place(x=92,y=105)
Button(root,text="%",width=3,height=1,font=("Arial",25,"bold"),bd=3,fg="#fff",bg="#035199",command=lambda: add_to_calculation("%")).place(x=174,y=105)
Button(root,text="x",width=3,height=1,font=("Arial",25,"bold"),bd=3,fg="#fff",bg="#035199",command=lambda: add_to_calculation("x")).place(x=256,y=105)

Button(root,text="7",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(7)).place(x=8,y=188)
Button(root,text="8",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(8)).place(x=92,y=188)
Button(root,text="9",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(9)).place(x=174,y=188)
Button(root,text="-",width=3,height=1,font=("arial",25,"bold"),bd=3,fg="#fff",bg="#035199",command=lambda: add_to_calculation("-")).place(x=256,y=185)

Button(root,text="4",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(4)).place(x=8,y=268)
Button(root,text="5",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(5)).place(x=92,y=268)
Button(root,text="6",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(6)).place(x=174,y=268)
Button(root,text="+",width=3,height=1,font=("arial",25,"bold"),bd=3,fg="#fff",bg="#035199",command=lambda: add_to_calculation("+")).place(x=256,y=265)

Button(root,text="1",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(1)).place(x=8,y=348)
Button(root,text="2",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(2)).place(x=92,y=348)
Button(root,text="3",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(3)).place(x=174,y=348)

Button(root,text="0",width=8,height=1,font=("Times New Roman",23,"bold"),bd=1,fg="#061d38",bg="#9abde6",command=lambda: add_to_calculation(0)).place(x=8,y=425)
Button(root,text=".",width=3,height=1,font=("Times New Roman",25,"bold"),bd=1,fg="#061d38",bg="#459fba",command=lambda: add_to_calculation(".")).place(x=174,y=424)
Button(root,text="=",width=3,height=3,font=("Times New Roman",25,"bold"),bd=3,fg="#fff",bg="#e89f2a",command=lambda: evaluate_calculation()).place(x=256,y=345)

root.mainloop()

