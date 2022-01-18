from tkinter import *
from tkinter import font
import copy
import clipboard
import tkinter.messagebox

class M_Root:
    def __init__(self):
        pass
    def loop_start(self, title, geometry):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry) #가로 * 세로
        # root.geometry("640x480+300+100") #가로 * 세로 + x좌표 + y좌표
        self.root.resizable(False, False) # 각각 x,y 값 변경불가(창 크기 변경 불가)

    def loop_end(self):
        self.root.mainloop()

class file_load:
    def read(self):
        with open("git\\login_file.txt", "r",encoding= "utf8") as file:
            file_list = file.readlines()
        return file_list

    def name_read(self,file_list,load_box):
        for idx,value in enumerate(file_list): # 리스트의 번호와 값을 같이 받아옴
                if idx % 4 == 1: # catch line(name)
                    load_box.insert(0,value)
    
    def Append_file(self, NAME, ID, PW):
        try:
            if NAME.get("1.0",END) == "\n" or \
                ID.get("1.0",END) == "\n" or \
                    PW.get("1.0",END) == "\n" :
                tkinter.messagebox.showerror("error","다시 입력해주세요")

            else:
                with open("git\\login_file.txt","a",encoding="utf8") as login_file:
                    print("----------------", file= login_file)
                    print(NAME.get("1.0", END),file=login_file,end='')
                    NAME.delete("1.0",END) # 모든 텍스트 지우기
                    print(ID.get("1.0", END),file=login_file,end='')
                    ID.delete("1.0",END) # 모든 텍스트 지우기
                    print(PW.get("1.0", END),file=login_file,end='')
                    PW.delete("1.0",END) # 모든 텍스트 지우기
                tkinter.messagebox.showinfo("success","성공적으로 추가되었습니다")
        except:
            tkinter.messagebox.showerror("error","다시 시도해주세요")

        finally:
            self.root.destroy()
            Reload(storage_box)
            
class M_Listbox(file_load):
    def __init__(self, root, font_size, width, height, x_pos, y_pos):
        self.root = root
        self.font_size= font_size
        self.width = width
        self.height = height
        self.x = x_pos
        self.y = y_pos
        self.list_box = Listbox(root, selectmode ="single", height = 0)
        self.list_box.config(font = (None, font_size,'bold')) # 폰트 크기 지정
    def drow(self): # 그리기    
        self.list_box.place(width = self.width, height = self.height, x=self.x, y=self.y) 

class M_Button(file_load):
    def __init__(self, root, name, width, height, x_pos, y_pos, fnc = "None", *ID_PW):
        self.root = root
        self.name = name
        self.width = width
        self.height = height
        self.x = x_pos
        self.y = y_pos
        self.ID_PW = ID_PW
        self.root_existence = "False"
        if fnc == "LOAD":
            self.fnc = self.LOAD
            self.btn = Button(self.root, text = self.name, command = self.fnc)

        elif fnc == "COPY":
            self.fnc = self.COPY
            self.btn = Button(self.root, text = self.name, \
                command = lambda x = self.ID_PW[0] :self.fnc(x))

        elif fnc == "ADD":
            self.fnc = self.ADD
            self.btn = Button(self.root, text = self.name, command = self.fnc)

        elif fnc == "Append":
            self.fnc = self.Append_file
            self.btn = Button(self.root, text = self.name, \
                command = lambda x=ID_PW[0], y=ID_PW[1], z=ID_PW[2] :self.fnc(x, y, z))
        
        elif fnc == "DEL":
            self.fnc = self.DEL
            self.btn = Button(self.root, text = self.name, command = self.fnc)
    
    def drow(self): #그리기
        self.btn.place(width= self.width, height = self.height, x=self.x, y=self.y)

    def LOAD(self):
        try:
            self.load_box.delete(0,END) # 과거 load한 ID&PW 지우기
            select_idx = self.read_box.curselection() 
            # storage_box 에서 선택된 항목의 value 값 가져옴.
            file = file_load()
            login_list = file.read()
            point_idx = login_list.index(self.read_box.get(select_idx))
            ID = login_list[point_idx+1]
            PW = login_list[point_idx+2]
            self.load_box.insert(0,ID)
            self.load_box.insert(1,PW)
            self.ID = ID
            self.PW = PW

            copy_id_btn = M_Button(main_root.root, "ID_Copy", 100, 50, 530, 360,"COPY",ID)
            copy_id_btn.drow()
            copy_pw_btn = M_Button(main_root.root, "PW_Copy", 100, 50, 530, 420,"COPY",PW)
            copy_pw_btn.drow()

        except:
            pass

    def COPY(self,content):
        try:
            str(content)
            clipboard.copy(content)
        except:
            pass   
    
    def ADD(self):
        # 새로운 창 띄우기
        sub_root = M_Root()
        sub_root.loop_start( "ID&PW_ADD","320x240+480+320")
        
        ##make_input
        # NAME_input
        # (self, root, width, height, font_size, t_width, t_height, x_pos, y_pos)
        NAME_input = M_Text(sub_root.root, 30, 5, 20, 220, 40, 80 ,20)
        NAME_input.drow()
        # ID_input
        ID_input = M_Text(sub_root.root, 30, 5, 15, 220, 40, 80 ,90)
        ID_input.drow()
        # PW_input
        PW_input = M_Text(sub_root.root, 30, 5, 15, 220, 40, 80 ,140)
        PW_input.drow()

        ##make_label
        #Label_NAME
        label_NAME = M_Label(sub_root.root, "NAME:", 10, 20, 30)
        label_NAME.drow()
        #Lable_ID
        label_NAME = M_Label(sub_root.root, "ID:", 15, 20, 90)
        label_NAME.drow()
        #Label_PW
        label_PW = M_Label(sub_root.root, "PW:", 15, 20, 140)
        label_PW.drow()

        Append_btn = M_Button(sub_root.root, "Add the List", 100, 50, 110, 190,"Append",\
            NAME_input.text, ID_input.text, PW_input.text)
        Append_btn.drow()
        
        sub_root.loop_end()
    
    def DEL(self):
        try:
            select_idx = self.read_box.curselection() 
            # storage_box 에서 선택된 항목의 value 값 가져옴.
            file = file_load()
            login_list = file.read()
            login_list = list(login_list)
            point_idx = login_list.index(self.read_box.get(select_idx))
            del login_list[point_idx-1]
            del login_list[point_idx-1]
            del login_list[point_idx-1]
            del login_list[point_idx-1]
            with open("git\\login_file.txt","w",encoding="utf8") as login_file:
                for data in login_list:
                    print(data,file=login_file,end='')
                    
            tkinter.messagebox.showinfo("delete","삭제되었습니다")
        except:
            tkinter.messagebox.showerror("error","다시시도해주세요")
        finally:
            Reload(storage_box)

class M_Label:
    def __init__(self, root, name, font_size,x_pos, y_pos):
        self.root = root
        self.name = name
        self.font_size = font_size
        self.x = x_pos
        self.y = y_pos
        self.label = Label(self.root, text=name)
        self.label.config(font = (None, self.font_size, 'bold'))
    def drow(self):
        self.label.place(x = self.x, y = self.y)

class M_Text:
    def __init__(self, root, width, height, font_size, t_width, t_height, x_pos, y_pos):
        self.root = root
        self.width = width
        self.height = height
        self.font_size = font_size
        self.t_width = t_width
        self.t_height = t_height
        self.x = x_pos
        self.y = y_pos

        self.text= Text(self.root, width = self.width, height = self.height)
        self.text.config(font = (None, self.font_size , 'bold'))
    def drow(self):      
        self.text.place(width= self.t_width, height=self.t_height, x = self.x, y = self.y)
        self.text.bind("<Tab>",focus_next_widget)

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def Reload(box): # storage_box = box
    box.list_box.delete(0,END)
    box.name_read(storage_box.read(),storage_box.list_box)



main_root = M_Root()
main_root.loop_start( "ID&PW_Storage_Box","640x480+300+200")

storage_box = M_Listbox(main_root.root,18,300,400,50,35) # Listbox 1 (see the name)
storage_box.name_read(storage_box.read(),storage_box.list_box)
storage_box.drow()

select = storage_box.list_box.curselection()

ID_PW_box = M_Listbox(main_root.root, 15, 200, 50, 400, 35)
ID_PW_box.list_box.config(font = (None, 15)) # 폰트 크기 재지정
ID_PW_box.drow()

Load_btn = M_Button(main_root.root,"Load", 100, 50, 420, 420, "LOAD")
Load_btn.read_box = storage_box.list_box
Load_btn.load_box = ID_PW_box.list_box
Load_btn.drow()

Add_btn = M_Button(main_root.root,"Add", 100, 50, 420, 360, "ADD")
Add_btn.drow()

Del_btn = M_Button(main_root.root, "Delete", 100, 50, 530, 300,"DEL")
Del_btn.read_box = storage_box.list_box
Del_btn.drow()

#Lable_ID_PW
label_ID = M_Label(main_root.root,"ID:", 10, 355, 35)
label_ID.drow()
label_PW = M_Label(main_root.root,"PW:", 10, 355, 60)
label_PW.drow()



main_root.loop_end()
