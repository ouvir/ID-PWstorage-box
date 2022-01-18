from tkinter import *
import Add_Btn
import Copy_Btn
root = Tk()
root.title("ID&PW_Storage_Box")
root.geometry("640x480+300+200") #가로 * 세로
# root.geometry("640x480+300+100") #가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # 각각 x,y 값 변경불가(창 크기 변경 불가)


# Listbox 1 (see the name)
storage_box = Listbox(root, selectmode ="single", height = 0) #storage_box 기본정보

login_file = open('git\\login_file.txt','r',encoding = 'utf8')
login_list = login_file.readlines() # file에 저장된 정보를 리스트의 형태로 불러옴 
for idx,name in enumerate(login_list): # 리스트의 번호와 값을 같이 받아옴
    if idx % 4 == 1: # 리스트에서 이름의 정보를 담고있는 항목만 실행
        storage_box.insert(0,name) # storage_box에 이름 정보 삽입
login_file.close() # 파일 닫기

storage_box.config(font = (None, 18, 'bold')) # 폰트 크기 지정
storage_box.place(width = 300, height = 400, x=50, y=35) # 그리기

select = storage_box.curselection()
# select : storage_box에서 선택된 항목의 순서를 저장

# Listbox 2 (if click the Load_Button, can see the ID,PW)
ID_PW_box = Listbox(root, selectmode ="single", height = 0) # ID_PW_box 기본정보
ID_PW_box.config(font = (None, 15))
ID_PW_box.place(width = 200, height = 50, x= 400, y=35) # 그리기


# Load_Button
def Loading_Id_Pw():
    try:
        ID_PW_box.delete(0,END) # 과거 load한 ID&PW 지우기
        select_idx = storage_box.curselection() # storage_box 에서 선택된 항목의 value 값 가져옴.
        with open('login_file.txt','r',encoding = 'utf8') as login_file:
            login_list = login_file.readlines()
            point_idx = login_list.index(storage_box.get(select_idx))
            ID = login_list[point_idx+1]
            PW = login_list[point_idx+2]
            ID_PW_box.insert(0,ID)
            ID_PW_box.insert(1,PW)

        # ID_copy_Button
        copy_btn = Button(root, text ="ID_Copy", command = lambda X=ID : Copy_Btn.COPY(X)) # 복사 버튼
        copy_btn.place(width= 100, height=50, x=530, y=360)

        # PW_copy_BUtton
        copy_btn = Button(root, text ="PW_Copy", command = lambda X=PW : Copy_Btn.COPY(X)) # 복사 버튼
        copy_btn.place(width= 100, height=50, x=530, y=420)
    except:
        pass

load_btn = Button(root, text="Load",command = Loading_Id_Pw)
load_btn.place(width= 100, height=50, x=420, y=420)


def Reload():
    storage_box.delete(0,END)
    login_file = open('login_file.txt','r',encoding = 'utf8')
    login_list = login_file.readlines() # file에 저장된 정보를 리스트의 형태로 불러옴 
    for idx,name in enumerate(login_list): # 리스트의 번호와 값을 같이 받아옴
        if idx % 4 == 1: # 리스트에서 이름의 정보를 담고있는 항목만 실행
            storage_box.insert(0,name) # storage_box에 이름 정보 삽입

# Add_list
add_btn = Button(root, text ="Add", command= Add_Btn.ADD) # 추가 버튼
add_btn.place(width= 100, height=50, x=420, y=360)

# list_refresh
refresh_icon = PhotoImage(file="C:/Users/kilhy/projects/git/refresh_icon.png")
refresh_btn = Button(root, image= refresh_icon , command= Reload) # 새로고침버튼
refresh_btn.place(width= 50, height=50, x=300, y=385)
#Lable_ID
label_ID = Label(root, text="ID:")
label_ID.config(font = (None, 10, 'bold'))
label_ID.place(x=355,y=35)
#Label_PW
label_PW = Label(root, text="PW:")
label_PW.config(font = (None, 10, 'bold'))
label_PW.place(x=355,y=60)


root.mainloop()