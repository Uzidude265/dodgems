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
    gameOverFrame.pack_forget()
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

def gameOverSwap():
    '''Swaps the displayed frame to the game over page'''
    gameCanvas.pack_forget()
    gameOverFrame.pack(fill="both", expand=True)

def initialiseMenu():
    '''Sets up the menu functionality, including the home page, settings page, leaderboard page, info page, and all respective titles and buttons.'''
    # Create frames for each page
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, gameOverFrame, logo
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)

    # Create all buttons
    playBtn = Btn(homeFrame, width=20, height=1, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=initialiseGame)
    settingsBtn = Btn(homeFrame, width=20, height=1, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=settingsSwap)
    leaderboardBtn = Btn(homeFrame, width=20, height=1, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=leaderboardSwap)
    infoBtn = Btn(homeFrame, width=20, height=1, text="How to Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=infoSwap)
    exitBtn = Btn(homeFrame, width=20, height=1, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=window.destroy)
    settingsHomeBtn = Btn(settingsFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    leaderboardHomeBtn = Btn(leaderboardFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    infoHomeBtn = Btn(infoFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)
    gameOverHomeBtn = Btn(gameOverFrame, width=20, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=homeSwap)

    # Create all labels
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="#cbf7e6", text="SETTINGS", font=("Comic Sans MS", 20, "bold"))
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="#cbf7e6", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"))
    infoLabel = Label(infoFrame, width=30, height=4, bg="#cbf7e6", text="HOW TO PLAY", font=("Comic Sans MS", 20, "bold"))
    gameOverLabel = Label(gameOverFrame, width=30, height=4, bg="#cbf7e6", text="GAME OVER!", font=("Comic Sans MS", 20, "bold"))

    # Pack all labels
    homeLabel.pack(side="top", pady=(150, 0))
    settingsLabel.pack(side="top", pady=(150, 0))
    leaderboardLabel.pack(side="top", pady=(150, 0))
    infoLabel.pack(side="top", pady=(150, 0))
    gameOverLabel.pack(side="top", pady=(150, 0))

    # Pack all buttons
    playBtn.pack(side="top", pady=(100, 0))
    settingsBtn.pack(side="top", pady=(20, 0))
    leaderboardBtn.pack(side="top", pady=(20, 0))
    infoBtn.pack(side="top", pady=(20, 0))
    exitBtn.pack(side="top", pady=(20, 0))
    settingsHomeBtn.pack(side="top", pady=(500, 0))
    leaderboardHomeBtn.pack(side="top", pady=(500, 0))
    infoHomeBtn.pack(side="top", pady=(500, 0))
    gameOverHomeBtn.pack(side="top", pady=(500, 0))

def updateSettings():
    '''Update the settings such as key binds and background colour'''
    # Set directions and background colour according to user input or first time setup
    global directionBinds, bgColour
    directionBinds = ["Up","Down","Left","Right"]
    bgColour = "#cbf7e6"

    # Update colours of pages
    homeFrame.config(bg=bgColour)
    settingsFrame.config(bg=bgColour)
    leaderboardFrame.config(bg=bgColour)
    infoFrame.config(bg=bgColour)
    gameOverFrame.config(bg=bgColour)

def initialiseGame():
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop'''
    # Hide the menu and create the game canvas
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameCanvas.pack(fill="both", expand=True)

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, xDirection, yDirection, player, scoreText
    time = 0
    score = 0
    numBalls = 0
    balls = []
    xSpeed = []
    ySpeed = []
    xDirection = 7
    yDirection = 0
    player = gameCanvas.create_rectangle(930, 510, 990, 570, fill="light blue", outline="black")
    scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))

    # Start with 1 ball
    for i in range(5):
        createBall()
    gameLoop()

def gameLoop():
    '''The main game loop that repeats until the game ends, then switches to the game over screen.'''
    # Keep track of if the game should loop again
    global activeGame, time
    activeGame = True

    # Keep looping until player is hit
    while activeGame:
        gameCanvas.move(player, xDirection, yDirection)
        moveBalls()
        checkPlayerCrash()
        sleep(0.005)
        time += 0.005
        window.update()
    
    # Go to game over screen once game is finished
    gameOverSwap()

def moveBalls():
    '''Responsible for checking collisions with the wall, between balls and the player, and moving each ball'''
    for i in range(len(balls)):

        # Get coordinates of the ball
        pos = gameCanvas.coords(balls[i])

        # Check the ball for collision with wall
        if pos[3] > 1080 or pos[1] < 0:
            ySpeed[i] = -ySpeed[i]
        if pos[2] > 1920 or pos[0] < 0:
            xSpeed[i] = -xSpeed[i]

        # Check the ball for collision with other balls
        for j in range(len(balls)):
            if i == j: # Skip if you are comparing the same ball
                continue
            pos2 = gameCanvas.coords(balls[j]) # Get coordinates of the second ball
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]: # If the balls are touching/within each other invert their directions
                ySpeed[i] = -ySpeed[i]
                xSpeed[i] = -xSpeed[i]
                ySpeed[j] = -ySpeed[j]
                xSpeed[j] = -xSpeed[j]

        gameCanvas.move(balls[i], xSpeed[i], ySpeed[i])

def createBall():
    '''Creates a new ball and appends it to an array, along with its corresponding x and y speed and colour'''
    # Create ball at random point
    xPos = randint(50,1870)
    yPos = randint(50,1030)
    xy = (xPos, yPos, xPos+20, yPos+20)
    balls.append(gameCanvas.create_oval(xy, fill="#ff0000"))

    # Randomise speed of ball
    tempX = randint(2,10)
    tempY = randint(2,10)
    xSpeed.append(tempX)
    ySpeed.append(tempY)

    # Determine colour of ball based on speed
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
    
    # Increment number of balls
    numBalls += 1

def changeDirection(event):
    '''Changed the x and y direction of the player according to what button they press'''
    global xDirection, yDirection
    if event.keysym == directionBinds[0]:
        xDirection = 0
        yDirection = -7
    elif event.keysym == directionBinds[1]:
        xDirection = 0
        yDirection = 7
    elif event.keysym == directionBinds[2]:
        xDirection = -7
        yDirection = 0
    elif event.keysym == directionBinds[3]:
        xDirection = 7
        yDirection = 0

def checkPlayerCrash():
    '''Checks if the player is touching a ball or has collided with the wall, if so it ends the game'''
    global activeGame

    # Check if player has collided with wall
    pos = gameCanvas.coords(player)
    if pos[3] > 1080 or pos[1] < 0 or pos[2] > 1920 or pos[0] < 0:
        activeGame = False

    # Check if player has collided with any ball
    for i in range(len(balls)):
        pos2 = gameCanvas.coords(balls[i])
        if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]: # Need to check if either side has collided
            activeGame = False


configureWindow() # Set up the window
initialiseMenu() # Set up the menu
updateSettings() # Use first time settings

# Start at the home page
homeFrame.pack(fill="both", expand=True)

#Whenever key press is detected, change direction of player
window.bind("<Key>", changeDirection)

window.mainloop()