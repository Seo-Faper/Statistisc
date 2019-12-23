'''
Created on 2019. 12. 21.

@author: dswhd
'''

from tkinter import *
master = Tk()

info=[  ["*", "*", "*", "@", "*"],
["*", "*", "*", "@", "*"],
["*", "*", "@", "*", "*"],
["*", "*", "@", "*", "*"],
["*", "*", "*", "@", "*"],
["*", "*", "@", "*", "*"],
["*", "@", "*", "*", "*"],
["*", "*", "*", "*", "@"],
["*", "*", "@", "*", "*"],
["*", "*", "*", "@", "*"],
["*", "@", "*", "*", "*"],
["*", "@", "*", "*", "*"],
["*", "*", "@", "*", "*"],
["*", "@", "*", "*", "*"],
["*", "@", "*", "*", "*"],
["*", "*", "@", "*", "*"],
]

heads = ["1","2","3","4","5"]
listbox = Listbox(master, width=60)
listbox.pack()
fixedlen = 10
listbox.insert(END, ("{:<15s}"+(fixedlen-len(heads[0]))*" " +"{:>5s}"+(fixedlen-len(heads[1]))*" " +"{:<25s}"+(fixedlen-len(heads[2]))*" " +"{:<5s}").format(heads[0],heads[1],heads[2],heads[3],heads[4]) )

for i  in range(len(info)):
    item = ("{:<15s}"+
            (fixedlen-len(str(info[i][0])))*" " +"{:>5d}"+
            (fixedlen-len(str(info[i][1])))*" " +"{:<25s}"+
            (fixedlen-len(str(info[i][2])))*" " +"{:<5s}").format(info[i][0],info[i][1],info[i][2],info[i][3],info[i][4])
    print (item)  # Gives nicely formatted lines
    listbox.insert(END, item)  #Lines are not nicely formatted in listbox

mainloop()