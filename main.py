from tkinter import *

case_cote_long = 15
class Coo:
    lin = 0
    col = 0

    def __init__(self, col, lin):
        self.lin = lin
        self.col = col





def getIndex(col, lin):
    if 0>col > line_longer or 0>lin > line_longer:

        return 0
    return col- 1+((lin - 1) * line_longer)

def getCoo(index):
    x = index +1
    lin = 1
    while x >line_longer:
        x = x-line_longer
        lin = lin +1

    coo = Coo(x, lin)

    return coo




def GetNbOfAliveAround(col, lin):
    global cases
    x = 0

    try:
        if cases[getIndexDir(col, lin, 1)]:

            x = x+1
    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 2)]:
            x = x+1
    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 3)]:
            x = x+1
    except:
        pass

    try:

        if cases[getIndexDir(col, lin, 4)]:
            x = x+1

    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 5)]:
            x = x+1
    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 6)]:
            x = x+1
    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 7)]:
            x = x+1
    except:
        pass

    try:
        if cases[getIndexDir(col, lin, 8)]:
            x = x+1
    except:
        pass

    return x
def switch(col, lin):
    global cases
    if cases[getIndex(col, lin)]:
        cases[getIndex(col, lin)] = False
        set(col, lin, False)

    else:
        cases[getIndex(col, lin)] = True
        set(col, lin, True)

def set(col, lin, bool = True):
    global cases
    cases[getIndex(col, lin)] = bool

    x = 25 + (lin - 1) * case_cote_long


    y = 25 + (col - 1) * case_cote_long

    if bool:
        can.create_rectangle(x, y, x + case_cote_long, y + case_cote_long, fill="blue", outline="black")
    else:
        can.create_rectangle(x, y, x + case_cote_long, y + case_cote_long, fill="white", outline="black")


def getIndexDir(col, lin, dir):
    if dir==0:
        return getIndex(col,lin)
    elif dir == 1:
        return getIndex(col, lin+1)
    elif dir == 2:
        return getIndex(col+1, lin+1)
    elif dir == 3:
        return getIndex(col+1, lin)
    elif dir == 4:
        return getIndex(col+1 , lin-1)
    elif dir == 5:
        return getIndex(col , lin-1)
    elif dir == 6:
        return getIndex(col-1, lin-1)
    elif dir == 7:
        return getIndex(col-1, lin)
    elif dir == 8:
        return getIndex(col-1, lin+1)
    else:
        return



line_longer = 50
window = Tk()
cases = [False] * 2500





window.geometry('1000x1000')
window.title("le jeu de la vie")
window.resizable(height=False, width=False)
can = Canvas(window, width=1000,height=1000)


def color(col, lin):
    global can
    nCol = 25 + col*case_cote_long - case_cote_long
    nLin = 25 + lin*case_cote_long - case_cote_long
    can.create_rectangle(nLin, nCol, nLin+case_cote_long , nCol +case_cote_long, fill = "red",  outline = "black")

for i in range(0, 2500):

    coo = getCoo(i)

    lin = coo.lin
    x = 25 + (lin-1)*case_cote_long

    col = coo.col
    y = 25 + (col-1)*case_cote_long

    can.create_rectangle(x, y, x+case_cote_long, y+case_cote_long)

    '''
    color(5, 10)
    color(getCoo(getIndexDir(5, 10, 1)).col, getCoo(getIndexDir(5, 10, 1)).lin)
    color(getCoo(getIndexDir(5, 10, 2)).col, getCoo(getIndexDir(5, 10, 2)).lin)
    color(getCoo(getIndexDir(5, 10, 3)).col, getCoo(getIndexDir(5, 10, 3)).lin)
    color(getCoo(getIndexDir(5, 10, 4)).col,getCoo(getIndexDir(5, 10, 4)).lin )
    color(getCoo(getIndexDir(5, 10, 5)).col, getCoo(getIndexDir(5, 10, 5)).lin)
    color(getCoo(getIndexDir(5, 10, 6)).col, getCoo(getIndexDir(5, 10, 6)).lin)
    color(getCoo(getIndexDir(5, 10, 7)).col, getCoo(getIndexDir(5, 10, 7)).lin)
    color(getCoo(getIndexDir(5, 10, 8)).col, getCoo(getIndexDir(5, 10, 8)).lin)
'''

    can.pack()
def on_click(event):
    global cases
    cooX = 0
    cooY = 0
    for i in range(0, 2500):
        if (25 + (i-1)*case_cote_long)<event.x < (25 + (i-1)*case_cote_long + case_cote_long):
            cooX = i






    for i in range(0, 2500):
        if (25 + (i-1)*case_cote_long)<event.y < (25 + (i-1)*case_cote_long + case_cote_long):
            cooY = i


    if cooX == 0 or cooY==0:
        return

    switch(cooY, cooX)

def on_enter(event):
    global cases
    copy_cases = cases.copy()



    for i in range(0, 2500):
        pos = getCoo(i)
        n= GetNbOfAliveAround(pos.col, pos.lin)



        coo = getCoo(i)

        lin = coo.lin
        x = 25 + (lin - 1) * case_cote_long

        col = coo.col
        y = 25 + (col - 1) * case_cote_long


        if cases[i]:
            if n == 2 or n==3:
                pass
            else:
                copy_cases[i] = False
                can.create_rectangle(x, y, x + case_cote_long, y + case_cote_long, fill="white", outline="black")
        else:
            if n==3:
                copy_cases[i] = True
                can.create_rectangle(x, y, x + case_cote_long, y + case_cote_long, fill="blue", outline="black")


    cases = copy_cases
    #can.pack()



set(25, 25)
set(26, 25)
set(27, 25)
set(28, 25)
set(29, 25)



window.bind("<Return>", on_enter)
window.bind("<Button-1>", on_click)
window.focus_set()
window.mainloop()
#print("before")






