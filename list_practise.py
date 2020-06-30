from tkinter import *


marks = []
def upload():
    global marks
    lis = []
    s= edit.get()
    lis=s.split(' ')
    temp = ''
    for val in lis:
        if int(val)<10:
            marks.append(int(val))
            temp += val + " "
    text11['text'] = 'List has been aploaded' + temp

def mean():
    global marks
    mark = 0

    text2['text'] = str(mark)

def maximum():
    global marks

    text3['text'] = str(big)

def minimun():
    global marks

    text['text'] = str(small)

def ten():
    global marks


root = Tk()
root.geometry('300x250')

text1=Label(root, text='Enter words from spaces', fg='yellow')
text1.place(x=70,y=0)

but1= Button(root,text='Download', command=upload)
but1.place(x=20,y=30)

edit1 = Entry(root, width=30)
edit1.place(x=100, y=33)

text11 = Label(root, text='List does not loaded', fg='blue')
text11.place(x=40, y=60)

but2= Button(root, width=10, text='Average', command=mean)
but2.place(x=20,y=90)
text2 = Label(root, text='Average score')
text2.place(x=120, y=93)

but3 = Button(root, width=10, text='Maximum', command=maximum)
but3.place(x=20,y=120)
text3 = Label(root, text='Maximum score')
text3.place(x=120, y=123)

but4 = Button(root, width=10, text='Minimum', command=minimum)
but4.place(x=20,y=150)
text4 = Label(root, text='Minimum score')
text4.place(x=120, y=153)

but5 = Button(root, width=10, text='10', command=len)
but5.place(x=20,y=180)
text4 = Label(root, text='Quantity is 10')
text4.place(x=120, y=183)
