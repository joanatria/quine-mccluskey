from tkinter import *
from tkinter import messagebox
import globalvars
import quine 

root = Tk()
root.title('Quine McCluskey Method')
root.geometry('925x500+300+200')

root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file = 'lmbg.png')
Label(root, image = img, bg = "white").place(x = -10, y = 0)

frame = Frame(root, width = 350, height = 350, bg = 'white')
frame.place(x = 480, y = 70)

def on_enter(e):
    user1.delete(0, 'end')
def on1_enter(e):
    user2.delete(0, 'end')
def on2_enter(e):
    user3.delete(0, 'end')

heading1 = Label(frame, text = 'Enter minterms \n(separated by space e.g 3 4 5...)', fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 13, 'bold'))
heading1.place(x = 50, y = 5)

user1 = Entry(frame, width = 40, fg = 'black', border = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
user1.place(x = 35, y = 60)
user1.insert(0, 'minterms (separated by space e.g 3 4 5...)')
user1.bind('<FocusIn>', on_enter)


Frame(frame, width = 295, height = 2, bg = 'black').place(x = 30, y = 85)

heading2 = Label(frame, text = 'Enter number of variables (e.g 4)', fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 13, 'bold'))
heading2.place(x = 40, y = 100)

user2 = Entry(frame, width = 40, fg = 'black', border = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
user2.place(x = 35, y = 135)
user2.insert(0, 'number of variables (e.g 4)')
user2.bind('<FocusIn>', on1_enter)

Frame(frame, width = 295, height = 2, bg = 'black').place(x = 30, y = 160)

heading3 = Label(frame, text = "Enter don't cares (if none, input space)", fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 13, 'bold'))
heading3.place(x = 15, y = 180)

user3 = Entry(frame, width = 40, fg = 'black', border = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
user3.place(x = 35, y = 215)
user3.insert(0, "don't cares (if any)")
user3.bind('<FocusIn>', on2_enter)


Frame(frame, width = 295, height = 2, bg = 'black').place(x = 30, y = 240)


def values(mt, var, dc1):
    globalvars.initial()
    quine.maindriver(mt,var,dc1)
    text = globalvars.varin
    return text

def values1(mt, var, dc1):
    globalvars.initial()
    quine.maindriver(mt,var,dc1)
    text1 = ''
    text1 += globalvars.varnx
    return text1

def values2(mt, var, dc1):
    globalvars.initial()
    quine.maindriver(mt,var,dc1)
    text2 = ''
    text2 += globalvars.table + globalvars.pi + globalvars.epi + globalvars.ans
    return text2


def minterms():
    mt = user1.get()
    var = user2.get()
    dc1 = user3.get()
    
    screen = Toplevel(root)
    screen.title("Quine McCluskey Method")
    screen.geometry('925x500+300+200')
    screen.config(bg="#fff")

    Label(screen, text = values(mt,var,dc1), fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 11)).pack(pady=5, side= TOP, anchor="w")
    
    img1 = PhotoImage(file = 'lm1.png')
    Label(screen, image = img1, bg = "white").place(x = 500, y = 60)

    button1 = Button(screen, width = 29, pady = 3, text = 'Next', bg = '#C33332', fg = 'black', border = 0, command = minterms1)
    button1.place(x = 700, y = 450)

    screen.mainloop()

def minterms1():
    mt = user1.get()
    var = user2.get()
    dc2 = user3.get()

    screen1 = Toplevel(root)
    screen1.title("Quine McCluskey Method")
    screen1.geometry('925x500+300+200')
    screen1.config(bg="#fff")

    Label(screen1, text = values1(mt,var,dc2), fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 11)).place(x = 5, y = 1)
    
    img2 = PhotoImage(file = 'lm2.png')
    Label(screen1, image = img2, bg = "white").place(x = 500, y = 60)

    button2 = Button(screen1, width = 29, pady = 3, text = 'Next', bg = '#C33332', fg = 'black', border = 0, command = minterms2)
    button2.place(x = 700, y = 450)
    
    screen1.mainloop()

def minterms2():
    mt = user1.get()
    var = user2.get()
    dc3 = user3.get()

    screen2 = Toplevel(root)
    screen2.title("Quine McCluskey Method")
    screen2.geometry('925x500+300+200')
    screen2.config(bg="#fff")

    Label(screen2, text = values2(mt,var,dc3), fg = '#C33332', bg = 'white', font = ('Microsoft YaHei UI Light', 11)).place(x = 5, y = 0)

    img3 = PhotoImage(file = 'lm3.png')
    Label(screen2, image = img3, bg = "white").place(x = 500, y = 60)

    screen2.mainloop()  

button = Button(frame, width = 29, pady = 3, text = 'Enter', bg = '#C33332', fg = 'black', border = 0, command = minterms)
button.place(x = 80, y = 270)

root.mainloop()