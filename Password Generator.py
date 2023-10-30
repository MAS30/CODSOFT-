from tkinter import *
import pyperclip # module to copy our generated password to clipboard.
import random
from tkinter import messagebox, IntVar

root = Tk()
root.geometry("400x380+500+150")
root.title("Password Generator by Affan")
root.configure(bg="#394e7d")

passstr = StringVar() # used to store the password generated

passlen = IntVar() # store the length of the password entered by the user

passlen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password = ""

    length = passlen.get()
    if length > 0:
        for x in range(length):
            password = password + random.choice(pass1)

        passstr.set(password) # setting the password to the entry widget
    else:
        messagebox.showerror("Error","Please Enter Valid Length 🙂.")
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

Label(root, text="Random Password Generator", font="Verdana 17 bold underline ", bg="#394e7d", fg="white").pack(pady=20)
Label(root, text="@AFFAN_SIDDIQUI",font="Roman 12 italic", bg="#394e7d" ,fg="white").place(x=275,y=345)

Label(root, text="Enter Password Length: ",font="Tahoma 12 bold", bg="#394e7d" , fg="white").place(x=10,y=105)
Entry(root, textvariable=passlen,border=4).place(x=215,y=105)

Button(root, text="  Generate  ",font="Ebrima 11 bold ", command=generate,border=5,bg="#b6c3e3").place(x=230,y=145)

Label(root, text="Generated Password: ",font="Tahoma 12 bold" , bg="#394e7d" , fg="white").place(x=10,y=200)
Entry(root, textvariable=passstr,border=4,font="calibri 12 bold" ,bg="white",width=20).place(x=200,y=200)

Button(root, text="Copy to clipboard", command=copytoclipboard,border=5,font="Ebrima 11 bold",bg="#b6c3e3").place(x=215,y=245)

root.mainloop()