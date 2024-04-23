from tkinter import *
from Handle import GetFile

window = Tk()
window.title("Demo NFA")

title = Label(window, text = "CHƯƠNG TRÌNH DEMO  XÂY DỰNG NFA-ε", font = ("Arial Bold", 20)).place(relx=.5,rely=.05,anchor= CENTER)
# title.grid(column=1, row=0)

readNFAButton = Button(window, text = "Get NFA-ε",font=('Arial', 14), command = lambda : GetFile(window))
readNFAButton.place(relx=.5,rely=.1,anchor= CENTER)
window.geometry('1280x720')
window.mainloop()