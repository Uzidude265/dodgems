# OBJECTIVES:
# 1. SAVE FUNCTION
# 2. ADD TIME TO LEADERBOARD
# 3. MAKE SCORE CORRELATED TO TIME

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
    defaultsBtn = Btn(settingsFrame, width=25, height=1, text="Reset to Default Settings", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=defaultSettings)
    cheatsBtn = Btn(settingsFrame, width=25, height=1, text="Cheats", bg="red", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=None)
    settingsHomeBtn = Btn(settingsFrame, width=25, height=1, text="Home", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda:swapFrames(0))

    # SETTINGS FRAME PACKING
    settingsLabel.pack(side="top", pady=(150, 0))
    bgBtn.pack(side="top", pady=(130, 0))
    keybindsBtn.pack(side="top", pady=(20, 0))
    defaultsBtn.pack(side="top", pady=(20, 0))
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

    # PAUSE FRAME WIDGETS
    pauseLabel = Label(pauseFrame, width=30, height=4, bg="pink", text="GAME PAUSED", font=("Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    pauseInfoLabel = Label(pauseFrame, width=30, height=6, bg="pink", text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.", font=("Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    saveBtn = Btn(pauseFrame, width=25, height=1, text="Save Game", bg="light blue", activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=saveGame)
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
        settingsFrame.pack_forget()
        leaderboardFrame.pack_forget()
        infoFrame.pack_forget()
        gameOverFrame.pack_forget()
        pauseFrame.pack_forget()
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
            gameCanvas.after_cancel(scoreUpRepeatNum)
            gameCanvas.after_cancel(timeRepeatNum)
            gameCanvas.after_cancel(scoreTimeRepeatNum)
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
    style.configure("Treeview", fieldbackground="pink", font=("Comic Sans MS", 15, "bold"), rowheight=35)
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
        newEntry = [name, str(displayTime), str(score)]
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
    global time, displayTime, score, numBalls, balls, xSpeed, ySpeed, playerDirectionX, playerDirectionY
    time = 0
    displayTime = 0
    score = 0
    numBalls = 0
    balls = [] # Stores all the balls created
    xSpeed = [] # Stores speed values for each ball
    ySpeed = []
    playerDirectionX = 7
    playerDirectionY = 0

    # Create all abilities
    global abilities, slowed, slowCount, invincible, invincibleCount
    abilities = []
    abilities.append(gameCanvas.create_rectangle(0, 0, 0, 0, fill="lime", outline="black", width=2, state="hidden")) # scoreUp ability
    abilities.append(gameCanvas.create_rectangle(0, 0, 0, 0, fill="white", outline="black", width=2, state="hidden")) # invincibility ability
    abilities.append(gameCanvas.create_rectangle(0, 0, 0, 0, fill="orange", outline="black", width=2, state="hidden")) # slow time ability
    abilities.append(gameCanvas.create_rectangle(0, 0, 0, 0, fill="cyan", outline="black", width=2, state="hidden")) # delete balls ability
    slowed = False
    slowCount = 0 # Stores how many slow time power ups they have collected
    invincible = False
    invincibleCount = 0 # Stores how many invincible power ups they have collected

    # Create player
    global player
    if cheats[0] == True: # If smaller player cheat is enabled, make smaller player
        xy = (950, 530, 970, 550)
    else:
        xy = (935, 515, 985, 565)
    player = gameCanvas.create_rectangle(xy, fill="light blue", outline="black", width=2)

    # Make all text and rectangles behind the text
    global scoreText, invincibilityText, invincibilityTextRectangle, invincibilityTextCount, slowText, slowTextCount, slowTextRectangle, timeText, timeTextCount, ballText, ballTextCount, ballTextRectangle, countdownText
    scoreText = gameCanvas.create_text(1825, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(scoreText)
    scoreTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    invincibilityText = gameCanvas.create_text(135, 30, text="Invincibility: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(invincibilityText)
    invincibilityTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    invincibilityTextCount = 0
    gameCanvas.lower(invincibilityTextRectangle, invincibilityText) # Puts the rectangle behind the text
    slowText = gameCanvas.create_text(385, 30, text="Slow Time: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(slowText)
    slowTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    slowTextCount = 0
    gameCanvas.lower(slowTextRectangle, slowText) # Puts the rectangle behind the text
    timeText = gameCanvas.create_text(1650, 30, text="Time: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(timeText)
    timeTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    timeTextCount = 0
    gameCanvas.lower(timeTextRectangle, timeText) # Puts the rectangle behind the text
    ballText = gameCanvas.create_text(960, 30, text="Time Until Next Ball: 5", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(ballText)
    ballTextRectangle = gameCanvas.create_rectangle(bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    ballTextCount = 0
    gameCanvas.lower(ballTextRectangle, ballText) # Puts the rectangle behind the text
    countdownText = gameCanvas.create_text(960, 540, text="3", font=("Comic Sans MS", 75, "bold"))

    # Start with 1 ball
    createBall()
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
    global gameActive, time, score, paused, randomizeRepeatNum, scoreUpRepeatNum, timeRepeatNum, scoreTimeRepeatNum, ballTextCount
    countdown()

    # Start all after loops
    randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)
    scoreUpRepeatNum = gameCanvas.after(4000, lambda:updateCoords(0))
    timeRepeatNum = gameCanvas.after(1000, timer)
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)
    
    gameActive = True
    while gameActive and not paused:
        gameCanvas.move(player, playerDirectionX, playerDirectionY)
        moveBalls()
        checkPlayerCollision()
        sleep(0.005)
        displayScore = score
        if time % 6 == 5: # Create ball every 5 seconds
            time = 0
            createBall()
        if ballTextCount == 0:
            ballTextCount = 5
            gameCanvas.itemconfigure(ballTextRectangle, fill="")
        elif ballTextCount == 1:
            gameCanvas.itemconfigure(ballTextRectangle, fill="red")
        gameCanvas.itemconfigure(ballText, text="Time Until Next Ball: " + str(ballTextCount))
        gameCanvas.itemconfigure(scoreText, text="Score: " + str(displayScore))
        gameCanvas.itemconfigure(timeText, text="Time: " + str(displayTime))
        window.update()

    # Go to game over screen once game is finished only if loop wasn't finished by pause
    if paused == False:
        score = int(score)
        finalScoreLabel.configure(text="You scored " + str(score) + " points!\n\nEnter your name to save your score\nor exit to the menu")
        gameCanvas.after_cancel(randomizeRepeatNum) # Stop after loop from randomizing abilities
        gameCanvas.after_cancel(scoreUpRepeatNum)
        gameCanvas.after_cancel(timeRepeatNum)
        gameCanvas.after_cancel(scoreTimeRepeatNum)
        swapFrames(6)

def timer():
    '''Adds one second to the universal timer'''
    global time, displayTime, ballTextCount, timeRepeatNum
    time += 1
    displayTime += 1
    ballTextCount -= 1
    timeRepeatNum = gameCanvas.after(1000, timer)

def increaseScore():
    '''Increases the score by 4 every second.'''
    global score, scoreTimeRepeatNum
    score += 1
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)

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
            gameCanvas.after_cancel(scoreUpRepeatNum)
            gameCanvas.after_cancel(timeRepeatNum)
            gameCanvas.after_cancel(scoreTimeRepeatNum)

#---------------------------------------------- POWER UP FUNCTIONS -----------------------------------------------------------------------

def randomizeAbility():
    '''Chooses a random ability to put on the screen, or update its position if still on the screen.'''
    global randomizeRepeatNum
    abilityNum = randint(1,3)
    updateCoords(abilityNum)
    randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)

def updateCoords(abilityNum):
    '''Updates the coordinates of a given ability.'''
    global abilities
    xPos = randint(50,1870)
    yPos = randint(50,1030)
    gameCanvas.coords(abilities[abilityNum], xPos, yPos, xPos+15, yPos+15)
    gameCanvas.itemconfigure(abilities[abilityNum], state="normal")

def scoreUp():
    '''Increases the score by 20 after the scoreUp power-up is collected.'''
    global score, abilities, scoreUpRepeatNum
    score += 20
    gameCanvas.itemconfigure(abilities[0], state="hidden")
    gameCanvas.coords(abilities[0], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
    scoreUpRepeatNum = gameCanvas.after(4000, lambda:updateCoords(0))

def invincibility(invincibleFromMain):
    '''Gain invincibility from balls after collecting the invinsible ability.'''
    global invincible, invincibleCount
    if invincibleFromMain == True: # If this function was triggered by collecting an ability, increase the count
        invincibleCount += 1
    if not invincible and invincibleCount != 0:
        invincible = True
        gameCanvas.after(5000, disableInvincibility)
        updateInvincibilityText()
    gameCanvas.coords(abilities[1], 0, 0, 0, 0) # Move scoreUp to top right to prevent overchecking collisions
    gameCanvas.itemconfigure(abilities[1], state="hidden")
    gameCanvas.itemconfigure(player, fill="#a1fc03")

def disableInvincibility():
    '''Disabled invincibility after 5 seconds.'''
    global invincible, invincibleCount
    invincible = False
    gameCanvas.itemconfigure(player, fill="light blue")
    invincibleCount -= 1
    if invincibleCount != 0:
        invincibility(False)

def slowTime(slowFromMain):
    '''Slows the balls by half after collecting the slow time ability.'''
    global xSpeed, ySpeed, slowed, slowCount
    if slowFromMain == True:
        slowCount += 1
    if not slowed and slowCount != 0:
        slowed = True
        xSpeed = [speed/2 for speed in xSpeed]
        ySpeed = [speed/2 for speed in ySpeed]
        gameCanvas.after(5000, unslowTime)
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
    global balls, numBalls
    if numBalls <= 2: # If there are less than 3 balls on the screen, get rid of them all
        deleteNum = numBalls
        numBalls -= numBalls
    else: # Else delete 3 balls
        deleteNum = 3
        numBalls -= 3
    for ball in range(deleteNum):
        tempBall = randint(0, len(balls)-1)
        tempXSpeed = xSpeed[tempBall]
        xSpeed.remove(tempXSpeed)
        tempYSpeed = ySpeed[tempBall]
        ySpeed.remove(tempYSpeed)
        tempBall = balls[tempBall]
        balls.remove(tempBall)
        gameCanvas.delete(tempBall)

def updateInvincibilityText():
    '''Updates the invincibility text with the amount of time left.'''
    global invincibilityTextCount
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
        gameCanvas.after(1000, updateInvincibilityText)
    else:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="")

def updateSlowText():
    '''Updates the slow text with the amount of time left.'''
    global slowTextCount
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
        gameCanvas.after(1000, updateSlowText)
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
    global gameActive, cheats, abilities
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
                gameActive = False

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

#---------------------------------------------- SAVE CURRENT GAME --------------------------------------------------------

def saveGame():
    pass

#---------------------------------------------- MAIN PROGRAM --------------------------------------------------------

configureWindow() # Set up the window
initialiseMenu() # Set up the menu
changeBackground(bgColour) # Set up initial background colour
initialiseKeybinds() # Set up the initial keybinds
homeFrame.pack(fill="both", expand=True) # Start at the home page

window.mainloop()