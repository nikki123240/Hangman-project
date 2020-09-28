def hangman():
    global ss, ll, ss1, n, ffdata, temps,first
    first = textinput.get()
    input1.delete(0,END)
    if (n>0):
        if (first in ss):
            for i in range(ss1):
                if (ss[i] == first and ll[i] == '*'):
                    ll.pop(i)
                    ll.insert(i,ss[i])
                    xx = ''.join(ll)
                    ss = list(ss)
                    ss.pop(i)
                    ss.insert(i,"*")
                    wordlabel.configure(text=xx)
                    if (xx==temps):
                        ans.configure(text = 'congratulation you won the game....')
                        res = messagebox.askyesno("notification","congratulation you won the game....\n want to play again")
                        if (res==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n -= 1
            leftlabel.configure(text="left = {}".format(n))
    if(n<=0):
          ans.configure(text="oops,you lost the game....")
          res = messagebox.askyesno("notification", "you lost the game.\n want to play again")
          if (res == True):
              chooseword()
          else:
              root.destroy()

def ffl(event):
    hangman()

from tkinter import *
import random
from tkinter import messagebox

wordlist = ['python','javascript','perl','java']


root = Tk()
root.geometry("750x500")
root.configure(bg='yellow')
root.iconbitmap('hangman.ico')
root.title("Hangman game")

introlabel = Label(root,text="Welcome to Hangman Game.....",font="arial 20 bold",fg="blue",bg="light blue")
introlabel.pack()

leftlabel = Label(root,text="Left=4",font="arial 23 bold",fg="blue",bg="yellow")
leftlabel.place(y=70,x=600)

ans = Label(root,text="You Won....",font="arial 20 bold",fg="blue",bg="yellow",pady=15)
ans.pack(side=BOTTOM,anchor=CENTER)

wordlabel = Label(root,text="****",font="arial 40 bold",fg="blue",bg="yellow",pady=60)
wordlabel.pack()

textinput = StringVar()
input1 = Entry(root,font="arial 20 bold",fg="blue",relief=SUNKEN,bd=6,justify=CENTER,bg="light goldenrod",textvariable=textinput)
input1.focus_set()
input1.pack()

btn = Button(root,text="Submit",font="arial 15 bold",fg="black",bg="DarkGoldenrod3",pady=15,padx=15,bd=5,
             activebackground="salmon4",activeforeground="white")
btn.place(y=300,x=330)
root.bind("<Return>",ffl)

def chooseword():
    global ss,ll,ss1,n,ffdata,temps
    ss = random.choice(wordlist)
    ll = ["*" for i in ss]
    ss1 = len(ss)
    n = ss1
    temps = ss
    leftlabel.configure(text='Left = {}'.format(n))
    ffdata = ''
    for i in ll:
        ffdata += i+ ' '
    wordlabel.configure(text=ffdata)
    ans.configure(text='')

chooseword()
root.mainloop()