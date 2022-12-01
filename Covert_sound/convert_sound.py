from tkinter import *
from gtts import gTTS

def convertTosound():
    word =text_entry.get()
    language = 'th','en'
    show = gTTS(text=word,lang=language,slow=False)
    show.save('sound.mp3')

display=Tk()
canvas = Canvas(display,width=400,height=300)
canvas.pack()

app_label =Label(text="Convert from text to sound",font=('Arial',20,'bold'))
canvas.create_window(200,130,window=app_label)

text_entry=Entry(display)
canvas.create_window(200,180,window=text_entry)

button = Button(text="Convert",command=convertTosound)
canvas.create_window(200,230,window=button)




display.mainloop()