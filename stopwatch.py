import tkinter
from datetime import datetime

counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 666000:
                display ='Starting...'
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strfrime('%H:%M:%S')
                display = string
            label['text']=display
            label.after(1000, count)
            counter += 1
    count()
    
def start(label):
    global running
    running = True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    
def stop():
    global running
    startp['state'] = 'normal'
    stop['state']= 'disabled'
    reset['state'] = 'normal'
    running = False

def reset(label):
    global counter
    counter = 66600
    if running == False:
        reset['state'] = 'disabled'
        label['text']='Welcome!'
    else:
        label['text'] = 'Starting ... '

root = tkinter.Tk()
root.title('Stopwatch')
root.minsize(width=250, height=70)
label=tkinter.Label(root, text='Welcome!', fg='black',
                    font='Veranda 30 bold')
label.pack()
f = tkinter.Frame(root)
start = tkinter.Button(f, text='Start', width=6, command=lambda:start)
stop = tkinter.Button(f, text='Stop',width=6, state='disabled', command=stop)
reset = tkinter.Button(f, text='Reset', width=6, state='disabled',command=lambda:Reset(label))

f.pack(anchor = 'center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()

                
