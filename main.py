from tkinter import Tk, Frame, Button as Btn, Label, PhotoImage as Image, Canvas, Checkbutton as CheckBtn, ttk
from time import sleep
from random import randint

def configureWindow():
    '''Creates a Tk object "window" and changes its attributes.'''
    global window
    window = Tk()
    window.title("Dodgems")
    window.geometry("1920x1080")
    window.attributes('-fullscreen', True)

#---------------------------------------------- MENU FUNCTIONS --------------------------------------------------------------

def initialiseMenu():
    '''Sets up the menu functionality, including the home page, settings page, leaderboard page, info page, and all respective titles and buttons.'''
    #Initialise any variables used in the menu and initial settings
    global triggeredKeybindChange, keybindNum, directionBinds, bgColour, previousBind, cheatCode
    triggeredKeybindChange = False
    keybindNum = 0
    directionBinds = ["<Up>","<Down>","<Left>","<Right>"]
    bgColour = "#cbf7e6"
    previousBind = ""
    howToPlayText = "Dodge the never-ending balls as long as you can!\nThe colour of the balls indicates their speed.\n\n(Black = Slow, Blue = Medium, Purple = Fast, Red = Very Fast)\n\nEvery 3 seconds, a new ball gets added at the sides, so watch out!\nYour final score is the number of balls you ended with.\n\nGood Luck!"
    cheatCode = ""

    # Create frames for each page
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, gameOverFrame, bgFrame, keybindsFrame, cheatsFrame
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)
    bgFrame = Frame(window)
    keybindsFrame = Frame(window)
    cheatsFrame = Frame(window)

    # Create the leaderboard
    createLeaderboard()

    # Create all buttons on home frame
    playBtn = Btn(homeFrame, width=25, height=1, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=initialiseGame)
    settingsBtn = Btn(homeFrame, width=25, height=1, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    leaderboardBtn = Btn(homeFrame, width=25, height=1, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(4))
    infoBtn = Btn(homeFrame, width=25, height=1, text="How to Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(5))
    exitBtn = Btn(homeFrame, width=25, height=1, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=window.destroy)

    # Create all buttons on settings frame
    global cheatsBtn
    settingsHomeBtn = Btn(settingsFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))
    bgBtn = Btn(settingsFrame, width=25, height=1, text="Change Background Colour", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(2))
    keybindsBtn = Btn(settingsFrame, width=25, height=1, text="Change Keybinds", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(3))
    cheatsBtn = Btn(settingsFrame, width=25, height=1, text="Cheats", bg="red", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=None, relief="ridge")

    # Create all buttons on the background colour frame
    bgSettingsBtn = Btn(bgFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    greenBtn = Btn(bgFrame, width=25, height=1, text="Green", bg="#cbf7e6", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground(0))
    redBtn = Btn(bgFrame, width=25, height=1, text="Red", bg="#edd3dc", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground(1))
    blueBtn = Btn(bgFrame, width=25, height=1, text="Blue", bg="#8ec8fa", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground(2))
    yellowBtn = Btn(bgFrame, width=25, height=1, text="Yellow", bg="#fffcc2", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground(3))

    # Create all buttons on the keybind frame
    global upBtn, downBtn, leftBtn, rightBtn, keybindsSettingsBtn
    keybindsSettingsBtn = Btn(keybindsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    upBtn = Btn(keybindsFrame, width=25, height=1, text="Up: Up", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(0))
    downBtn = Btn(keybindsFrame, width=25, height=1, text="Down: Down", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(1))
    leftBtn = Btn(keybindsFrame, width=25, height=1, text="Left: Left", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(2))
    rightBtn = Btn(keybindsFrame, width=25, height=1, text="Right: Right", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(3))

    # Create all buttons on the cheats frame
    cheatsHomeBtn = Btn(cheatsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    smallerPlayerBtn = CheckBtn(cheatsFrame)

    # Create home buttons on rest of frames
    leaderboardHomeBtn = Btn(leaderboardFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))
    infoHomeBtn = Btn(infoFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))
    gameOverHomeBtn = Btn(gameOverFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # Create all labels for each frame
    global logo, keybindsPromptLabel, finalScoreLabel
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="pink", text="SETTINGS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="pink", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    infoLabel = Label(infoFrame, width=30, height=4, bg="pink", text="HOW TO PLAY", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    howToPlayLabel = Label(infoFrame, width=60, height=12, bg="pink", text=howToPlayText, font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    gameOverLabel = Label(gameOverFrame, width=30, height=4, bg="pink", text="GAME OVER!", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    finalScoreLabel = Label(gameOverFrame, width=30, height=3, bg="pink", text="", font=("Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    bgLabel = Label(bgFrame, width=30, height=4, bg="pink", text="CHANGE BACKGROUND COLOUR", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    keybindsLabel = Label(keybindsFrame, width=30, height=4, bg="pink", text="CHANGE KEYBINDS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    keybindsPromptLabel = Label(keybindsFrame, width=50, height=2, bg="pink", text="Click a keybind to change", font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    cheatsLabel = Label(cheatsFrame, width=30, height=4, bg="pink", text="CHEATS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")

    # Pack and position all labels
    homeLabel.pack(side="top", pady=(130, 0))
    settingsLabel.pack(side="top", pady=(150, 0))
    leaderboardLabel.pack(side="top", pady=(150, 0))
    infoLabel.pack(side="top", pady=(150, 0))
    howToPlayLabel.pack(side="top", pady=(50, 0))
    gameOverLabel.pack(side="top", pady=(150, 0))
    finalScoreLabel.pack(side="top", pady=(180, 0))
    bgLabel.pack(side="top", pady=(150, 0))
    keybindsLabel.pack(side="top", pady=(150, 0))
    keybindsPromptLabel.pack(side="top", pady=(30, 0))
    cheatsLabel.pack(side="top", pady=(150, 0))

    # Pack the leaderboard
    leaderboard.pack(side="top", pady=(50, 0))

    # Pack all buttons on the home frame
    playBtn.pack(side="top", pady=(120, 0))
    settingsBtn.pack(side="top", pady=(20, 0))
    leaderboardBtn.pack(side="top", pady=(20, 0))
    infoBtn.pack(side="top", pady=(20, 0))
    exitBtn.pack(side="top", pady=(20, 0))

    # Pack all buttons on the setting frame
    bgBtn.pack(side="top", pady=(130, 0))
    keybindsBtn.pack(side="top", pady=(20, 0))
    cheatsBtn.pack(side="top", pady=(20, 0))
    settingsHomeBtn.pack(side="top", pady=(170, 0))

    # Pack all buttons on the background colour frame
    greenBtn.pack(side="top", pady=(110, 0))
    redBtn.pack(side="top", pady=(20, 0))
    blueBtn.pack(side="top", pady=(20, 0))
    yellowBtn.pack(side="top", pady=(20, 0))
    bgSettingsBtn.pack(side="top", pady=(120, 0))

    # Pack all buttons on the keybind frame
    upBtn.pack(side="top", pady=(60, 0))
    downBtn.pack(side="top", pady=(20, 0))
    leftBtn.pack(side="top", pady=(20, 0))
    rightBtn.pack(side="top", pady=(20, 0))    
    keybindsSettingsBtn.pack(side="top", pady=(70, 0))

    # Pack all buttons on the cheats frame
    cheatsHomeBtn.pack(side="top", pady=(500, 0))

    # Pack rest of home buttons
    leaderboardHomeBtn.pack(side="top", pady=(60, 0))
    infoHomeBtn.pack(side="top", pady=(90, 0))
    gameOverHomeBtn.pack(side="top", pady=(200, 0))

def createLeaderboard():
    '''Uses a text file containing information to create and fill the leaderboard.'''
    global leaderboard
    style = ttk.Style()
    style.configure("Treeview", font=("Comic Sans MS", 15, "bold"), rowheight=35)
    style.configure("Treeview.Heading", font=("Comic Sans MS", 15, "bold"))
    leaderboard = ttk.Treeview(leaderboardFrame, columns=("name", "stage", "score"), show="headings")
    leaderboard.column("name", anchor="center")
    leaderboard.heading("name", text="Name")
    leaderboard.column("stage", anchor="center")
    leaderboard.heading("stage", text="Stage")
    leaderboard.column("score", anchor="center")
    leaderboard.heading("score", text="Score")
    for i in range(20):
        leaderboard.insert("", "end", iid=i, values=("Uzi", i, i))

def swapFrames(frameNum):
    '''Swaps to a frame according to the given button press.'''
    if frameNum == 0: # Swap to the home frame
        settingsFrame.pack_forget()
        leaderboardFrame.pack_forget()
        infoFrame.pack_forget()
        gameOverFrame.pack_forget()
        homeFrame.pack(fill="both", expand=True)
    elif frameNum == 1: # Swap to the settings frame
        homeFrame.pack_forget()
        bgFrame.pack_forget()
        keybindsFrame.pack_forget()
        cheatsFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)
    elif frameNum == 2: # Swap to the background colour frame
        settingsFrame.pack_forget()
        bgFrame.pack(fill="both", expand=True)
    elif frameNum == 3: # Swap to the keybinds frame
        settingsFrame.pack_forget()
        keybindsFrame.pack(fill="both", expand=True)
    elif frameNum == 4: # Swap to the leaderboard frame
        homeFrame.pack_forget()
        leaderboardFrame.pack(fill="both", expand=True)
    elif frameNum == 5: # Swap to the info frame
        homeFrame.pack_forget()
        infoFrame.pack(fill="both", expand=True)
    elif frameNum == 6: # Swap to the game over frame
        gameCanvas.pack_forget()
        gameOverFrame.pack(fill="both", expand=True)
    else: # Swap to the cheats frame
        settingsFrame.pack_forget()
        cheatsFrame.pack(fill="both", expand=True)

#---------------------------------------------- SETTINGS FUNCTIONS --------------------------------------------------------------------

def updateSettings(updateType):
    '''Update the settings such as key binds and background colour.'''
    # Update colours of pages
    if updateType == 0 or updateType == 2:
        homeFrame.config(bg=bgColour)
        settingsFrame.config(bg=bgColour)
        leaderboardFrame.config(bg=bgColour)
        infoFrame.config(bg=bgColour)
        gameOverFrame.config(bg=bgColour)
        bgFrame.config(bg=bgColour)
        keybindsFrame.config(bg=bgColour)
        cheatsFrame.config(bg=bgColour)

    # Update button text if they updated keybind and update the bind
    elif updateType == 1:
        global upBtn, downBtn, leftBtn, rightBtn, directionBinds, keybindNum, previousBind
        window.unbind(previousBind)
        tempText = directionBinds[keybindNum]
        tempText = tempText[1:len(tempText)-1] # Get rid of < >
        if keybindNum == 0:
            upBtn.config(text="Up: " + tempText)
            window.bind(directionBinds[keybindNum], upDirection)
        elif keybindNum == 1:
            downBtn.config(text="Down: " + tempText)
            window.bind(directionBinds[keybindNum], downDirection)
        elif keybindNum == 2:
            leftBtn.config(text="Left: " + tempText)
            window.bind(directionBinds[keybindNum], leftDirection)
        else:
            rightBtn.config(text="Right: " + tempText)
            window.bind(directionBinds[keybindNum], rightDirection)
    
    # If initialising settings, bind the keys
    if updateType == 2:
        window.bind(directionBinds[0], upDirection)
        window.bind(directionBinds[1], downDirection)
        window.bind(directionBinds[2], leftDirection)
        window.bind(directionBinds[3], rightDirection)
        window.bind("<BackSpace>", cancelCheatCode)
        window.bind("<Escape>", pause)
        window.bind("<Key>", updateKeybind)

def changeBackground(bgNum):
    '''Changes the colour of the backgrounds according to user input'''
    global bgColour
    if bgNum == 0:
        bgColour = "#cbf7e6"
    elif bgNum == 1:
        bgColour = "#edd3dc"
    elif bgNum == 2:
        bgColour = "#8ec8fa"
    else:
        bgColour = "#fffcc2"
    updateSettings(0) # Update settings to confirm change

def setKeybindChange(tempNum):
    '''Sets the boolean state to true so that the player can then press the key and update their keybind.'''
    global triggeredKeybindChange, keybindNum, keybindsSettingsBtn
    keybindsPromptLabel.config(text="Press the key you want to bind:")
    triggeredKeybindChange = True
    keybindNum = tempNum
    keybindsSettingsBtn.config(text="Cancel", command=cancelKeybindChange) # Change button to a cancel button

def updateKeybind(event):
    '''Updates the keybind as long as they intended to, else adds the keypress to the cheat code buffer.'''
    global directionBinds, triggeredKeybindChange, keybindsPromptLabel, previousBind, keybindsSettingsBtn
    # Only update if they pressed a button beforehand
    if triggeredKeybindChange == True:
        previousBind = directionBinds[keybindNum] # Remember previous bind to unbind later
        directionBinds[keybindNum] = "<" + event.keysym + ">" # Store as correct key format
        triggeredKeybindChange = False # Reset variables
        keybindsPromptLabel.config(text="Click a keybind to change")
        keybindsSettingsBtn.config(text="Back to Settings", command=lambda:swapFrames(1)) # Change button back to normal
        updateSettings(1) # Update settings to confirm change
    else:
        updateCheatCode(event.keysym) # Add keypress to cheat code

def cancelKeybindChange():
    '''Used if the user decides not to bind a key after clicking a button.'''
    global triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    triggeredKeybindChange = False #Reset variables
    keybindsPromptLabel.config(text="Click a keybind to change")
    keybindsSettingsBtn.config(text="Back to Settings", command=lambda:swapFrames(1)) # Change button back to normal

#---------------------------------------------- CHEAT CODE FUNCTIONS -----------------------------------------------------------------------

def cancelCheatCode(event):
    '''Resets the cheat code for misinputs.'''
    global cheatCode
    cheatCode = ""
 
def updateCheatCode(keyName):
    '''Updates the cheat code and then checks if the player has inputted it correctly.'''
    global cheatCode, cheatsBtn
    cheatCode += keyName
    if cheatCode == "unlockcheats":
        cheatsBtn.config(command=lambda:swapFrames(7), relief="raised", bg="light blue")

#---------------------------------------------- GAME FUNCTIONS -----------------------------------------------------------------------

def initialiseGame():
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop.'''
    # Hide the menu and create the game canvas
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameCanvas.pack(fill="both", expand=True)

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, xDirection, yDirection, paused, player, scoreText, countdownText, pausedBackground, pausedText, bossImage
    time = 0
    score = 0
    numBalls = 0
    balls = []
    xSpeed = []
    ySpeed = []
    xDirection = 7
    yDirection = 0
    paused = False
    player = gameCanvas.create_rectangle(930, 510, 990, 570, fill="light blue", outline="black")
    scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    countdownText = gameCanvas.create_text(960, 540, text="3", font=("Comic Sans MS", 75, "bold"), state="normal")
    pausedBackground = gameCanvas.create_rectangle(850, 480, 100, 600, fill="pink", outline="black", state="hidden")
    pausedText = gameCanvas.create_text(960, 540, text="PAUSED\nPress Esc to resume.", font=("Comic Sans MS", 75, "bold"), state="hidden")
    #bossImage = gameCanvas.create_image()

    # Start with 1 ball
    createBall()
    
    # Start the countdown, then start the game
    countdown()
    gameLoop()

def countdown():
    '''Short countdown before the game starts'''
    global countdownText
    for i in range(3, 0, -1):
        gameCanvas.itemconfig(countdownText, text=str(i))
        window.update()
        sleep(1)
    gameCanvas.itemconfig(countdownText, text="Go!")
    window.update()
    sleep(1)
    gameCanvas.itemconfig(countdownText, state="hidden")

def gameLoop():
    '''The main game loop that repeats until the game ends, then switches to the game over screen.'''
    # Keep track of if the game should loop again
    global activeGame, time, score, paused
    activeGame = True

    # Keep looping until player is hit
    while activeGame:
        gameCanvas.move(player, xDirection, yDirection)
        moveBalls()
        checkPlayerCrash()
        sleep(0.005)
        time += 0.005
        score += 0.02
        displayScore = int(score)
        gameCanvas.itemconfig(scoreText, text="Score: " + str(displayScore))
        if time > 1:
            createBall()
            time = 0
        #while paused:
        #    sleep(0.01)
        window.update()

    # Go to game over screen once game is finished
    score = int(score)
    finalScoreLabel.config(text="You scored " + str(score) + " points!")
    swapFrames(6)

def pause(event):
    global paused
    if paused:
        paused = False
        gameCanvas.itemconfig(pausedBackground, state="hidden")
        gameCanvas.itemconfig(pausedText, state="hidden")
    else:
        paused = True
        gameCanvas.itemconfig(pausedBackground, state="normal")
        gameCanvas.itemconfig(pausedText, state="normal")
    print(paused)

#def bossKey():
#    pause()

#---------------------------------------------- BALL FUNCTIONS -----------------------------------------------------------------------

def createBall():
    '''Creates a new ball and appends it to an array, along with its corresponding x and y speed and colour.'''
    # Choose starting point for ball
    side = randint(0,3) # Choose a side to start at
    if side == 0: # Up
        xPos = randint(50,1870)
        yPos = 10
    elif side == 1: # Down
        xPos = randint(50,1870)
        yPos = 1040
    elif side == 2: # Left
        xPos = 10
        yPos = randint(50,1030)
    else: # Right
        xPos = 1880
        yPos = randint(50,1030)

    # Create ball
    xy = (xPos, yPos, xPos+20, yPos+20)
    balls.append(gameCanvas.create_oval(xy, fill="#ff0000"))

    # Generate speed values for ball
    tempX = randint(2,10) # Get random speed values for x and y
    tempY = randint(2,10)
    xSign = randint(0,1) # Determine direction (positive or negative speed)
    ySign = randint(0,1)
    if xSign == 0:
        tempX = -tempX # Make direction Left (-x), else Right
    if ySign == 0:
        tempY = -tempY # Make direction Up (-y), else Down
    xSpeed.append(tempX)
    ySpeed.append(tempY)

    # Determine colour of ball based on speed (Black < Blue < Purple < Red)
    averageSpeed = (abs(tempX) + abs(tempY))/2
    global numBalls
    if averageSpeed >= 8:
        gameCanvas.itemconfig(balls[numBalls], fill="#ff0000", outline="black")
    elif averageSpeed >= 7:
        gameCanvas.itemconfig(balls[numBalls], fill="#d303fc", outline="black")
    elif averageSpeed >= 5:
        gameCanvas.itemconfig(balls[numBalls], fill="blue", outline="black")
    else:
        gameCanvas.itemconfig(balls[numBalls], fill="black", outline="black")
    
    # Increment number of balls
    numBalls += 1
    #gameCanvas.itemconfig(scoreText, text="Score: " + str(numBalls)) <-- REENABLE AFTER TESTING TIMING

def moveBalls():
    '''Responsible for checking collisions with the wall, between balls and the player, and moving each ball.'''
    # Check every ball
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

        # Move ball using its speed values
        gameCanvas.move(balls[i], xSpeed[i], ySpeed[i])

#---------------------------------------------- PLAYER DIRECTION FUNCTIONS ----------------------------------------------------

def upDirection(event):
    '''Change the player's direction to up.'''
    global xDirection, yDirection
    xDirection = 0
    yDirection = -7

def downDirection(event):
    '''Change the player's direction to down.'''
    global xDirection, yDirection
    xDirection = 0
    yDirection = 7

def leftDirection(event):
    '''Change the player's direction to left.'''
    global xDirection, yDirection
    xDirection = -7
    yDirection = 0

def rightDirection(event):
    '''Change the player's direction to right.'''
    global xDirection, yDirection
    xDirection = 7
    yDirection = 0

#---------------------------------------------- END GAME FUNCTIONS --------------------------------------------------------

def checkPlayerCrash():
    '''Checks if the player is touching a ball or has collided with the wall, if so it ends the game.'''
    global activeGame

    # Check if player has collided with wall
    pos = gameCanvas.coords(player)
    if pos[3] > 1080 or pos[1] < 0 or pos[2] > 1920 or pos[0] < 0:
        activeGame = False

    # Check if player has collided with any ball
    for i in range(len(balls)):
        pos2 = gameCanvas.coords(balls[i])
        if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]: # Need to check if either side of player has collided
            activeGame = False

#---------------------------------------------- MAIN PROGRAM --------------------------------------------------------

configureWindow() # Set up the window
initialiseMenu() # Set up the menu
updateSettings(2) # Use first time settings
homeFrame.pack(fill="both", expand=True) # Start at the home page

window.mainloop()