from tkinter import*
root = Tk()

lbl = Label(root, text = "설문지 번호 : ")
lbl.grid(row = 0, column = 0)
txt = Entry(root)
txt.grid(row = 0, column = 1)


btn = Button(root, text = "Ok", width = 15)
btn.grid(row = 1, column = 1)

root.mainloop()

#일반적 특징 3개 