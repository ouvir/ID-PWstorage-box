from tkinter import *
import Add_Btn
import Copy_Btn
root = Tk()
root.title("ID&PW_Storage_Box")
root.geometry("640x480+300+200") #가로 * 세로
# root.geometry("640x480+300+100") #가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # 각각 x,y 값 변경불가(창 크기 변경 불가)

# ID와 Password를 저장 할 공간
Login_dict = {}
Login_dict["naver"] = ["naver_id","naver_password"]
Login_dict["google"] = ["google_id","google_password"]
Login_dict["youtube"] = ["youtube_id","youtube_password"]
# 다른 파일에서 로드해올수있어야함.


storage_box = Listbox(root, selectmode ="single", height = 0) #storage_box 기본정보

for name in list(Login_dict.keys()): # Login_dict에서 키 값(저장이름)을 가져 옴. 
    storage_box.insert(0,name) # 가장 위에 저장.
storage_box.config(font = (None, 18, 'bold')) # 폰트 크기 지정
storage_box.place(width = 300, height = 400, x=50, y=35) # 그리기

select = storage_box.curselection()
# select : storage_box에서 선택된 항목의 순서를 저장

ID_PW_box = Listbox(root, selectmode ="single", height = 0) # ID_PW_box 기본정보
ID_PW_box.config(font = (None, 15))
ID_PW_box.place(width = 200, height = 50, x= 400, y=35) # 그리기


# Load_Button
def Loading_Id_Pw():
    try:
        ID_PW_box.delete(0,END) # 과거 load한 ID&PW 지우기
        select = storage_box.curselection() # storage_box 에서 선택된 항목의 value 값 가져옴.
        ID = Login_dict[storage_box.get(select)][0]
        PW = Login_dict[storage_box.get(select)][1]
        ID_PW_box.insert(0,ID)
        ID_PW_box.insert(1,PW)
    except:
        pass

load_btn = Button(root, text="Load",command = Loading_Id_Pw)
load_btn.place(width= 100, height=50, x=420, y=420)


# copy_Button
copy_btn = Button(root, text ="Copy", command=Copy_Btn.COPY) # 복사 버튼
copy_btn.place(width= 100, height=50, x=530, y=420)

# Add_list
add_btn = Button(root, text ="Add", command=Add_Btn.ADD) # 추가 버튼
add_btn.place(width= 100, height=50, x=420, y=360)

#Lable
label_ID = Label(root, text="ID:")
label_ID.config(font = (None, 10, 'bold'))
label_ID.place(x=355,y=35)

label_PW = Label(root, text="PW:")
label_PW.config(font = (None, 10, 'bold'))
label_PW.place(x=355,y=60)


root.mainloop()