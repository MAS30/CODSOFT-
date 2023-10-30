from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        messagebox.showinfo("Note", "Task Added Successfully 😎.")

    else:
        messagebox.showwarning("Warning", "Please Enter Task.")

def deleteTask():
    lb.delete(ANCHOR)

widget = Tk()
widget.geometry("500x450+450+150")
widget.title("To Do List By AFFAN")
widget.config(bg="#394e7d")
widget.resizable(width=False, height=False)

frame = Frame(widget)
frame.pack(pady=20)

lb = Listbox(frame,width=22,height=6,font=("Calibri", 22),border=4,fg="#070442",bg="white",selectbackground="#3c93b5",activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(widget,font=("Times", 20),border=5,bg="#919174")
my_entry.pack(pady=20)

button_frame = Frame(widget)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame,text="Add Task",font=("sans-serif",18),bg="#5ee05a",padx=20,pady=20,command=newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame,text="Delete Task",font=("sans-serif",18),bg='#ab4846',padx=20,pady=20,command=deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

widget.mainloop()
