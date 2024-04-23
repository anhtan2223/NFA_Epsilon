from automathon import NFA
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from NFAe import *

def CheckString(event = None , entry : Entry = None , window = None):
    string = entry.get()

    isOke = True
    for i in string :
        if i not in nfa_epsilon.sigma :
            isAccept = False
            message = f"Chuỗi Có Kí Tự Không Có Trong Bộ Nhập Vui Lòng Nhập Lại các kí tự bao gồm : {nfa_epsilon.sigma}"
            entry.delete(0,END)
            isOke = False
    
    if(isOke == True):
        path = nfa_epsilon.MoveWithString(string)
        pathMessage = f'Start : {path.pop(0)} \n'
        for i in string:
            pathMessage = pathMessage + f'Move with {i} → {path.pop(0)}\n'


        isAccept = nfa_epsilon.IsAccept()
        message = f"Chuỗi {string} {'Được Đón Nhận' if isAccept else 'Không Được Đón Nhận'} \n Các Biến Sau Khi Qua Chuỗi Bao Gồm : {nfa_epsilon.current}"
        pathMessage = pathMessage +'\n\n' + message
        
        global pathResult
        try :
            pathResult.destroy()
        except :
            pass
        pathResult = Label(window , text=pathMessage , font = ("Arial", 14))
        pathResult.place(relx=.5,rely=.8,anchor=CENTER)


    messagebox.showinfo("Kết Quả" , message)
    nfa_epsilon.ResetCurrent()

def GetFile(window):
    try :
        filepath = filedialog.askopenfilename(title="Choose NFA text file", filetypes=(("Text Document", "*.txt"), ("All files", "*.*")))
        file = open(filepath, "r")
        print("Open File : " , file)
        string = file.read()
        input = string.split('\n')
        var = input.pop(0).split(' ')
        sigma = input.pop(0).split(' ')
        start = input.pop(0)
        end = set(input.pop(0).split(' '))

        map = dict()
        imageMap = dict()
        index = ''
        while(len(input) != 0) :
            value = input.pop(0).split(' ')
            if(len(value) == 1) : 
                index = value[0]
                continue
            try :
                # print({ value[0] : set(value[1:]) })
                map[index][value[0]] = set(value[1:])
                if value[0]!='e':
                    imageMap[index][value[0]] = set(value[1:])
                else :
                    imageMap[index][''] = set(value[1:])
            except KeyError:
                map[index] = { value[0] : set(value[1:]) }
                if value[0]!='e':
                    imageMap[index] = { value[0] : set(value[1:]) }
                else :
                    imageMap[index] = { '' : set(value[1:]) }
                # print("Error ")
            except :
                print("Someting False")
                break
        file.close()
        nfa = NFA(var, sigma, imageMap, start, end)
        global nfa_epsilon
        nfa_epsilon = NFAe(var , sigma , map , start , end)

        try :
            nfa.view("NFA")
        except :
            pass
        ShowImage(window)
        
    except IndexError :
        messagebox.showerror('Some Eror Was Rise' , "File Không Hợp Lệ Vui Lòng Chọn File Khác")
        
def ShowImage(window):
    img = PhotoImage(file="NFA.gv.png")
    global imgLabel
    try :
        imgLabel.destroy()
    except :
        pass
    imgLabel = Label(window, image=img)
    imgLabel.place(relx=.5,rely=.4,anchor=CENTER)
    imgLabel.image = img
    inputFrame = Frame(window)
    stringLabel = Label(inputFrame, text='Chuỗi cần kiểm tra', font=("Arial", 18))
    stringInput = Entry(inputFrame, width=40)
    stringInput.bind("<Return>" , func = lambda event : CheckString(entry=stringInput , window=window)  )
    checkButton = Button(inputFrame, text="Kiểm tra", font=('Arial', 18) ,command = lambda : CheckString(entry=stringInput , window=window) )

    stringLabel.grid(column=0, row=0)
    stringInput.grid(column=1, row=0)
    checkButton.grid(column=2, row=0)
    inputFrame.place(relx=.5,rely=.7,anchor=CENTER)