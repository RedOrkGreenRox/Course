from tkinter import *
Virus = Tk()
count = Label(text=6, fg='green', bg='black')
Virus.geometry('900x300')
Virus.title('Virus')
Virus.resizable(width=False, height=False)
Virus.config(bg='black')


def count_start():
    global label
    if count['text'] > 0:
        count['text'] -= 1
        count.place(relx=0.4, rely=0.4)
        Virus.after(1000, count_start)
    else:
        Virus.geometry(f'{Virus.winfo_screenheight()}x{Virus.winfo_screenwidth()}')
        photo = PhotoImage(file="test.jpeg")
        label = Label(image=photo, bg='black')
        label.image = photo
        label.place(height=Virus.winfo_screenheight(), width=Virus.winfo_screenwidth(), x=0, y=0)


def on_close():
    count_start()


label = Label(text='Virus Detected.', bg='black', fg='green')
label.place(relx=0.45, rely=0.5)
Virus.protocol('WM_DELETE_WINDOW', on_close)
mainloop()
