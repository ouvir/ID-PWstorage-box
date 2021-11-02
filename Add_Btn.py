from tkinter import *

def btncmd():
    print("버튼 클릭됨.")
    
def ADD():
    root2 = Tk()
    root2.title("ID&PW_ADD")
    root2.geometry("320x240+480+320")
    root2.resizable(False, False)

    txt = Text(root2, width = 30, height =5)
    txt.pack()

    Add_btn = Button(root2, text ="Add the List", command=btncmd)
    Add_btn.place(width= 100, height=50, x=110, y=190)
    root2.mainloop()
    pass