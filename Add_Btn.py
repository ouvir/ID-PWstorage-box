from tkinter import *
import tkinter.messagebox

def ADD():
        # 새로운 창 띄우기
    root2 = Tk()
    root2.title("ID&PW_ADD")
    root2.geometry("320x240+480+320")
    root2.resizable(False, False)

    ##make_input
    # ID_input
    ID_input = Text(root2, width = 30, height =5)
    ID_input.config(font = (None, 15, 'bold'))
    ID_input.place(width= 220, height=40, x=80, y=90)
    # PW_input
    PW_input= Text(root2, width = 30, height =5)
    PW_input.config(font = (None, 15, 'bold'))
    PW_input.place(width= 220, height=40, x=80, y=140)
    # NAME_input
    NAME_input= Text(root2, width = 30, height =5)
    NAME_input.config(font = (None, 20, 'bold'))
    NAME_input.place(width= 220, height=40, x=80, y=20)

    ##make_label
    #Lable_ID
    label_ID = Label(root2, text="ID:")
    label_ID.config(font = (None, 15, 'bold')) 
    label_ID.place(x=20,y=90)
    #Label_PW
    label_PW = Label(root2, text="PW:")
    label_PW.config(font = (None, 15, 'bold'))
    label_PW.place(x=20,y=140)
    #Label_NAME
    label_NAME = Label(root2, text="NAME:")
    label_NAME.config(font = (None, 10, 'bold'))
    label_NAME.place(x=20,y=30)

    def Append_File():
        try:
            if NAME_input.get("1.0",END) == "\n" or \
                ID_input.get("1.0",END) == "\n" or \
                    PW_input.get("1.0",END) == "\n" :
                tkinter.messagebox.showerror("error","다시 입력해주세요")

            else:
                with open("login_file.txt","a",encoding="utf8") as login_file:
                    print("----------------", file= login_file)
                    print(NAME_input.get("1.0", END),file=login_file,end='')
                    NAME_input.delete("1.0",END) # 모든 텍스트 지우기
                    print(ID_input.get("1.0", END),file=login_file,end='')
                    ID_input.delete("1.0",END) # 모든 텍스트 지우기
                    print(PW_input.get("1.0", END),file=login_file,end='')
                    PW_input.delete("1.0",END) # 모든 텍스트 지우기
                tkinter.messagebox.showinfo("success","성공적으로 추가되었습니다")
        except:
            tkinter.messagebox.showerror("error","다시 시도해주세요")

        finally:
            root2.destroy()
        
    Add_btn = Button(root2, text ="Add the List", command = Append_File)
    Add_btn.place(width= 100, height=50, x=110, y=190)
    print(NAME_input.get("1.0", END),end='')
    root2.mainloop()