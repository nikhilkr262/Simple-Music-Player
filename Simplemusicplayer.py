def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()

def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)

def stopmusic():
    mixer.music.stop()

def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)

def createwidthes():
    #########################  Labels
    Tracklabel = Label(root,text="Select Audio Track :",bg='pink',font=('arial',18,'italic bold'))
    Tracklabel.grid(row=0,column=0,padx=20,pady=20)
    #############################################################################  Entry Box
    TracklabelEntry = Entry(root,font=('arial',18,'italic bold'),width=35,textvariable=audiotrack)
    TracklabelEntry.grid(row=0,column=1,padx=20,pady=20)

    #####################################################Buttons
    BrouseButton = Button(root,text='Search',width=20,bg='cyan2',font=('arial',13,'italic bold'),bd=5,
                          activebackground='orange',command=musicurl)
    BrouseButton.grid(row=0,column=3,padx=20,pady=20)

    PlayButton = Button(root, text='PLAY', width=15, bg='green2', font=('arial', 13, 'italic bold'), bd=5,
                          activebackground='light grey',command=playmusic)
    PlayButton.grid(row=1,column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text='Pause', width=15, bg='skyblue', font=('arial', 13, 'italic bold'), bd=5,
                          activebackground='light grey',command=pausemusic)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    root.ResumeButton = Button(root, text='Resume', width=15, bg='skyblue', font=('arial', 13, 'italic bold'), bd=5,
                         activebackground='light grey',command=resumemusic)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    root.mutebutton = Button(root,text='Mute',width=10,bg='light green',activebackground='purple4',
                             bd=5,command=mutemusic)
    root.mutebutton.grid(row=3,column=3)

    root.unmutebutton = Button(root, text='Unmute', width=10, bg='light green', activebackground='purple4',
                               bd=5,command=unmutemusic)
    root.unmutebutton.grid(row=3, column=3)
    root.unmutebutton.grid_remove()

    StopButton = Button(root, text='STOP', width=15, bg='orange', font=('arial', 13, 'italic bold'), bd=5,
                          activebackground='cyan2',command=stopmusic)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumeupButton = Button(root, text='VOL🔊  ++', width=20, bg='medium sea green', font=('arial', 13, 'italic bold'), bd=5,
                          activebackground='light grey',command=volumeup)
    VolumeupButton.grid(row=1, column=3, padx=20, pady=20)

    VolumedownButton = Button(root, text='VOL🔊  --', width=20, bg='dark sea green', font=('arial', 13, 'italic bold'), bd=5,
                          activebackground='light grey',command=volumedown)
    VolumedownButton.grid(row=2, column=3, padx=20, pady=20)




###########################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
root = Tk()
root.geometry('1100x500+120+50')
root.title('Simple Music Player')
#root.iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='pink')

###################################################################### global variables
audiotrack = StringVar()
currentvol = 0
################################################################### Create Slider
ss = 'Develop by Nikhil Kumar'
count = 0
text = ''
Sliderlabel = Label(root,text=ss,bg='pink',font=('arial',30,'italic bold'))
Sliderlabel.grid(row=3,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        Sliderlabel.configure(text=text)
    else:
        text = text+ss[count]
        Sliderlabel.configure(text=text)
    count += 1
    Sliderlabel.after(200,IntroLabelTick)
IntroLabelTick()
mixer.init()
createwidthes()
root.mainloop()
