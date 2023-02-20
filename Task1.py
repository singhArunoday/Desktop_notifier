#Task: Desktop Notifier

from plyer import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time


root = Tk()
root.title('Sync Interns Task 1')
root.geometry("500x300")
root.iconbitmap("notification_icon.ico")
img = Image.open("notification_img.png")
tkimage = ImageTk.PhotoImage(img)


def get_details():
    get_title = title.get()
    get_msg = msg.get()    
    get_time = time1.get()

    

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(get_time)
        # sec_timer = int_time * 60
        sec_timer = int_time 
        messagebox.showinfo("Notification Set", "Successfully, Notification Set")
        root.destroy()
        time.sleep(sec_timer)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="notification_icon.ico",
                            toast=True,
                            timeout=10)

img_label = Label(root, image=tkimage).grid()

t_label = Label(root, text="Notification Title",font=("Comicsansms", 10))
t_label.place(x=12, y=70)


title = Entry(root, width="25",font=("Comicsansms", 13))
title.place(x=123, y=70)


m_label = Label(root, text="Display Message", font=("Comicsansms", 10))
m_label.place(x=12, y=120)


msg = Entry(root, width="40", font=("Comicsansms", 13))
msg.place(x=123,height=30, y=120)


time_label = Label(root, text="Set Time", font=("Comicsansms", 10))
time_label.place(x=12, y=175)

time1 = Entry(root, width="5", font=("Comicsansms", 13))
time1.place(x=123, y=175)

time_min_label = Label(root, text="sec", font=("Comicsansms", 10))
time_min_label.place(x=175, y=180)


but = Button(root, text="SET NOTIFICATION", font=("Comicsansms", 10, "bold"), fg="black", bg="white", width=20,
             relief="groove",
             command=get_details)
but.place(x=170, y=230)

root.mainloop()
