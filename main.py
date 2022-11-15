from tkinter import Tk, Frame, Button as Btn, Label, PhotoImage as Image, Canvas


def configureWindow():
    '''Creates a Tk object "window" and changes its attributes.'''
    global window
    window = Tk()
    window.title("Dodgems")
    window.geometry("1920x1080")
    window.attributes('-fullscreen', True)


def homeSwap():
    '''Swaps the displayed frame to the homepage.'''
    settingsFrame.pack_forget()
    leaderboardFrame.pack_forget()
    homeFrame.pack(fill="both", expand=True)


def settingsSwap():
    '''Swaps the displayed frame to the settings page.'''
    homeFrame.pack_forget()
    leaderboardFrame.pack_forget()
    settingsFrame.pack(fill="both", expand=True)


def leaderboardSwap():
    '''Swaps the displayed frame to the leaderboard page.'''
    homeFrame.pack_forget()
    settingsFrame.pack_forget()
    leaderboardFrame.pack(fill="both", expand=True)


def initialiseMenu():
    '''Sets up the menu functionality, including the home page, settings page, leaderboard page, and all respective titles and buttons.'''
    #Start at the home page
    homeFrame.pack(fill="both", expand=True)

    #Create all buttons
    playBtn = Btn(homeFrame, width=20, height=2, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=None)
    settingsBtn = Btn(homeFrame, width=20, height=2, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=settingsSwap)
    leaderboardBtn = Btn(homeFrame, width=20, height=2, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=leaderboardSwap)
    exitBtn = Btn(homeFrame, width=20, height=2, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=window.destroy)
    home1Btn = Btn(settingsFrame, width=20, height=2, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    home2Btn = Btn(leaderboardFrame, width=20, height=2, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)

    #Create all labels
    homeLabel = Label(homeFrame, image=logo)
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="#FFA4A2", text="SETTINGS", font=("Comic Sans MS", 20, "bold"))
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="#FFA4A2", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"))

    #Pack all labels
    homeLabel.pack(side="top", pady=(150, 0))
    settingsLabel.pack(side="top", pady=(150, 0))
    leaderboardLabel.pack(side="top", pady=(150, 0))

    #Pack all buttons
    playBtn.pack(side="top", pady=(100,0))
    settingsBtn.pack(side="top", pady=(20,0))
    leaderboardBtn.pack(side="top", pady=(20, 0))
    exitBtn.pack(side="top", pady=(20, 0))
    home1Btn.pack(side="top", pady=(500,0))
    home2Btn.pack(side="top", pady=(500, 0))


configureWindow()

homeFrame = Frame(window, bg="#FFA4A2")
settingsFrame = Frame(window, bg="#FFA4A2")
leaderboardFrame = Frame(window, bg="#FFA4A2")

logo = Image(file="Dodgems.png")

initialiseMenu()

window.mainloop()