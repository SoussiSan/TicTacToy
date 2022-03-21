
from tkfn import *
import tkfn
def end():
    b1.config(text='')
    b2.config(text='')
    b3.config(text='')
    b4.config(text='')
    b5.config(text='')
    b6.config(text='')
    b7.config(text='')
    b8.config(text='')
    b9.config(text='')

def leftclick(butn):
    butn.config(text='Y')
    if b1['text'] == 'Y' and b2['text'] == 'Y' and b3['text'] == 'Y' or \
            b1['text'] == 'Y' and b5['text'] == 'Y' and b9['text'] == 'Y' or \
            b1['text'] == 'Y' and b4['text'] == 'Y' and b7['text'] == 'Y' or \
            b2['text'] == 'Y' and b5['text'] == 'Y' and b8['text'] == 'Y' or \
            b3['text'] == 'Y' and b6['text'] == 'Y' and b9['text'] == 'Y' or \
            b4['text'] == 'Y' and b5['text'] == 'Y' and b6['text'] == 'Y' or \
            b7['text'] == 'Y' and b8['text'] == 'Y' and b9['text'] == 'Y'or \
            b3['text'] == 'Y' and b5['text'] == 'Y' and b7['text'] == 'Y':
        msgbox('showinfo', 'the end of the game', 'Y is the winner')
        end()
def rightclick(butn):
    butn.config(text='X')
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or \
            b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or \
            b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or \
            b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or \
            b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' or \
            b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or \
            b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'or \
            b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        msgbox('showinfo', 'the end of the game', 'X is the winner')
        end()
def game():
    if b1['text'] == 'X':
        print('finish')
win = Tk()
bg = '#702070'
win.config(bg=bg)
win.title('Tic Toc Toy')
Label(win, text='Tic Toc Toy', bg=bg, fg='yellow', font='mistral 50').pack(padx=5, pady=5)
frm = Frame(bg=bg)
frm.pack(padx=15, pady=5)
Label(frm, text='Right Click', font='None 15 bold', bg=bg, fg='white').grid(row=0, column=0)
rc_v = StringVar()
rc = ttk.Entry(frm, state='readonly', textvariable=rc_v)
rc_v.set('X')
rc.grid(row=0, column=1)
Label(frm, text='Left Click', font='None 15 bold', bg=bg, fg='white').grid(row=1, column=0)
lc_v = StringVar()
lc = ttk.Entry(frm, state='readonly', textvariable=lc_v)
lc_v.set('Y')
lc.grid(row=1, column=1)
frm1 = Frame(win, bg=bg)
frm1.pack(pady=10, padx=5)
b1 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b1))
b1.grid(row=0, column=0)
b1.bind('<Button-3>', lambda f:leftclick(b1))
b2 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b2))
b2.grid(row=0, column=1)
b2.bind('<Button-3>', lambda f:leftclick(b2))
b3 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b3))
b3.grid(row=0, column=2)
b3.bind('<Button-3>', lambda f:leftclick(b3))
b4 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b4))
b4.grid(row=1, column=0)
b4.bind('<Button-3>', lambda f:leftclick(b4))
b5 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b5))
b5.grid(row=1, column=1)
b5.bind('<Button-3>', lambda f:leftclick(b5))
b6 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b6))
b6.grid(row=1, column=2)
b6.bind('<Button-3>', lambda f:leftclick(b6))
b7 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b7))
b7.grid(row=2, column=0)
b7.bind('<Button-3>', lambda f:leftclick(b7))
b8 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b8))
b8.grid(row=2, column=1)
b8.bind('<Button-3>', lambda f:leftclick(b8))
b9 = Button(frm1, bg='#aaaaaa', width=9, height=3, command= lambda:rightclick(b9))
b9.grid(row=2, column=2)
b9.bind('<Button-3>', lambda f:leftclick(b9))
Button(win, text='Play Again', bg='white', fg=bg, command=end).pack(pady=5)
Button(win, text='Exit', bg='white', fg=bg, command=win.destroy).pack(pady=5)
game()
win.mainloop()