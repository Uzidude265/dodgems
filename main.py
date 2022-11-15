from tkinter import Tk, Frame, Button as Btn

window = Tk()
window.title("Test for Frames")
window.geometry("1920x1080")

menuFrame = Frame(window, bg="green")
settingsFrame = Frame(window, bg="blue")

def menuSwap():
    settingsFrame.pack_forget()
    menuFrame.pack(fill="both", expand=1)

def settingsSwap():
    menuFrame.pack_forget()
    settingsFrame.pack(fill="both", expand=1)

def initialiseMenu():
    menuFrame.pack(fill="both", expand=1)
    playBtn = Btn(menuFrame, width=30, height=5, text="Play", command=None)
    settingsBtn = Btn(menuFrame, width=30, height=5, text="Settings", command=settingsSwap)
    homeBtn = Btn(settingsFrame, width=30, height=5, text="Home", command=menuSwap)
    playBtn.pack(side="top", pady=(350,0))
    settingsBtn.pack(side="top")
    homeBtn.pack(side="top", pady=(500,0))

initialiseMenu()

window.mainloop()