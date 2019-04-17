from tkinter import*
from time import*

## 전역 변수 선언 부분 ##
fnameList=["jeju1.gif"]
photoList=[None]*9
num=0

## 함수 선언 부분 ##
def clickNext():
    global num
    num+=1
    if num>8:
           num=8
    photo=photoImage(file="gif/"+fnameList[num])
    pLabel.configure(image=photo)
           pLabel.image=photo

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev=Button(window,text="<<이전",command=clickPrev)
btnNext=Button(window,text="다음>>",command=clickNext)

photo=PhotoImage(file="gif/"+fnameList[0])
pLabel=Label(window,image=photo)

btnPrev.place(x=250,y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=50)

window.mainloop()
