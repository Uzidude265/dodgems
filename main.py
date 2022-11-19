from tkinter import Tk, Frame, Button as Btn, Label, PhotoImage as Image, Canvas, Checkbutton as CheckBtn, ttk, Entry
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

    #Set up all settings
    initialiseSettings()

    # FRAMES
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, gameOverFrame, bgFrame, keybindsFrame, cheatsFrame, bossFrame
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)
    bgFrame = Frame(window)
    keybindsFrame = Frame(window)
    cheatsFrame = Frame(window)
    bossFrame = Frame(window)

    # HOME FRAME WIDGETS
    global logo
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    playBtn = Btn(homeFrame, width=25, height=1, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=initialiseGame)
    settingsBtn = Btn(homeFrame, width=25, height=1, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    leaderboardBtn = Btn(homeFrame, width=25, height=1, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(4))
    infoBtn = Btn(homeFrame, width=25, height=1, text="How to Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(5))
    exitBtn = Btn(homeFrame, width=25, height=1, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=exitGame)

    # HOME FRAME PACKING
    homeLabel.pack(side="top", pady=(130, 0))
    playBtn.pack(side="top", pady=(120, 0))
    settingsBtn.pack(side="top", pady=(20, 0))
    leaderboardBtn.pack(side="top", pady=(20, 0))
    infoBtn.pack(side="top", pady=(20, 0))
    exitBtn.pack(side="top", pady=(20, 0))

    # SETTINGS FRAME WIDGETS
    global cheatsBtn
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="pink", text="SETTINGS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    bgBtn = Btn(settingsFrame, width=25, height=1, text="Change Background Colour", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(2))
    keybindsBtn = Btn(settingsFrame, width=25, height=1, text="Change Keybinds", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(3))
    cheatsBtn = Btn(settingsFrame, width=25, height=1, text="Cheats", bg="red", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=None)
    settingsHomeBtn = Btn(settingsFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # SETTINGS FRAME PACKING
    settingsLabel.pack(side="top", pady=(150, 0))
    bgBtn.pack(side="top", pady=(130, 0))
    keybindsBtn.pack(side="top", pady=(20, 0))
    cheatsBtn.pack(side="top", pady=(20, 0))
    settingsHomeBtn.pack(side="top", pady=(170, 0))

    # BACKGROUND COLOUR FRAME
    bgLabel = Label(bgFrame, width=30, height=4, bg="pink", text="CHANGE BACKGROUND COLOUR", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    greenBtn = Btn(bgFrame, width=25, height=1, text="Green", bg="#cbf7e6", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground("#cbf7e6"))
    redBtn = Btn(bgFrame, width=25, height=1, text="Red", bg="#edd3dc", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground("#edd3dc"))
    blueBtn = Btn(bgFrame, width=25, height=1, text="Blue", bg="#8ec8fa", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground("#8ec8fa"))
    yellowBtn = Btn(bgFrame, width=25, height=1, text="Yellow", bg="#fffcc2", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:changeBackground("#fffcc2"))
    bgSettingsBtn = Btn(bgFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))

    # BACKGROUND COLOUR PACKING
    bgLabel.pack(side="top", pady=(150, 0))
    greenBtn.pack(side="top", pady=(110, 0))
    redBtn.pack(side="top", pady=(20, 0))
    blueBtn.pack(side="top", pady=(20, 0))
    yellowBtn.pack(side="top", pady=(20, 0))
    bgSettingsBtn.pack(side="top", pady=(120, 0))

    # KEYBIND FRAME WIDGETS
    global upBtn, downBtn, leftBtn, rightBtn, keybindsSettingsBtn, keybindsPromptLabel
    tempUp = controls[0] # Remove the < > from the controls to add to the corresponding button's text
    tempUp = tempUp[1:len(tempUp)-1]
    tempDown = controls[1]
    tempDown = tempDown[1:len(tempDown)-1]
    tempLeft = controls[2]
    tempLeft = tempLeft[1:len(tempLeft)-1]
    tempRight = controls[3]
    tempRight = tempRight[1:len(tempRight)-1]
    keybindsLabel = Label(keybindsFrame, width=30, height=4, bg="pink", text="CHANGE KEYBINDS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    keybindsPromptLabel = Label(keybindsFrame, width=50, height=2, bg="pink", text="Click a keybind to change", font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    upBtn = Btn(keybindsFrame, width=25, height=1, text="Up: " + tempUp, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(0))
    downBtn = Btn(keybindsFrame, width=25, height=1, text="Down: " + tempDown, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(1))
    leftBtn = Btn(keybindsFrame, width=25, height=1, text="Left: " + tempLeft, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(2))
    rightBtn = Btn(keybindsFrame, width=25, height=1, text="Right: " + tempRight, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(3))
    keybindsSettingsBtn = Btn(keybindsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    # NEED TO ADD EXTRA BUTTON FOR BOSS KEY

    # KEYBIND FRAME PACKING
    keybindsLabel.pack(side="top", pady=(150, 0))
    keybindsPromptLabel.pack(side="top", pady=(30, 0))
    upBtn.pack(side="top", pady=(60, 0))
    downBtn.pack(side="top", pady=(20, 0))
    leftBtn.pack(side="top", pady=(20, 0))
    rightBtn.pack(side="top", pady=(20, 0))    
    keybindsSettingsBtn.pack(side="top", pady=(70, 0))

    # CHEATS FRAME WIDGETS
    cheatsLabel = Label(cheatsFrame, width=30, height=4, bg="pink", text="CHEATS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    smallerPlayerBtn = CheckBtn(cheatsFrame, width=25, height=1, text="Smaller Player", bg="light blue", activebackground="light blue", font=("Comic Sans MS", 15, "bold"), command=lambda:changeCheats(0))
    invincibility = CheckBtn(cheatsFrame, width=25, height=1, text="Invincible", bg="light blue", activebackground="light blue", font=("Comic Sans MS", 15, "bold"), command=lambda:changeCheats(1))
    cheatsHomeBtn = Btn(cheatsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))

    # CHEATS FRAME PACKING
    cheatsLabel.pack(side="top", pady=(150, 0))
    smallerPlayerBtn.pack(side="top", pady=(150, 0))
    invincibility.pack(side="top", pady=(20, 0))
    cheatsHomeBtn.pack(side="top", pady=(200, 0))

    # LEADERBOARD FRAME WIDGETS
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="pink", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    leaderboardHomeBtn = Btn(leaderboardFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))
    createLeaderboard()

    # LEADERBOARD FRAME PACKING
    leaderboardLabel.pack(side="top", pady=(150, 0))
    leaderboard.pack(side="top", pady=(50, 0))
    leaderboardHomeBtn.pack(side="top", pady=(60, 0))

    # INFO FRAME WIDGETS
    infoLabel = Label(infoFrame, width=30, height=4, bg="pink", text="HOW TO PLAY", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    howToPlayLabel = Label(infoFrame, width=60, height=12, bg="pink", text=howToPlayText, font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    infoHomeBtn = Btn(infoFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # INFO FRAME PACKING
    infoLabel.pack(side="top", pady=(150, 0))
    howToPlayLabel.pack(side="top", pady=(50, 0))
    infoHomeBtn.pack(side="top", pady=(90, 0))

    # GAME OVER FRAME WIDGETS
    global finalScoreLabel, nameInput, submitBtn
    gameOverLabel = Label(gameOverFrame, width=30, height=4, bg="pink", text="GAME OVER!", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    finalScoreLabel = Label(gameOverFrame, width=30, height=5, bg="pink", text="", font=("Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    nameInput = Entry(gameOverFrame, width=30, bg="#aeeafc", font=("Comic Sans MS", 20, "bold"), justify="center")
    submitBtn = Btn(gameOverFrame, width=25, height=1, text="Submit Name", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=addToLeaderboard)
    gameOverHomeBtn = Btn(gameOverFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # GAME OVER FRAME PACKING
    gameOverLabel.pack(side="top", pady=(150, 0))
    finalScoreLabel.pack(side="top", pady=(50, 0))
    nameInput.pack(side="top", pady=(70, 0))
    submitBtn.pack(side="top", pady=(70, 0))
    gameOverHomeBtn.pack(side="top", pady=(20, 0))

    # BOSS KEY FRAME WIDGETS AND PACKING
    global bossImage
    bossImage = Image(file="BossKeyImage.png")
    bossKeyImage = Label(bossFrame, image=bossImage)
    bossKeyImage.pack(fill="both", expand=True)

def swapFrames(frameNum):
    '''Swaps to a frame according to the given button press.'''
    if frameNum == 0: # Swap to the home frame
        settingsFrame.pack_forget()
        leaderboardFrame.pack_forget()
        infoFrame.pack_forget()
        gameOverFrame.pack_forget()
        homeFrame.pack(fill="both", expand=True)
        nameInput.delete(0, "end") # Disable entry box after going back home
        nameInput.configure(state="disabled") 
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
        submitBtn.configure(bg="light blue", relief="raised", command=addToLeaderboard) # Reset submit button
        nameInput.configure(state="normal") # Re-enable entry box
    elif frameNum == 7: # Swap to the cheats frame
        settingsFrame.pack_forget()
        cheatsFrame.pack(fill="both", expand=True)
    else: # Swap to the boss frame                      NEEDS FIXING, DOESN'T SHOW ABOVE CANVAS
        global bossEnabled
        if bossEnabled == True:
            bossFrame.place_forget()
            bossEnabled = False
        else:
            bossFrame.place(x=0, y=0)
            bossEnabled = True

def exitGame():
    '''Save all settings and current leaderboard state, then close the game.'''
    saveSettings()
    saveLeaderboard()
    window.destroy()

#---------------------------------------------- SETTINGS FUNCTIONS --------------------------------------------------------------------

def initialiseSettings():
    '''Initialise all the settings and read settings.txt file to get saved settings.'''
    #Initialise unsaved settings
    global triggeredKeybindChange, keybindNum, controls, bgColour, previousBind, howToPlayText, cheatCode, cheats, bossEnabled
    triggeredKeybindChange = False # Checks if player clicked button to change keybind
    keybindNum = 0
    previousBind = "" # Used when unbinding previous key
    howToPlayText = "Dodge the never-ending balls as long as you can!\nThe colour of the balls indicates their speed.\n\n(Black = Slow, Blue = Medium, Purple = Fast, Red = Very Fast)\n\nEvery 3 seconds, a new ball gets added at the sides, so watch out!\nYour final score is the number of balls you ended with.\n\nGood Luck!"
    cheatCode = "" # Keeps track of keys pressed to check if they enter a cheat code
    cheats = [False, False] # Checks what cheats are enabled
    bossEnabled = False # Checks if the boss frame is active or not

    # Get saved settings from settings.txt file
    controls = []
    bgColour = ""
    settings = open("settings.txt", "r")
    for setting in range(5):
        setting = settings.readline().strip()
        controls.append(setting)
    bgColour = settings.readline().strip()

    settings.close()

def saveSettings():
    '''Save the current settings in a text file for next time.'''
    global controls, bgColour
    settings = open("settings.txt", "w")
    for setting in controls:
        settings.write(setting + "\n")
    settings.write(bgColour)
    settings.close()

def changeBackground(bgCode):
    '''Changes the colour of the backgrounds according to user input'''
    # Get colour code from argument
    global bgColour
    bgColour = bgCode
    
    # Update each frame
    homeFrame.configure(bg=bgColour)
    settingsFrame.configure(bg=bgColour)
    leaderboardFrame.configure(bg=bgColour)
    infoFrame.configure(bg=bgColour)
    gameOverFrame.configure(bg=bgColour)
    bgFrame.configure(bg=bgColour)
    keybindsFrame.configure(bg=bgColour)
    cheatsFrame.configure(bg=bgColour)

def initialiseKeybinds():
    '''Bind the initial keybinds with their respective functions.'''
    window.bind(controls[0], upDirection)
    window.bind(controls[1], downDirection)
    window.bind(controls[2], leftDirection)
    window.bind(controls[3], rightDirection)
    window.bind(controls[4], lambda a=8: swapFrames(a))
    window.bind("<BackSpace>", cancelCheatCode)
    window.bind("<Escape>", pause)
    window.bind("<Key>", updateKeybind)

def setKeybindChange(tempNum):
    '''Sets the boolean state to true so that the player can then press the key and update their keybind.'''
    global triggeredKeybindChange, keybindNum, keybindsSettingsBtn
    keybindsPromptLabel.configure(text="Press the key you want to bind:")
    triggeredKeybindChange = True # Set flag saying user wants to change their keybind
    keybindNum = tempNum
    keybindsSettingsBtn.configure(text="Cancel", command=cancelKeybindChange) # Change button to a cancel button

def updateKeybind(event):
    '''Updates the keybind as long as they intended to, else adds the keypress to the cheat code buffer.'''
    global controls, triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    if triggeredKeybindChange == False:
        updateCheatCode(event.keysym) # Add keypress to cheat code
    else: # Only update if they pressed a button beforehand
        window.unbind(controls[keybindNum])
        controls[keybindNum] = "<" + event.keysym + ">" # Store as correct key format
        triggeredKeybindChange = False # Reset variables
        keybindsPromptLabel.configure(text="Click a keybind to change") # Change label to original message
        keybindsSettingsBtn.configure(text="Back to Settings", command=lambda:swapFrames(1)) # Change button back to normal
        tempText = controls[keybindNum]
        tempText = tempText[1:len(tempText)-1] # Get rid of < >

        # Update corresponding button and bind
        if keybindNum == 0:
            upBtn.configure(text="Up: " + tempText)
            window.bind(controls[keybindNum], upDirection)
        elif keybindNum == 1:
            downBtn.configure(text="Down: " + tempText)
            window.bind(controls[keybindNum], downDirection)
        elif keybindNum == 2:
            leftBtn.configure(text="Left: " + tempText)
            window.bind(controls[keybindNum], leftDirection)
        else:
            rightBtn.configure(text="Right: " + tempText)
            window.bind(controls[keybindNum], rightDirection)

def cancelKeybindChange():
    '''Used if the user decides not to bind a key after clicking a button.'''
    global triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    triggeredKeybindChange = False #Reset variables
    keybindsPromptLabel.configure(text="Click a keybind to change")
    keybindsSettingsBtn.configure(text="Back to Settings", command=lambda:swapFrames(1)) # Change button back to normal

#---------------------------------------------- LEADERBOARD FUNCTIONS -----------------------------------------------------------------------

#                                 ADD ABILITY TO ADD NAME AND SCORE FROM GAME OVER MENU

def createLeaderboard():
    '''Creates and formats the leaderboard with headings.'''
    global leaderboard
    style = ttk.Style() # Configure style of leaderboard
    style.theme_use("clam")
    style.configure("Treeview", fieldbackground="pink", font=("Comic Sans MS", 15, "bold"), rowheight=35)
    style.configure("Treeview.Heading", background="pink", font=("Comic Sans MS", 20, "bold"))
    leaderboard = ttk.Treeview(leaderboardFrame, columns=("name", "score"), show="headings")
    leaderboard.column("name", anchor="center") # Give leaderboard headings
    leaderboard.heading("name", text="Name")
    leaderboard.column("score", anchor="center")
    leaderboard.heading("score", text="Score")
    populateLeaderboard() # Fill the leaderboard

def populateLeaderboard():
    '''Reads the text file 'leaderboard.txt' and populates the leaderboard.'''
    leaderboardFile = open("leaderboard.txt", "r")
    tempName = leaderboardFile.readline().strip()
    leaderboard.tag_configure("odd", background="pink") # Create tags for rows
    leaderboard.tag_configure("even", background="#fca7f5")
    rowNum = 0
    while tempName != "": # Loop through the file until end of file is reached
        tempScore = leaderboardFile.readline().strip()
        if rowNum % 2 == 0:
            leaderboard.insert("", "end", iid=rowNum, values=(tempName, tempScore), tags=("even",)) # NEEDS FIXING, DOESN'T CHANGE COLOUR
        else:
            leaderboard.insert("", "end", iid=rowNum, values=(tempName, tempScore), tags=("odd",))
        rowNum += 1
        tempName = leaderboardFile.readline().strip()
    leaderboardFile.close()

def addToLeaderboard():
    '''Take user input and add it to the leaderboard.'''
    global cheats

    # Check if they cheated
    cheated = False
    for cheat in cheats:
        if cheat:
            cheated = True

    # Get input from entry box
    name = nameInput.get()

    if cheated:
        finalScoreLabel.configure(text="Cheaters can't add their\nscore to the leaderboard :)")
    elif name == "":
        finalScoreLabel.configure(text="Field is empty.")
    else:
        finalScoreLabel.configure(text="Score Submitted!")
        submitBtn.configure(bg="red", relief="sunken", command=lambda:finalScoreLabel.configure(text="Already submitted your score."))
        nameInput.delete(0, "end")
        nameInput.configure(state="disabled")

        # Get all entries from the leaderboard
        treeviewData = []
        for line in leaderboard.get_children():
            tempArray = []
            for value in leaderboard.item(line)["values"]:
                tempArray.append(value)
            treeviewData.append(tempArray)
        
        # Empty the leaderboard
        numOfEntries = 0
        for line in leaderboard.get_children():
            numOfEntries += 1
            leaderboard.delete(line)
        
        # Repopulate leaderboard with new entry
        newEntry = [name, str(score)]
        placed = False
        for line in range(numOfEntries):
            if score < int(treeviewData[line][1]):
                leaderboard.insert("", "end", iid=line, values=(treeviewData[line]))
            else:
                if placed == False:
                    leaderboard.insert("", "end", iid=line, values=(newEntry))
                    placed = True
                else:
                    leaderboard.insert("", "end", iid=line, values=(treeviewData[line-1]))

        if placed == False:
            leaderboard.insert("", "end", iid=numOfEntries, values=(newEntry))
        else:
            leaderboard.insert("", "end", iid=numOfEntries, values=(treeviewData[numOfEntries-1]))

def saveLeaderboard():
    '''Writes the current state of the leaderboard to the file to save it for next time.'''
    global window
    leaderboardFile = open("leaderboard.txt", "w")
    for entry in leaderboard.get_children():
        for value in leaderboard.item(entry)["values"]:
            leaderboardFile.write(str(value)+"\n") # Write every entry to the text file
    leaderboardFile.close()

#---------------------------------------------- CHEAT CODE FUNCTIONS -----------------------------------------------------------------------

#                          ONLY UPDATE LEADERBOARD IF USING NO CHEATS BY CHECKING 'CHEATS' ARRAY

def cancelCheatCode(event):
    '''Resets the cheat code for misinputs.'''
    global cheatCode
    cheatCode = ""
 
def updateCheatCode(keyName):
    '''Updates the cheat code and then checks if the player has inputted it correctly.'''
    global cheatCode, cheatsBtn
    cheatCode += keyName
    if cheatCode == "unlockcheats":
        cheatsBtn.configure(command=lambda:swapFrames(7), bg="light blue")

def changeCheats(cheatNum):
    '''Enables or disables the cheat that the player chose.'''
    if cheats[cheatNum] == True:
        cheats[cheatNum] = False
    else:
        cheats[cheatNum] = True

#---------------------------------------------- GAME FUNCTIONS -----------------------------------------------------------------------

def initialiseGame():
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop.'''
    # Hide the menu and create the game canvas
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameCanvas.pack(fill="both", expand=True)

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, playerDirectionX, playerDirectionY, paused, player, scoreText, countdownText, pausedBackground, pausedText, bossImage
    time = 0
    score = 0
    numBalls = 0
    balls = [] # Stores all the balls created
    xSpeed = [] # Stores speed values for each ball
    ySpeed = []
    playerDirectionX = 7
    playerDirectionY = 0
    paused = False 
    if cheats[0] == True: # If smaller player cheat is enabled, make smaller player
        xy = (950, 530, 970, 550)
    else:
        xy = (930, 510, 990, 570)
    player = gameCanvas.create_rectangle(xy, fill="light blue", outline="black")
    scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    countdownText = gameCanvas.create_text(960, 540, text="3", font=("Comic Sans MS", 75, "bold"), state="normal")
    pausedBackground = gameCanvas.create_rectangle(850, 480, 100, 600, fill="pink", outline="black", state="hidden")
    pausedText = gameCanvas.create_text(960, 540, text="PAUSED\nPress Esc to resume.", font=("Comic Sans MS", 75, "bold"), state="hidden")

    # Start with 1 ball
    createBall()
    
    # Start the countdown, then start the game
    countdown()
    gameLoop()

def countdown():
    '''Short countdown before the game starts'''
    global countdownText
    for i in range(3, 0, -1):
        gameCanvas.itemconfigure(countdownText, text=str(i))
        window.update()
        sleep(1)
    gameCanvas.itemconfigure(countdownText, text="Go!")
    window.update()
    sleep(1)
    gameCanvas.itemconfigure(countdownText, state="hidden")

def gameLoop():
    '''The main game loop that repeats until the game ends, then switches to the game over screen.'''
    # Keep track of if the game should loop again
    global activeGame, time, score, paused
    activeGame = True

    # Keep looping until player is hit
    while activeGame:
        gameCanvas.move(player, playerDirectionX, playerDirectionY)
        moveBalls()
        checkPlayerCrash()
        sleep(0.005)
        time += 0.005
        score += 0.03
        displayScore = int(score)
        gameCanvas.itemconfigure(scoreText, text="Score: " + str(displayScore))
        if time > 1:
            createBall()
            time = 0
        # while paused:                                NEEDS FIXING, CRASHES GAME
        #    sleep(0.01)
        window.update()

    # Go to game over screen once game is finished
    score = int(score)
    finalScoreLabel.configure(text="You scored " + str(score) + " points!\n\nEnter your name to save your score\nor exit to the menu")
    swapFrames(6)

def pause(event):                                    # NEEDS FIXING, DOESN'T PAUSE THE GAME, JUST SHOWS LOGO
    '''Pause or unpause the game, and display the paused logo.'''
    global paused
    if paused:
        paused = False
        gameCanvas.itemconfigure(pausedBackground, state="hidden")
        gameCanvas.itemconfigure(pausedText, state="hidden")
    else:
        paused = True
        gameCanvas.itemconfigure(pausedBackground, state="normal")
        gameCanvas.itemconfigure(pausedText, state="normal")
    print(paused)

#def bossKey():
#    pause()

#---------------------------------------------- POWER UP FUNCTIONS -----------------------------------------------------------------------

# HALF SPEED VALUES AND DOUBLE AFTERWARDS
def slowTime():
    pass

# INCREASE SCORE AFTER COLLECTING POWER UP
def increaseScore():
    pass

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
        gameCanvas.itemconfigure(balls[numBalls], fill="#ff0000", outline="black")
    elif averageSpeed >= 7:
        gameCanvas.itemconfigure(balls[numBalls], fill="#d303fc", outline="black")
    elif averageSpeed >= 5:
        gameCanvas.itemconfigure(balls[numBalls], fill="blue", outline="black")
    else:
        gameCanvas.itemconfigure(balls[numBalls], fill="black", outline="black")
    
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
    global playerDirectionX, playerDirectionY
    playerDirectionX = 0
    playerDirectionY = -7

def downDirection(event):
    '''Change the player's direction to down.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = 0
    playerDirectionY = 7

def leftDirection(event):
    '''Change the player's direction to left.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = -7
    playerDirectionY = 0

def rightDirection(event):
    '''Change the player's direction to right.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = 7
    playerDirectionY = 0

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
changeBackground(bgColour) # Set up initial background colour
initialiseKeybinds() # Set up the initial keybinds
homeFrame.pack(fill="both", expand=True) # Start at the home page

window.mainloop()