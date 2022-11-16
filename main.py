from tkinter import Tk, Frame, Button as Btn, Label, PhotoImage as Image, Canvas
from time import sleep
from random import randint

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
    #Create frames for each page
    global homeFrame, settingsFrame, leaderboardFrame, logo
    homeFrame = Frame(window, bg="#FFA4A2")
    settingsFrame = Frame(window, bg="#FFA4A2")
    leaderboardFrame = Frame(window, bg="#FFA4A2")

    #Start at the home page
    homeFrame.pack(fill="both", expand=True)

    #Create all buttons
    playBtn = Btn(homeFrame, width=20, height=2, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=initialiseGame)
    settingsBtn = Btn(homeFrame, width=20, height=2, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=settingsSwap)
    leaderboardBtn = Btn(homeFrame, width=20, height=2, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=leaderboardSwap)
    exitBtn = Btn(homeFrame, width=20, height=2, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=window.destroy)
    home1Btn = Btn(settingsFrame, width=20, height=2, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    home2Btn = Btn(leaderboardFrame, width=20, height=2, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)

    #Create all labels
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
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


def initialiseGame():
    '''Sets up all of the variables and conditions in order to play the game'''
    #Hide the menu and show the canvas
    homeFrame.pack_forget()
    gameCanvas = Canvas(window, width=1920, height=1080)
    gameCanvas.pack(fill="both", expand=True)

    global time, score
    time = 0
    score = 0

    gameLoop()


def gameLoop():
    '''The main game loop'''
    time = 0
    activeGame = True
    while activeGame:
        collisionDetection()
        sleep(0.005)
        time += 0.005
        window.update()


def collisionDetection():
    '''Responsible for checking collisions with the wall, between balls and the player'''
    for i in range(len(balls)):

        pos = gameCanvas.coords(balls[i])

        #Checks for collision with wall
        if pos[3] > 1080 or pos[1] < 0:
            y[i] = -y[i]
        if pos[2] > 1920 or pos[0] < 0:
            x[i] = -x[i]

        #Checks for collision with other balls
        for j in range(len(balls)):
            if i == j:
                continue
            pos2 = gameCanvas.coords(balls[j])
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]: #If the balls are touching/within each other
                y[i] = -y[i]
                x[i] = -x[i]
                y[j] = -y[i]
                x[j] = -x[j]

        gameCanvas.move(balls[i],x[i],y[i])


configureWindow()

#initialiseMenu()


gameCanvas = Canvas(window, width=1920, height=1080)
gameCanvas.pack(fill="both", expand=True)

y = 0
x = 0
numBalls = 20
balls = []

for i in range(numBalls):
    x = randint(50,1870)
    y = randint(50,1030)
    xy = (x, y, x+25, y+25)
    balls.append(gameCanvas.create_oval(xy, fill="red", outline="red"))

y = []
x = []

for i in range(len(balls)):

    tempX = randint(2,9)
    tempY = randint(2,9)

    y.append(tempY)
    x.append(tempX)

    averageSpeed = (tempX + tempY)/2

    if averageSpeed >= 7:
        gameCanvas.itemconfig(balls[i], fill="purple", outline="purple")
    elif averageSpeed >= 5:
        gameCanvas.itemconfig(balls[i], fill="purple2", outline="purple2")
    elif averageSpeed >= 3:
        gameCanvas.itemconfig(balls[i], fill="red3", outline="red3")
    else:
        gameCanvas.itemconfig(balls[i], fill="red", outline="red")

time = 0
score = 0

player = gameCanvas.create_rectangle(930, 510, 990, 570, fill="light blue", outline="light blue")

scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))

gameLoop()

window.mainloop()