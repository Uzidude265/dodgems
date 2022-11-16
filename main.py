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
    infoFrame.pack_forget()
    homeFrame.pack(fill="both", expand=True)

def settingsSwap():
    '''Swaps the displayed frame to the settings page.'''
    homeFrame.pack_forget()
    settingsFrame.pack(fill="both", expand=True)

def leaderboardSwap():
    '''Swaps the displayed frame to the leaderboard page.'''
    homeFrame.pack_forget()
    leaderboardFrame.pack(fill="both", expand=True)

def infoSwap():
    '''Swaps the displayed frame to the info page'''
    homeFrame.pack_forget()
    infoFrame.pack(fill="both", expand=True)

def initialiseMenu():
    '''Sets up the menu functionality, including the home page, settings page, leaderboard page, info page, and all respective titles and buttons.'''
    #Create frames for each page
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, logo
    homeFrame = Frame(window, bg="#cbf7e6")
    settingsFrame = Frame(window, bg="#cbf7e6")
    leaderboardFrame = Frame(window, bg="#cbf7e6")
    infoFrame = Frame(window, bg="#cbf7e6")

    #Start at the home page
    homeFrame.pack(fill="both", expand=True)

    #Create all buttons
    playBtn = Btn(homeFrame, width=20, height=1, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=initialiseGame)
    settingsBtn = Btn(homeFrame, width=20, height=1, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=settingsSwap)
    leaderboardBtn = Btn(homeFrame, width=20, height=1, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=leaderboardSwap)
    infoBtn = Btn(homeFrame, width=20, height=1, text="How to Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=infoSwap)
    exitBtn = Btn(homeFrame, width=20, height=1, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=window.destroy)
    settingsHomeBtn = Btn(settingsFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    leaderboardHomeBtn = Btn(leaderboardFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    infoHomeBtn = Btn(infoFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)

    #Create all labels
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="#cbf7e6", text="SETTINGS", font=("Comic Sans MS", 20, "bold"))
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="#cbf7e6", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"))
    infoLabel = Label(infoFrame, width=30, height=4, bg="#cbf7e6", text="HOW TO PLAY", font=("Comic Sans MS", 20, "bold"))

    #Pack all labels
    homeLabel.pack(side="top", pady=(150, 0))
    settingsLabel.pack(side="top", pady=(150, 0))
    leaderboardLabel.pack(side="top", pady=(150, 0))
    infoLabel.pack(side="top", pady=(150, 0))

    #Pack all buttons
    playBtn.pack(side="top", pady=(100, 0))
    settingsBtn.pack(side="top", pady=(20, 0))
    leaderboardBtn.pack(side="top", pady=(20, 0))
    infoBtn.pack(side="top", pady=(20, 0))
    exitBtn.pack(side="top", pady=(20, 0))
    settingsHomeBtn.pack(side="top", pady=(500, 0))
    leaderboardHomeBtn.pack(side="top", pady=(500, 0))
    infoHomeBtn.pack(side="top", pady=(500, 0))

def initialiseGame():
    '''Sets up all of the variables and conditions in order to play the game'''
    #Hide the menu and create the game canvas
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg="#cbf7e6")
    gameCanvas.pack(fill="both", expand=True)

    #Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, player, scoreText
    time = 0
    score = 0
    numBalls = 0
    balls = []
    xSpeed = []
    ySpeed = []
    player = gameCanvas.create_rectangle(930, 510, 990, 570, fill="light blue", outline="light blue")
    scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))

    #Start with 1 ball
    createBall()
    gameLoop()

def gameLoop():
    '''The main game loop that repeats until the game ends'''
    time = 0
    activeGame = True

    #Keep looping until player is hit
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
            ySpeed[i] = -ySpeed[i]
        if pos[2] > 1920 or pos[0] < 0:
            xSpeed[i] = -xSpeed[i]

        #Checks for collision with other balls
        for j in range(len(balls)):
            if i == j: #Skip if comparing same ball
                continue
            pos2 = gameCanvas.coords(balls[j])
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]: #If the balls are touching/within each other
                ySpeed[i] = -ySpeed[i]
                xSpeed[i] = -xSpeed[i]
                ySpeed[j] = -ySpeed[j]
                xSpeed[j] = -xSpeed[j]

        gameCanvas.move(balls[i], xSpeed[i], ySpeed[i])

def createBall():
    '''Creates a new ball and appends it to an array, along with its corresponding x and y speed and colour'''
    #Create ball at random point
    x = randint(50,1870)
    y = randint(50,1030)
    xy = (x, y, x+20, y+20)
    balls.append(gameCanvas.create_oval(xy, fill="#ff0000"))

    #Randomise speed of ball
    tempX = randint(2,10)
    tempY = randint(2,10)
    xSpeed.append(tempX)
    ySpeed.append(tempY)

    #Determine colour of ball based on speed
    averageSpeed = (tempX + tempY)/2
    global numBalls
    if averageSpeed >= 8:
        gameCanvas.itemconfig(balls[numBalls], fill="#ff0000", outline="#000000")
    elif averageSpeed >= 7:
        gameCanvas.itemconfig(balls[numBalls], fill="#f202da", outline="#000000")
    elif averageSpeed >= 5:
        gameCanvas.itemconfig(balls[numBalls], fill="#ae16cc", outline="#000000")
    else:
        gameCanvas.itemconfig(balls[numBalls], fill="#411466", outline="#000000")
    
    #Increment number of balls
    numBalls += 1

configureWindow()
initialiseMenu()
initialiseGame()

window.mainloop()