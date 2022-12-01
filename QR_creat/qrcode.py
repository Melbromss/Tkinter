from tkinter import *
import pyqrcode
import png
from PIL import ImageTk,Image

def generateQRCode():
    # ! ดึงข้อมูล สรืา มาสร้าง QECODE
    link_name = n_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    # ! สร้าง QRCODE
    url = pyqrcode.creat(link)
    url.png(file_name,scale=6)
    # ! แสดง QRCODE บน GUI
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_lable=Label(image=image)
    image_lable.image=image
    canvas.create_window(200,370,window=image_lable)
    
    

display = Tk()
display.title("Creating QRCODE")
canvas = Canvas(display,width= 450,height=450)
canvas.pack()

#! ระบุชื่อโปรแกรม
app_label = Label(display,text="QRCODE Generator",font=("Arial",30,'bold'))
canvas.create_window(200,50,window=app_label) 
 
 #! ระบุชื่อพร้อม URL ของ QRCODE
n_lable = Label(display,text='QRCODE NAME')
canvas.create_window(200,100,window=n_lable) 

link_lable = Label(display,text='URL')
canvas.create_window(200,160,window=link_lable) 


#! creat box
n_entry = Entry(display)
canvas.create_window(200,130,window=n_entry)

link_entry = Entry(display)
canvas.create_window(200,180,window=link_entry)


# todo Creat QRCODE
button = Button(text='QRCODE Generate',command=generateQRCode)
canvas.create_window(200,230,window=button)


display.mainloop()