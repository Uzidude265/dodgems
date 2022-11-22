# SCREEN RESOLUTION: 1920x1080
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
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, gameOverFrame, bgFrame, keybindsFrame, cheatsFrame, bossFrame, pauseFrame
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)
    bgFrame = Frame(window)
    keybindsFrame = Frame(window)
    cheatsFrame = Frame(window)
    bossFrame = Frame(window)
    pauseFrame = Frame(window)

    # HOME FRAME WIDGETS
    global logo, loadBtn
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    playBtn = Btn(homeFrame, width=25, height=1, text="Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:initialiseGame(False))
    loadBtn = Btn(homeFrame, width=25, height=1, text="Load Game", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=loadGame)
    settingsBtn = Btn(homeFrame, width=25, height=1, text="Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))
    leaderboardBtn = Btn(homeFrame, width=25, height=1, text="Leaderboard", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(4))
    infoBtn = Btn(homeFrame, width=25, height=1, text="How to Play", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(5))
    exitBtn = Btn(homeFrame, width=25, height=1, text="Exit", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=exitGame)

    # HOME FRAME PACKING
    homeLabel.pack(side="top", pady=(130, 0))
    playBtn.pack(side="top", pady=(95, 0))
    loadBtn.pack(side="top", pady=(10, 0))
    settingsBtn.pack(side="top", pady=(10, 0))
    leaderboardBtn.pack(side="top", pady=(10, 0))
    infoBtn.pack(side="top", pady=(10, 0))
    exitBtn.pack(side="top", pady=(10, 0))

    # SETTINGS FRAME WIDGETS
    global cheatsBtn
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="pink", text="SETTINGS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    bgBtn = Btn(settingsFrame, width=25, height=1, text="Change Background Colour", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(2))
    keybindsBtn = Btn(settingsFrame, width=25, height=1, text="Change Keybinds", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(3))
    defaultsBtn = Btn(settingsFrame, width=25, height=1, text="Reset to Default Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=defaultSettings)
    cheatsBtn = Btn(settingsFrame, width=25, height=1, text="Cheats", bg="red", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=None)
    settingsHomeBtn = Btn(settingsFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # SETTINGS FRAME PACKING
    settingsLabel.pack(side="top", pady=(150, 0))
    bgBtn.pack(side="top", pady=(105, 0))
    keybindsBtn.pack(side="top", pady=(20, 0))
    defaultsBtn.pack(side="top", pady=(20, 0))
    cheatsBtn.pack(side="top", pady=(20, 0))
    settingsHomeBtn.pack(side="top", pady=(120, 0))

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
    global upBtn, downBtn, leftBtn, rightBtn, bossKeyBtn, keybindsSettingsBtn, keybindsPromptLabel
    tempUp = controls[0] # Remove the < > from the controls to add to the corresponding button's text
    tempUp = tempUp[1:len(tempUp)-1]
    tempDown = controls[1]
    tempDown = tempDown[1:len(tempDown)-1]
    tempLeft = controls[2]
    tempLeft = tempLeft[1:len(tempLeft)-1]
    tempRight = controls[3]
    tempRight = tempRight[1:len(tempRight)-1]
    tempBossKey = controls[4]
    tempBossKey = tempBossKey[1:len(tempBossKey)-1]
    keybindsLabel = Label(keybindsFrame, width=30, height=4, bg="pink", text="CHANGE KEYBINDS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    keybindsPromptLabel = Label(keybindsFrame, width=50, height=2, bg="pink", text="Click a keybind to change", font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    upBtn = Btn(keybindsFrame, width=25, height=1, text="Up: " + tempUp, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(0))
    downBtn = Btn(keybindsFrame, width=25, height=1, text="Down: " + tempDown, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(1))
    leftBtn = Btn(keybindsFrame, width=25, height=1, text="Left: " + tempLeft, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(2))
    rightBtn = Btn(keybindsFrame, width=25, height=1, text="Right: " + tempRight, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(3))
    bossKeyBtn = Btn(keybindsFrame, width=25, height=1, text="Boss Key: " + tempBossKey, bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:setKeybindChange(4))
    keybindsSettingsBtn = Btn(keybindsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))

    # KEYBIND FRAME PACKING
    keybindsLabel.pack(side="top", pady=(150, 0))
    keybindsPromptLabel.pack(side="top", pady=(30, 0))
    upBtn.pack(side="top", pady=(50, 0))
    downBtn.pack(side="top", pady=(10, 0))
    leftBtn.pack(side="top", pady=(10, 0))
    rightBtn.pack(side="top", pady=(10, 0))
    bossKeyBtn.pack(side="top", pady=(10, 0)) 
    keybindsSettingsBtn.pack(side="top", pady=(50, 0))

    # CHEATS FRAME WIDGETS
    cheatsLabel = Label(cheatsFrame, width=30, height=4, bg="pink", text="CHEATS", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    smallerPlayerBtn = CheckBtn(cheatsFrame, width=25, height=2, text="Smaller Player", bg="light blue", activebackground="light blue", font=("Comic Sans MS", 15, "bold"), command=lambda:changeCheats(0))
    invincibility = CheckBtn(cheatsFrame, width=25, height=2, text="Invincible", bg="light blue", activebackground="light blue", font=("Comic Sans MS", 15, "bold"), command=lambda:changeCheats(1))
    cheatsHomeBtn = Btn(cheatsFrame, width=25, height=1, text="Back to Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(1))

    # CHEATS FRAME PACKING
    cheatsLabel.pack(side="top", pady=(150, 0))
    smallerPlayerBtn.pack(side="top", pady=(170, 0))
    invincibility.pack(side="top", pady=(20, 0))
    cheatsHomeBtn.pack(side="top", pady=(160, 0))

    # LEADERBOARD FRAME WIDGETS
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="pink", text="LEADERBOARD", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    leaderboardHomeBtn = Btn(leaderboardFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))
    createLeaderboard()

    # LEADERBOARD FRAME PACKING
    leaderboardLabel.pack(side="top", pady=(150, 0))
    leaderboard.pack(side="top", pady=(45, 0))
    leaderboardHomeBtn.pack(side="top", pady=(45, 0))

    # INFO FRAME WIDGETS
    infoLabel = Label(infoFrame, width=30, height=4, bg="pink", text="HOW TO PLAY", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    howToPlayLabel = Label(infoFrame, width=60, height=12, bg="pink", text=howToPlayText, font=("Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    infoHomeBtn = Btn(infoFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # INFO FRAME PACKING
    infoLabel.pack(side="top", pady=(150, 0))
    howToPlayLabel.pack(side="top", pady=(50, 0))
    infoHomeBtn.pack(side="top", pady=(90, 0))

    # PAUSE FRAME WIDGETS
    global pauseInfoLabel, saveBtn, pauseHomeBtn
    pauseLabel = Label(pauseFrame, width=30, height=4, bg="pink", text="GAME PAUSED", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    pauseInfoLabel = Label(pauseFrame, width=30, height=6, bg="pink", text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.", font=("Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    saveBtn = Btn(pauseFrame, width=25, height=1, text="Save Game", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:saveGame(False))
    pauseHomeBtn = Btn(pauseFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # PAUSE FRAME PACKING
    pauseLabel.pack(side="top", pady=(150, 0))
    pauseInfoLabel.pack(side="top", pady=(100, 0))
    saveBtn.pack(side="top", pady=(100, 0))
    pauseHomeBtn.pack(side="top", pady=(20, 0))

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
        global paused, gameActive
        settingsFrame.pack_forget()
        leaderboardFrame.pack_forget()
        infoFrame.pack_forget()
        gameOverFrame.pack_forget()
        pauseFrame.pack_forget()
        homeFrame.pack(fill="both", expand=True)
        nameInput.delete(0, "end") # Disable entry box after going back home
        nameInput.configure(state="disabled")
        paused = False
        gameActive = False
        if slowed:
            gameCanvas.after_cancel(slowTextRepeatNum)
            gameCanvas.after_cancel(unslowRepeatNum)
        if invincible:
            gameCanvas.after_cancel(invincibilityTextRepeatNum)
            gameCanvas.after_cancel(disableInvincibilityRepeatNum)
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
    else: # Swap to the cheats frame
        settingsFrame.pack_forget()
        cheatsFrame.pack(fill="both", expand=True)

def bossKey(event):
    '''Activates whenever the boss key is pressed and displays an unsuspecting image.'''
    global gameActive, bossEnabled, paused, pauseFrameActive, randomizeRepeatNum, scoreUpRepeatNum, timeRepeatNum, scoreTimeRepeatNum
    if gameActive == False: # If at menu, place boss frame on top
        if bossEnabled == True:
            bossEnabled = False
            bossFrame.place_forget()
        else:
            bossEnabled = True
            bossFrame.place(x=0, y=0)
    elif gameActive == True and pauseFrameActive == False: # If game active, pause the game and hide gameCanvas
        if bossEnabled == True:
            bossEnabled = False
            paused = False
            bossFrame.pack_forget()
            gameCanvas.pack(fill="both", expand=True)
            gameLoop()
        else:
            bossEnabled = True
            paused = True
            gameCanvas.pack_forget()
            bossFrame.pack(fill="both", expand=True)
            gameCanvas.after_cancel(randomizeRepeatNum) # Stop after loop from randomizing abilities
            gameCanvas.after_cancel(timeRepeatNum)
            gameCanvas.after_cancel(scoreTimeRepeatNum)
            if scoreUpRepeatNum != 0:
                gameCanvas.after_cancel(scoreUpRepeatNum)
            if slowed:
                gameCanvas.after_cancel(slowTextRepeatNum)
                gameCanvas.after_cancel(unslowRepeatNum)
            if invincible:
                gameCanvas.after_cancel(invincibilityTextRepeatNum)
                gameCanvas.after_cancel(disableInvincibilityRepeatNum)
    elif pauseFrameActive == True: # Else if the pause frame is showing, replace with boss frame
        if bossEnabled == True:
            bossEnabled = False
            bossFrame.place_forget()
            pauseFrame.pack(fill="both", expand=True)
        else:
            bossEnabled = True
            pauseFrame.pack_forget()
            bossFrame.place(x=0, y=0)

def exitGame():
    '''Save all settings and current leaderboard state, then close the game.'''
    saveSettings()
    saveLeaderboard()
    window.destroy()

#---------------------------------------------- SETTINGS FUNCTIONS --------------------------------------------------------------------

def initialiseSettings():
    '''Initialise all the settings and read settings.txt file to get saved settings.'''
    #Initialise unsaved settings
    global triggeredKeybindChange, keybindNum, controls, bgColour, previousBind, howToPlayText, cheatCode, cheats, bossEnabled, gameActive, paused, pauseFrameActive
    triggeredKeybindChange = False # Checks if player clicked button to change keybind
    keybindNum = 0
    previousBind = "" # Used when unbinding previous key
    howToPlayText = "Dodge the never-ending balls as long as you can!\nThe colour of the balls indicates their speed.\n\n(Black = Slow, Blue = Medium, Purple = Fast, Red = Very Fast)\n\nEvery 3 seconds, a new ball gets added at the sides, so watch out!\nYour final score is the number of balls you ended with.\n\nGood Luck!"
    cheatCode = "" # Keeps track of keys pressed to check if they enter a cheat code
    cheats = [False, False] # Checks what cheats are enabled
    bossEnabled = False # Checks if the boss frame is active or not
    gameActive = False
    paused = False
    pauseFrameActive = False # Used by bossKey to check if the pause frame is showing

    # Get saved settings from settings.txt file
    controls = []
    bgColour = ""
    settings = open("settings.txt", "r")
    for setting in range(5):
        setting = settings.readline().strip()
        controls.append(setting)
    bgColour = settings.readline().strip()
    settings.close()

    # Check if there is a save
    global saveExists
    saveFile = open("save.txt", "r")
    time = saveFile.readline().strip()
    if time == "":
        saveExists = False
    else:
        saveExists = True
    saveFile.close()

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
    pauseFrame.configure(bg=bgColour)

def initialiseKeybinds():
    '''Bind the initial keybinds with their respective functions.'''
    window.bind(controls[0], upDirection)
    window.bind(controls[1], downDirection)
    window.bind(controls[2], leftDirection)
    window.bind(controls[3], rightDirection)
    window.bind(controls[4], bossKey)
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

def cancelKeybindChange():
    '''Used if the user decides not to bind a key after clicking a button.'''
    global triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    triggeredKeybindChange = False #Reset variables
    keybindsPromptLabel.configure(text="Click a keybind to change")
    keybindsSettingsBtn.configure(text="Back to Settings", command=lambda:swapFrames(1)) # Change button back to normal

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
        elif keybindNum == 3:
            rightBtn.configure(text="Right: " + tempText)
            window.bind(controls[keybindNum], rightDirection)
        else:
            bossKeyBtn.configure(text="Boss Key: " + tempText)
            window.bind(controls[keybindNum], bossKey)

def defaultSettings():
    global bgColour, controls
    bgColour = "#cbf7e6"
    for control in controls:
        window.unbind(control)
    controls = ["<Up>", "<Down>", "<Left>", "<Right>", "<Control_L>"]
    initialiseKeybinds()
    upBtn.configure(text="Up: Up")
    downBtn.configure(text="Down: Down")
    leftBtn.configure(text="Left: Left")
    rightBtn.configure(text="Right: Right")
    bossKeyBtn.configure(text="Boss Key: Control_L")
    changeBackground(bgColour)

def saveSettings():
    '''Save the current settings in a text file for next time.'''
    global controls, bgColour
    settings = open("settings.txt", "w")
    for setting in controls:
        settings.write(setting + "\n")
    settings.write(bgColour)
    settings.close()
    
#---------------------------------------------- LEADERBOARD FUNCTIONS -----------------------------------------------------------------------

def createLeaderboard():
    '''Creates and formats the leaderboard with headings.'''
    global leaderboard
    style = ttk.Style() # Configure style of leaderboard
    style.theme_use("clam")
    style.configure("Treeview", font=("Comic Sans MS", 15, "bold"), rowheight=35)
    style.configure("Treeview.Heading", background="pink", font=("Comic Sans MS", 20, "bold"))
    leaderboard = ttk.Treeview(leaderboardFrame, columns=("name", "time", "score"), show="headings")
    leaderboard.column("name", anchor="center") # Give leaderboard headings
    leaderboard.heading("name", text="Name:")
    leaderboard.column("time", anchor="center")
    leaderboard.heading("time", text="Time:")
    leaderboard.column("score", anchor="center")
    leaderboard.heading("score", text="Score:")
    populateLeaderboard() # Fill the leaderboard

def populateLeaderboard():
    '''Reads the text file 'leaderboard.txt' and populates the leaderboard.'''
    leaderboardFile = open("leaderboard.txt", "r")
    tempName = leaderboardFile.readline().strip()
    leaderboard.tag_configure("odd", background="pink") # Create tags for rows
    leaderboard.tag_configure("even", background="#fca7f5")
    rowNum = 0
    while tempName != "": # Loop through the file until end of file is reached
        tempTime = leaderboardFile.readline().strip()
        tempScore = leaderboardFile.readline().strip()
        if rowNum % 2 == 0:
            leaderboard.insert("", "end", iid=rowNum, values=(tempName, tempTime, tempScore), tags=("even",)) # NEEDS FIXING, DOESN'T CHANGE COLOUR
        else:
            leaderboard.insert("", "end", iid=rowNum, values=(tempName, tempTime, tempScore), tags=("odd",))
        rowNum += 1
        tempName = leaderboardFile.readline().strip()
    leaderboardFile.close()

def addToLeaderboard():
    '''Take user input and add it to the leaderboard.'''
    global cheats, cheated

    # Check if they cheated
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
        newEntry = [name, str(time), str(score)]
        placed = False
        for line in range(numOfEntries):
            if score < int(treeviewData[line][2]):
                leaderboard.insert("", "end", iid=line, values=(treeviewData[line]))
            else:
                if placed == False:
                    leaderboard.insert("", "end", iid=line, values=(newEntry))
                    placed = True
                else:
                    leaderboard.insert("", "end", iid=line, values=(treeviewData[line-1]))

        # Place final entry
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

def initialiseGame(loaded):
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop.'''
    # Hide the menu and create the game canvas
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameCanvas.pack(fill="both", expand=True)

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, playerDirectionX, playerDirectionY, saved, playerCoords, ballPos, cheated, lives, ballTextCount, slowed, slowTextCount, slowCount, invincible, invincibilityTextCount, invincibilityCount, abilityCoords
    if loaded == False: # Only use default numbers if game wasn't loaded
        time = 0
        score = 0
        numBalls = 0
        balls = [] # Stores all the balls created
        xSpeed = [] # Stores speed values for each ball
        ySpeed = []
        playerCoords = (935, 515, 985, 565)
        cheated = False
        lives = 3
        ballTextCount = 0
        slowed = False
        slowTextCount = 0
        slowCount = 0 # Stores how many slow time power ups they have collected
        invincible = False
        invincibilityTextCount = 0
        invincibilityCount = 0 # Stores how many invincible power ups they have collected
        abilityCoords = [(0,0,0,0) for x in range(4)]
    else:
        balls = []
        for ball in ballPos:
            balls.append(gameCanvas.create_oval(ball[0], ball[1], ball[2], ball[3], fill=ball[4], width=2))
    playerDirectionX = 7
    playerDirectionY = 0
    saved = False

    # Create all abilities
    global abilities, abilityNum, previousAbility
    abilities = []
    abilities.append(gameCanvas.create_rectangle(abilityCoords[0], fill="lime", outline="black", width=2)) # scoreUp ability
    abilities.append(gameCanvas.create_rectangle(abilityCoords[1], fill="white", outline="black", width=2)) # invincibility ability
    abilities.append(gameCanvas.create_rectangle(abilityCoords[2], fill="orange", outline="black", width=2)) # slow time ability
    abilities.append(gameCanvas.create_rectangle(abilityCoords[3], fill="cyan", outline="black", width=2)) # delete balls ability
    abilityNum = 0
    previousAbility = 0

    # Create player
    global player, beenHit
    if cheats[0] == True: # If smaller player cheat is enabled, make smaller player
        playerCoords = (playerCoords[0]+15, playerCoords[1]+15, playerCoords[2]-15, playerCoords[3]-15)
    player = gameCanvas.create_rectangle(playerCoords, fill="light blue", outline="black", width=2)
    beenHit = False

    # Create and Modify Hearts
    global heart, heartBroken, heart1, heart2, heart3
    heart = Image(file="Heart.png")
    heartBroken = Image(file="HeartBroken.png")
    heart1 = gameCanvas.create_image(1750, 1020, image=heart)
    heart2 = gameCanvas.create_image(1800, 1020, image=heart)
    heart3 = gameCanvas.create_image(1850, 1020, image=heart)
    updateHearts() # Update the hearts if they load the game

    # Make all text and rectangles behind the text
    global saveBtn, scoreText, invincibilityText, invincibilityTextRectangle, slowText, slowTextRectangle, timeText, ballText, ballTextRectangle, countdownText, livesText, livesTextRectangle
    saveBtn.configure(text="Save Game")
    scoreText = gameCanvas.create_text(1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(scoreText)
    scoreTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    invincibilityText = gameCanvas.create_text(135, 30, text="Invincibility: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(invincibilityText)
    invincibilityTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(invincibilityTextRectangle, invincibilityText) # Puts the rectangle behind the text
    slowText = gameCanvas.create_text(385, 30, text="Slow Time: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(slowText)
    slowTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(slowTextRectangle, slowText) # Puts the rectangle behind the text 
    timeText = gameCanvas.create_text(1600, 30, text="Time: " + str(time), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(timeText)
    timeTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(timeTextRectangle, timeText) # Puts the rectangle behind the text
    ballText = gameCanvas.create_text(960, 30, text="Time Until Next Ball: " + str(ballTextCount), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(ballText)
    ballTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(ballTextRectangle, ballText) # Puts the rectangle behind the text
    countdownText = gameCanvas.create_text(960, 540, text="3", font=("Comic Sans MS", 75, "bold"))
    livesText = gameCanvas.create_text(1665, 1020, text="Lives:", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(livesText)
    livesTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1]-25, bbox[2]+200, bbox[3]+25, outline="black", width=2)
    gameCanvas.lower(livesTextRectangle, heart1)

    gameLoop()

def countdown():
    '''Short countdown before the game starts'''
    global countdownText
    gameCanvas.itemconfigure(countdownText, state="normal")
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
    global gameActive, time, score, paused, randomizeRepeatNum, scoreUpRepeatNum, timeRepeatNum, scoreTimeRepeatNum, ballTextCount, slowTextRepeatNum, unslowRepeatNum, invincibilityTextRepeatNum, disableInvincibilityRepeatNum, slowed, invincible
    countdown()

    # Start all after loops
    randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)
    timeRepeatNum = gameCanvas.after(1000, timer)
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)
    if gameCanvas.coords(abilities[0]) == [0, 0, 0, 0]:
        scoreUpRepeatNum = gameCanvas.after(4000, lambda:updateCoords(0))
    else:
        scoreUpRepeatNum = 0

    # Keep the status of the abilities
    
    if slowTextCount != 0:
        if slowTextCount != 1:
            gameCanvas.itemconfigure(slowTextRectangle, fill="lime")
        else:
            gameCanvas.itemconfigure(slowTextRectangle, fill="red")
        gameCanvas.itemconfigure(slowText, text="Slow Time: " + str(slowTextCount))
        slowTextRepeatNum = gameCanvas.after(1000, updateSlowText)
        unslowRepeatNum = gameCanvas.after(slowTextCount*1000, unslowTime)
    if invincibilityTextCount != 0:
        if invincibilityTextCount != 1:
            gameCanvas.itemconfigure(invincibilityTextRectangle, fill="lime")
        else:
            gameCanvas.itemconfigure(invincibilityTextRectangle, fill="red")
        gameCanvas.itemconfigure(invincibilityText, text="Invincibility: " + str(invincibilityTextCount))
        invincibilityTextRepeatNum = gameCanvas.after(1000, updateInvincibilityText)
        disableInvincibilityRepeatNum = gameCanvas.after(invincibilityTextCount*1000, disableInvincibility)
        gameCanvas.itemconfigure(player, fill="lime")

    # Main game loop
    gameActive = True
    while gameActive and not paused:
        gameCanvas.move(player, playerDirectionX, playerDirectionY)
        moveBalls()
        checkPlayerCollision()
        sleep(0.005)
        displayScore = score
        if ballTextCount == 0: # Create ball every 5 seconds
            ballTextCount = 5
            createBall()
            gameCanvas.itemconfigure(ballTextRectangle, fill="")
        elif ballTextCount == 1:
            gameCanvas.itemconfigure(ballTextRectangle, fill="red")
        gameCanvas.itemconfigure(ballText, text="Time Until Next Ball: " + str(ballTextCount))
        gameCanvas.itemconfigure(scoreText, text="Score: " + str(displayScore))
        gameCanvas.itemconfigure(timeText, text="Time: " + str(time))
        window.update()

    # Go to game over screen once game is finished only if loop wasn't finished by pause
    if paused == False:
        score = int(score)
        finalScoreLabel.configure(text="You scored " + str(score) + " points!\n\nEnter your name to save your score\nor exit to the menu")
        gameCanvas.after_cancel(randomizeRepeatNum) # Stop after loop from randomizing abilities
        gameCanvas.after_cancel(timeRepeatNum)
        gameCanvas.after_cancel(scoreTimeRepeatNum)
        if scoreUpRepeatNum != 0:
            gameCanvas.after_cancel(scoreUpRepeatNum)
        if slowed:
            gameCanvas.after_cancel(slowTextRepeatNum)
            gameCanvas.after_cancel(unslowRepeatNum)
        if invincible:
            gameCanvas.after_cancel(invincibilityTextRepeatNum)
            gameCanvas.after_cancel(disableInvincibilityRepeatNum)
        swapFrames(6) # Game Over screen

def timer():
    '''Adds one second to the universal timer'''
    global time, ballTextCount, timeRepeatNum
    time += 1
    ballTextCount -= 1
    timeRepeatNum = gameCanvas.after(1000, timer)

def increaseScore():
    '''Increases the score by 4 every second.'''
    global score, scoreTimeRepeatNum
    score += 1
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)

def updateHearts():
    global heart, heartBroken, heart1, heart2, heart3, lives
    if lives == 3:
        gameCanvas.itemconfigure(heart1, image=heart)
        gameCanvas.itemconfigure(heart2, image=heart)
        gameCanvas.itemconfigure(heart3, image=heart)
    elif lives == 2:
        gameCanvas.itemconfigure(heart1, image=heartBroken)
        gameCanvas.itemconfigure(heart2, image=heart)
        gameCanvas.itemconfigure(heart3, image=heart)
    elif lives == 1:
        gameCanvas.itemconfigure(heart1, image=heartBroken)
        gameCanvas.itemconfigure(heart2, image=heartBroken)
        gameCanvas.itemconfigure(heart3, image=heart)
    else:
        gameCanvas.itemconfigure(heart1, image=heartBroken)
        gameCanvas.itemconfigure(heart2, image=heartBroken)
        gameCanvas.itemconfigure(heart3, image=heartBroken)

def pause(event):                                    
    '''Pause or unpause the game, and display the paused frame.'''
    global paused, pauseFrameActive, gameActive, randomizeRepeatNum, scoreUpRepeatNum, timeRepeatNum, scoreTimeRepeatNum
    if gameActive == True: # Only change paused state if playing game
        if paused:
            paused = False
            pauseFrameActive = False
            gameCanvas.pack(fill="both", expand=True) # Show game and hide pause frame
            pauseFrame.pack_forget()
            gameLoop()
        else:
            paused = True
            pauseFrameActive = True
            gameCanvas.pack_forget() # Hide game and show pause frame
            pauseFrame.pack(fill="both", expand=True)
            gameCanvas.after_cancel(randomizeRepeatNum) # Stop after loop from randomizing abilities
            gameCanvas.after_cancel(timeRepeatNum)
            gameCanvas.after_cancel(scoreTimeRepeatNum)
            if scoreUpRepeatNum != 0:
                gameCanvas.after_cancel(scoreUpRepeatNum)
            if slowed:
                gameCanvas.after_cancel(slowTextRepeatNum)
                gameCanvas.after_cancel(unslowRepeatNum)
            if invincible:
                gameCanvas.after_cancel(invincibilityTextRepeatNum)
                gameCanvas.after_cancel(disableInvincibilityRepeatNum)


#---------------------------------------------- POWER UP FUNCTIONS -----------------------------------------------------------------------

def randomizeAbility():
    '''Chooses a random ability to put on the screen, or update its position if still on the screen.'''
    global randomizeRepeatNum, previousAbility, abilityNum
    while abilityNum == previousAbility: # New ability cannot be the same as the last one
        abilityNum = randint(1,3)
    previousAbility = abilityNum
    updateCoords(abilityNum)
    randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)

def updateCoords(abilityNum):
    '''Updates the coordinates of a given ability.'''
    global abilities
    xPos = randint(100,1790)
    yPos = randint(100,950)
    gameCanvas.coords(abilities[abilityNum], xPos, yPos, xPos+15, yPos+15)
    gameCanvas.itemconfigure(abilities[abilityNum], state="normal")

def scoreUp():
    '''Increases the score by 30 after the scoreUp power-up is collected.'''
    global score, abilities, scoreUpRepeatNum
    score += 30
    gameCanvas.itemconfigure(abilities[0], state="hidden")
    gameCanvas.coords(abilities[0], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
    scoreUpRepeatNum = gameCanvas.after(4000, lambda:updateCoords(0))

def invincibility(invincibleFromMain):
    '''Gain invincibility from balls after collecting the invinsible ability.'''
    global invincible, invincibilityCount, disableInvincibilityRepeatNum, beenHit
    if invincibleFromMain == True: # If this function was triggered by collecting an ability, increase the count
        invincibilityCount += 1
    if not invincible and invincibilityCount != 0:
        invincible = True
        disableInvincibilityRepeatNum = gameCanvas.after(5000, disableInvincibility)
        updateInvincibilityText()
    gameCanvas.itemconfigure(player, fill="#a1fc03")
    if not beenHit: # Only hide ability if the invincibility didn't occur due to the player being hit
        gameCanvas.coords(abilities[1], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
        gameCanvas.itemconfigure(abilities[1], state="hidden")
    else:
        beenHit = False

def disableInvincibility():
    '''Disabled invincibility after 5 seconds.'''
    global invincible, invincibilityCount
    invincible = False
    gameCanvas.itemconfigure(player, fill="light blue")
    invincibilityCount -= 1
    if invincibilityCount != 0:
        invincibility(False)

def slowTime(slowFromMain):
    '''Slows the balls by half after collecting the slow time ability.'''
    global xSpeed, ySpeed, slowed, slowCount, unslowRepeatNum
    if slowFromMain == True:
        slowCount += 1
    if not slowed and slowCount != 0:
        slowed = True
        xSpeed = [speed/2 for speed in xSpeed]
        ySpeed = [speed/2 for speed in ySpeed]
        unslowRepeatNum = gameCanvas.after(5000, unslowTime)
        updateSlowText()
    gameCanvas.coords(abilities[2], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
    gameCanvas.itemconfigure(abilities[2], state="hidden")

def unslowTime():
    '''Resets all ball speeds by doubling the speed value.'''
    global xSpeed, ySpeed, slowed, slowCount
    slowed = False
    xSpeed = [speed*2 for speed in xSpeed]
    ySpeed = [speed*2 for speed in ySpeed]
    slowCount -= 1
    if slowCount != 0:
        slowTime(False)

def deleteBalls():
    '''Deletes 3 balls randomly after collecting the delete balls ability.'''
    gameCanvas.itemconfigure(abilities[3], state="hidden")
    gameCanvas.coords(abilities[3], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
    global balls, numBalls, xSpeed, ySpeed
    if numBalls <= 2: # If there are less than 3 balls on the screen, get rid of them all
        deleteNum = numBalls
        numBalls -= numBalls
    else: # Else delete 3 balls
        deleteNum = 3
        numBalls -= 3
    for ball in range(deleteNum):
        tempBall = randint(0, len(balls)-1)
        xSpeed.pop(tempBall)
        ySpeed.pop(tempBall)
        tempBall = balls[tempBall]
        balls.remove(tempBall)
        gameCanvas.delete(tempBall)

def updateInvincibilityText():
    '''Updates the invincibility text with the amount of time left.'''
    global invincibilityTextCount, invincibilityTextRepeatNum
    # Update count accordingly
    if invincibilityTextCount == 0:
        invincibilityTextCount = 5
    else:
        invincibilityTextCount -= 1
    gameCanvas.itemconfigure(invincibilityText, text="Invincibility: " + str(invincibilityTextCount))

    # Configure colour of rectangle according to time left
    if invincibilityTextCount >= 3:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="lime")
    elif invincibilityTextCount == 2 or invincibilityTextCount == 1: # Show visible red warning for ability ending soon
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="red")

    # Call function again if timer isn't over
    if invincibilityTextCount != 0:
        invincibilityTextRepeatNum = gameCanvas.after(1000, updateInvincibilityText)
    else:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="")

def updateSlowText():
    '''Updates the slow text with the amount of time left.'''
    global slowTextCount, slowTextRepeatNum
    # Update count accordingly
    if slowTextCount == 0:
        slowTextCount = 5
    else:
        slowTextCount -= 1
    gameCanvas.itemconfigure(slowText, text="Slow Time: " + str(slowTextCount))

    # Configure colour of rectangle according to time left
    if slowTextCount >= 3:
        gameCanvas.itemconfigure(slowTextRectangle, fill="lime")
    elif slowTextCount == 2 or slowTextCount == 1: # Show visible red warning for ability ending soon
        gameCanvas.itemconfigure(slowTextRectangle, fill="red")

    # Call function again if timer isn't over
    if slowTextCount != 0:
        slowTextRepeatNum = gameCanvas.after(1000, updateSlowText)
    else:
        gameCanvas.itemconfigure(slowTextRectangle, fill="")

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
    balls.append(gameCanvas.create_oval(xy, fill="#ff0000", width=2))

    # If slow time ability is active, half speed values
    global slowed
    if slowed == True:
        speedValues = [1, 5]
        colourBounds = [4, 3, 2]
    else:
        speedValues = [2, 10]
        colourBounds = [8, 6, 4]

    # Generate speed values for ball
    tempX = 0
    tempY = 0
    while tempX == 0 and tempY == 0: # Cannot have a ball standing still
        tempX = randint(speedValues[0], speedValues[1]) # Get random speed values for x and y
        tempY = randint(speedValues[0], speedValues[1])
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
    if averageSpeed >= colourBounds[0]:
        gameCanvas.itemconfigure(balls[numBalls], fill="#ff0000", outline="black")
    elif averageSpeed >= colourBounds[1]:
        gameCanvas.itemconfigure(balls[numBalls], fill="#d303fc", outline="black")
    elif averageSpeed >= colourBounds[2]:
        gameCanvas.itemconfigure(balls[numBalls], fill="blue", outline="black")
    else:
        gameCanvas.itemconfigure(balls[numBalls], fill="black", outline="black")
    
    # Increment number of balls
    numBalls += 1

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

#---------------------------------------------- PLAYER FUNCTIONS ----------------------------------------------------

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

def checkPlayerCollision():
    '''Checks if the player is touching a ball, the wall or any abilities.'''
    # Check if player has collided with wall, even with invincibility cheat on
    global gameActive, cheats, abilities, lives
    pos = gameCanvas.coords(player)
    if pos[3] > 1080 or pos[1] < 0 or pos[2] > 1920 or pos[0] < 0:
        gameActive = False

    # Check collision with all abilities
    scoreUpCollision(pos)
    invincibleCollision(pos)
    slowTimeCollision(pos)
    deleteBallsCollision(pos)

    # Only check if player has collided with any ball if invincibility is disabled
    if cheats[1] != True and invincible != True:
        for i in range(len(balls)):
            pos2 = gameCanvas.coords(balls[i])
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
            or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]: # Need to check if either side of player has collided
                hit() # Decrease the lives

def scoreUpCollision(pos):
    '''Takes the players position as argument and checks if they collided with the scoreUp ability'''
    pos2 = gameCanvas.coords(abilities[0])
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
    or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        scoreUp()

def invincibleCollision(pos):
    '''Takes the players position as argument and checks if they collided with the invincible ability'''
    pos2 = gameCanvas.coords(abilities[1])
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
    or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        invincibility(True)

def slowTimeCollision(pos):
    '''Takes the players position as argument and checks if they collided with the slow time ability'''
    pos2 = gameCanvas.coords(abilities[2])
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
    or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        slowTime(True)

def deleteBallsCollision(pos):
    '''Takes the players position as argument and checks if they collided with the delete balls ability'''
    pos2 = gameCanvas.coords(abilities[3])
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
    or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        deleteBalls()

def hit():
    '''Decreases the life if the player is hit, if they are on 0 lives, end the game.'''
    global gameActive, lives, livesTextRectangle, beenHit
    lives -= 1
    beenHit = True
    updateHearts()
    invincibility(True)
    gameCanvas.itemconfigure(livesTextRectangle, fill="#fc0390")
    sleep(0.35)
    gameCanvas.after(1000, lambda:gameCanvas.itemconfigure(livesTextRectangle, fill=""))
    if lives == 0:
        gameActive = False

#---------------------------------------------- SAVE/LOAD GAME FUNCTIONS --------------------------------------------------------

def saveGame(override):
    '''Saves the current state of the game into a text file that can be read from to load the game.'''
    global time, score, numBalls, lives, ballTextCount, slowed, slowTextCount, slowCount, invincible, invincibilityTextCount, invincibilityCount, balls, xSpeed, ySpeed, saved, cheated
    if saved == True:
        saveBtn.configure(text="Already saved.")
    else:
        saveFile = open("save.txt", "r")
        line = saveFile.readline().strip()
        saveFile.close()
        if line != "" and override == False:
            pauseInfoLabel.configure(text="Do you want to override\nthe last save?")
            saveBtn.configure(text="Yes", command=lambda:overrideSave(True))
            pauseHomeBtn.configure(text="No", command=lambda:overrideSave(False))
            window.unbind("<Escape>")
        else:
            override = True
        if override == True: # Save the game variables
            saveFile = open("save.txt", "w")
            saveFile.write(str(time) + "\n")
            saveFile.write(str(score) + "\n")
            saveFile.write(str(numBalls) + "\n")
            saveFile.write(str(lives) + "\n")
            saveFile.write(str(ballTextCount) + "\n")
            saveFile.write(str(slowed) + "\n")
            saveFile.write(str(slowTextCount) + "\n")
            saveFile.write(str(slowCount) + "\n")
            saveFile.write(str(invincible) + "\n")
            saveFile.write(str(invincibilityTextCount) + "\n")
            saveFile.write(str(invincibilityCount) + "\n")
            playerPos = gameCanvas.coords(player) # Write player coordinates
            if cheats[0] == True: # If they used the 'smaller player' cheat, increase the size back to normal
                for coordinate in range(4):
                    if coordinate <= 1:
                        saveFile.write(str(playerPos[coordinate]-15) + "\n")
                    else:
                        saveFile.write(str(playerPos[coordinate]+15) + "\n")
            else: # Else save the normal coordinates
                for coordinate in range(4):
                    saveFile.write(str(playerPos[coordinate]) + "\n")
            for ability in abilities:
                tempCoords = gameCanvas.coords(ability)
                for coordinate in tempCoords:
                    saveFile.write(str(coordinate) + "\n")
            for variable in range(3):
                for ball in range(numBalls):
                    if variable == 0: # Write all ball coordinates
                        ballPos = gameCanvas.coords(balls[ball])
                        for coordinate in ballPos:
                            saveFile.write(str(coordinate) + "\n")
                        saveFile.write(gameCanvas.itemcget(balls[ball], "fill") + "\n")
                    elif variable == 1: # Write all x speeds
                        saveFile.write(str(xSpeed[ball]) + "\n")
                    else: # Write all y speeds
                        saveFile.write(str(ySpeed[ball]) + "\n")
            if cheats[0] == True or cheats[1] == True or cheated == True:
                saveFile.write("True\n")
            else:
                saveFile.write("False\n")
            saveFile.close()
            saveBtn.configure(text="Saved!")
            saved = True
            gameCanvas.after(1000, lambda:swapFrames(0))

def overrideSave(override):
    '''Decides whether to override the save file or not.'''
    if override == True:
        pauseInfoLabel.configure(text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.")
        saveBtn.configure(command=lambda:saveGame(False))
        pauseHomeBtn.configure(text="Home", command=lambda:swapFrames(0))
        window.bind("<Escape>", pause)
        saveGame(True)
    else:
        pauseInfoLabel.configure(text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.")
        saveBtn.configure(text="Save Game", command=lambda:saveGame(False))
        pauseHomeBtn.configure(text="Home", command=lambda:swapFrames(0))
        window.bind("<Escape>", pause)

def loadGame():
    '''Loads a game from the save.txt file, or ignores if game not found.'''
    saveFile = open("save.txt", "r")
    temp = saveFile.readline().strip()
    if temp == "":
        loadBtn.configure(text="No Game Found")
        window.after(1000, lambda:loadBtn.configure(text="Load Game"))
    else:
        global saveExists, loaded, time, score, numBalls, lives, ballTextCount, slowed, slowTextCount, slowCount, invincible, invincibilityTextCount, invincibilityCount, playerCoords, abilityCoords, ballPos, xSpeed, ySpeed, cheated
        saveExists = False
        loaded = True
        time = int(temp)
        score = int(saveFile.readline().strip())
        numBalls = int(saveFile.readline().strip())
        lives = int(saveFile.readline().strip())
        ballTextCount = int(saveFile.readline().strip())
        slowed = saveFile.readline().strip()
        if slowed == "False": # Cannot immediately convert string to boolean
            slowed = False
        else:
            slowed = True
        slowTextCount = int(saveFile.readline().strip())
        slowCount = int(saveFile.readline().strip())
        invincible = saveFile.readline().strip()
        if invincible == "False": # Cannot immediately convert string to boolean
            invincible = False
        else:
            invincible = True
        invincibilityTextCount = int(saveFile.readline().strip())
        invincibilityCount = int(saveFile.readline().strip())
        playerCoords = []
        abilityCoords = []
        ballPos = []
        xSpeed = []
        ySpeed = []

        # Load the player's coordinates
        for coordinate in range(4):
            playerCoords.append(float(saveFile.readline().strip()))
        playerCoords = (playerCoords[0], playerCoords[1], playerCoords[2], playerCoords[3])

        # Load the ability coordinates
        for ability in range(4):
            tempCoords = []
            for coordinate in range(4):
                coordinate = saveFile.readline().strip()
                tempCoords.append(coordinate)
            abilityCoords.append((tempCoords[0], tempCoords[1], tempCoords[2], tempCoords[3]))

        for variable in range(3):
            for ball in range(numBalls):
                if variable == 0:
                    tempBallPos = []
                    for coordinate in range(4):
                        tempBallPos.append(float(saveFile.readline().strip()))
                    colour = saveFile.readline().strip()
                    tempBallPos.append(colour)
                    ballPos.append(tempBallPos)
                elif variable == 1:
                    xSpeed.append(float(saveFile.readline().strip()))
                else:
                    ySpeed.append(float(saveFile.readline().strip()))

        cheated = bool(saveFile.readline().strip())

        saveFile.close()

        # Erase the save
        open("save.txt", "w").close()

        initialiseGame(True)

#---------------------------------------------- MAIN PROGRAM --------------------------------------------------------

configureWindow() # Set up the window
initialiseMenu() # Set up the menu
changeBackground(bgColour) # Set up initial background colour
initialiseKeybinds() # Set up the initial keybinds
homeFrame.pack(fill="both", expand=True) # Start at the home page

window.mainloop()