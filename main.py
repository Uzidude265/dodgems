# SCREEN RESOLUTION: 1920x1080

# FUNCTION CHUNKS:
# 1. MENU FUNCTIONS
# 2. SETTINGS FUNCTIONS
# 3. LEADERBOARD FUNCTIONS
# 4. HOW TO PLAY FUNCTIONS
# 5. CHEAT CODE FUNCTIONS
# 6. GAME FUNCTIONS
# 7. POWER UP FUNCTIONS
# 8. BALL FUNCTIONS
# 9. PLAYER FUNCTIONS
# 10. SAVE/LOAD GAME FUNCTIONS
# 11. MAIN PROGRAM

from tkinter import Tk, Frame, Button as Btn, Label, PhotoImage as Image, \
    Canvas, Checkbutton as CheckBtn, ttk, Entry, messagebox
from time import sleep
from random import randint
import ctypes

# Fixes DPI issue that caused window dimensions to be off
ctypes.windll.shcore.SetProcessDpiAwareness(2)


# ---------------------------------------------- MENU FUNCTIONS --------------------------------------------------------------


def configureWindow():
    '''Creates a Tk object "window" and changes its attributes.'''
    global window
    window = Tk()
    window.title("Dodgems")
    window.geometry("1920x1080")
    window.attributes('-fullscreen', True)


def initialiseMenu():
    '''Sets up the menu functionality, including the home page, settings page, leaderboard page, info page, and all respective titles and buttons.'''
    initialiseSettings()
    initialiseHowToPlay()

    # FRAMES
    global homeFrame, settingsFrame, leaderboardFrame, infoFrame, gameOverFrame, playerColourFrame, \
        bgFrame, keybindsFrame, cheatsFrame, bossFrame, pauseFrame
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)
    playerColourFrame = Frame(window)
    bgFrame = Frame(window)
    keybindsFrame = Frame(window)
    cheatsFrame = Frame(window)
    bossFrame = Frame(window)
    pauseFrame = Frame(window)

    # HOME FRAME WIDGETS
    global logo, loadBtn
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    playBtn = Btn(homeFrame, width=25, height=1, text="Play", bg="light blue", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: initialiseGame(False))
    loadBtn = Btn(homeFrame, width=25, height=1, text="Load Game", bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=loadGame)
    settingsBtn = Btn(homeFrame, width=25, height=1, text="Settings", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))
    leaderboardBtn = Btn(homeFrame, width=25, height=1, text="Leaderboard", bg="light blue",
                         activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(4))
    infoBtn = Btn(homeFrame, width=25, height=1, text="How to Play", bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(5))
    exitBtn = Btn(homeFrame, width=25, height=1, text="Exit", bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=exitGame)

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
    settingsLabel = Label(settingsFrame, width=30, height=4, bg="pink", text="SETTINGS", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    playerColourBtn = Btn(settingsFrame, width=25, height=1, text="Change Player Colour", bg="light blue",
                          activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(8))
    bgBtn = Btn(settingsFrame, width=25, height=1, text="Change Background Colour", bg="light blue",
                activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(2))
    keybindsBtn = Btn(settingsFrame, width=25, height=1, text="Change Keybinds", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(3))
    defaultsBtn = Btn(settingsFrame, width=25, height=1, text="Reset to Default Settings", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=defaultSettings)
    cheatsBtn = Btn(settingsFrame, width=25, height=1, text="Cheats", bg="red",
                    activebackground="cyan", font=("Comic Sans MS", 15, "bold"),
                    command=lambda: messagebox.showerror(title="NOT UNLOCKED", message="You haven't unlocked the cheats yet."))
    settingsHomeBtn = Btn(settingsFrame, width=25, height=1, text="Home", bg="light blue",
                          activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))

    # SETTINGS FRAME PACKING
    settingsLabel.pack(side="top", pady=(150, 0))
    playerColourBtn.pack(side="top", pady=(95, 0))
    bgBtn.pack(side="top", pady=(10, 0))
    keybindsBtn.pack(side="top", pady=(10, 0))
    defaultsBtn.pack(side="top", pady=(10, 0))
    cheatsBtn.pack(side="top", pady=(10, 0))
    settingsHomeBtn.pack(side="top", pady=(95, 0))

    # PLAYER COLOUR FRAME WIDGETS
    playerColourLabel = Label(playerColourFrame, width=30, height=4, bg="pink", text="CHANGE PLAYER COLOUR", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    bluePlayerBtn = Btn(playerColourFrame, width=25, height=1, text="Blue", bg="light blue", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changePlayerColour("light blue"))
    orangePlayerBtn = Btn(playerColourFrame, width=25, height=1, text="Orange", bg="orange", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changePlayerColour("orange"))
    greenPlayerBtn = Btn(playerColourFrame, width=25, height=1, text="Green", bg="green", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changePlayerColour("green"))
    purplePlayerBtn = Btn(playerColourFrame, width=25, height=1, text="Purple", bg="purple", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changePlayerColour("purple"))
    playerColourSettingsBtn = Btn(playerColourFrame, width=25, height=1, text="Back to Settings", bg="light blue",
                                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))

    # PLAYER COLOUR FRAME PACKING
    playerColourLabel.pack(side="top", pady=(150, 0))
    bluePlayerBtn.pack(side="top", pady=(110, 0))
    orangePlayerBtn.pack(side="top", pady=(20, 0))
    greenPlayerBtn.pack(side="top", pady=(20, 0))
    purplePlayerBtn.pack(side="top", pady=(20, 0))
    playerColourSettingsBtn.pack(side="top", pady=(110, 0))

    # BACKGROUND COLOUR FRAME WIDGETS
    bgLabel = Label(bgFrame, width=30, height=4, bg="pink", text="CHANGE BACKGROUND COLOUR", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    blueBgBtn = Btn(bgFrame, width=25, height=1, text="Blue", bg="#8ec8fa", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changeBackground("#8ec8fa"))
    greenBgBtn = Btn(bgFrame, width=25, height=1, text="Green", bg="#cbf7e6", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changeBackground("#cbf7e6"))
    redBgBtn = Btn(bgFrame, width=25, height=1, text="Red", bg="#edd3dc", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changeBackground("#edd3dc"))
    yellowBgBtn = Btn(bgFrame, width=25, height=1, text="Yellow", bg="#fffcc2", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda: changeBackground("#fffcc2"))
    bgSettingsBtn = Btn(bgFrame, width=25, height=1, text="Back to Settings", bg="light blue",
                        activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))

    # BACKGROUND COLOUR FRAME PACKING
    bgLabel.pack(side="top", pady=(150, 0))
    blueBgBtn.pack(side="top", pady=(110, 0))
    greenBgBtn.pack(side="top", pady=(20, 0))
    redBgBtn.pack(side="top", pady=(20, 0))
    yellowBgBtn.pack(side="top", pady=(20, 0))
    bgSettingsBtn.pack(side="top", pady=(110, 0))

    # KEYBIND FRAME WIDGETS
    global upBtn, downBtn, leftBtn, rightBtn, bossKeyBtn, keybindsSettingsBtn, keybindsPromptLabel
    # Remove the < > from the controls to add to the corresponding button's text
    tempUp = controls[0]
    tempUp = tempUp[1:len(tempUp)-1]
    tempDown = controls[1]
    tempDown = tempDown[1:len(tempDown)-1]
    tempLeft = controls[2]
    tempLeft = tempLeft[1:len(tempLeft)-1]
    tempRight = controls[3]
    tempRight = tempRight[1:len(tempRight)-1]
    tempBossKey = controls[4]
    tempBossKey = tempBossKey[1:len(tempBossKey)-1]
    keybindsLabel = Label(keybindsFrame, width=30, height=4, bg="pink", text="CHANGE KEYBINDS", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    keybindsPromptLabel = Label(keybindsFrame, width=50, height=2, bg="pink", text="Click a keybind to change", font=(
        "Comic Sans MS", 15, "bold"), borderwidth=3, relief="solid")
    upBtn = Btn(keybindsFrame, width=25, height=1, text="Up: " + tempUp, bg="light blue",
                activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: setKeybindChange(0))
    downBtn = Btn(keybindsFrame, width=25, height=1, text="Down: " + tempDown, bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: setKeybindChange(1))
    leftBtn = Btn(keybindsFrame, width=25, height=1, text="Left: " + tempLeft, bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: setKeybindChange(2))
    rightBtn = Btn(keybindsFrame, width=25, height=1, text="Right: " + tempRight, bg="light blue",
                   activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: setKeybindChange(3))
    bossKeyBtn = Btn(keybindsFrame, width=25, height=1, text="Boss Key: " + tempBossKey, bg="light blue",
                     activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: setKeybindChange(4))
    keybindsSettingsBtn = Btn(keybindsFrame, width=25, height=1, text="Back to Settings", bg="light blue",
                              activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))

    # KEYBIND FRAME PACKING
    keybindsLabel.pack(side="top", pady=(150, 0))
    keybindsPromptLabel.pack(side="top", pady=(30, 0))
    upBtn.pack(side="top", pady=(45, 0))
    downBtn.pack(side="top", pady=(10, 0))
    leftBtn.pack(side="top", pady=(10, 0))
    rightBtn.pack(side="top", pady=(10, 0))
    bossKeyBtn.pack(side="top", pady=(10, 0))
    keybindsSettingsBtn.pack(side="top", pady=(50, 0))

    # CHEATS FRAME WIDGETS
    cheatsLabel = Label(cheatsFrame, width=30, height=4, bg="pink", text="CHEATS", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    smallerPlayerBtn = CheckBtn(cheatsFrame, width=25, height=2, text="Smaller Player", bg="light blue",
                                activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeCheats(0))
    invincibilityBtn = CheckBtn(cheatsFrame, width=25, height=2, text="Invincible", bg="light blue",
                                activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeCheats(1))
    halfCooldownBtn = CheckBtn(cheatsFrame, width=25, height=2, text="Half Ability Cooldowns", bg="light blue",
                               activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeCheats(2))
    cheatsHomeBtn = Btn(cheatsFrame, width=25, height=1, text="Back to Settings", bg="light blue",
                        activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))

    # CHEATS FRAME PACKING
    cheatsLabel.pack(side="top", pady=(150, 0))
    smallerPlayerBtn.pack(side="top", pady=(110, 0))
    invincibilityBtn.pack(side="top", pady=(20, 0))
    halfCooldownBtn.pack(side="top", pady=(20, 0))
    cheatsHomeBtn.pack(side="top", pady=(120, 0))

    # LEADERBOARD FRAME WIDGETS
    leaderboardLabel = Label(leaderboardFrame, width=30, height=4, bg="pink", text="LEADERBOARD", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    leaderboardHomeBtn = Btn(leaderboardFrame, width=25, height=1, text="Home", bg="light blue",
                             activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))
    createLeaderboard()

    # LEADERBOARD FRAME PACKING
    leaderboardLabel.pack(side="top", pady=(150, 0))
    leaderboard.pack(side="top", pady=(45, 0))
    leaderboardHomeBtn.pack(side="top", pady=(40, 0))

    # INFO FRAME WIDGETS
    global howToPlayLabel
    infoLabel = Label(infoFrame, width=30, height=4, bg="pink", text="HOW TO PLAY", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    cheatsInfoBtn = Btn(infoFrame, width=30, height=1, text="", bg="pink",
                        activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeInfoLabel(howToPlay[4]))
    howToPlayLabel = Label(infoFrame, width=70, height=14, bg="pink", text=howToPlay[0], font=(
        "Comic Sans MS", 14, "bold"), borderwidth=3, relief="solid")
    gameInfoBtn = Btn(infoFrame, width=15, height=1, text="Main Game", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeInfoLabel(howToPlay[0]))
    abilityInfoBtn = Btn(infoFrame, width=15, height=1, text="Abilities", bg="light blue",
                         activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeInfoLabel(howToPlay[1]))
    gameFeaturesInfoBtn = Btn(infoFrame, width=15, height=1, text="Game Features", bg="light blue",
                              activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeInfoLabel(howToPlay[3]))
    tipsInfoBtn = Btn(infoFrame, width=15, height=1, text="Tips", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: changeInfoLabel(howToPlay[2]))
    infoHomeBtn = Btn(infoFrame, width=15, height=1, text="Home", bg="light blue",
                      activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))

    # INFO FRAME PACKING
    infoLabel.pack(side="top", pady=(150, 0))
    cheatsInfoBtn.pack(side="top", pady=(5, 0))
    howToPlayLabel.pack(side="top", pady=(5, 0))
    gameInfoBtn.pack(side="left", anchor="nw", pady=(30, 0), padx=(430, 0))
    abilityInfoBtn.pack(side="left", anchor="nw", pady=(30, 0), padx=(30, 0))
    gameFeaturesInfoBtn.pack(side="left", anchor="nw",
                             pady=(30, 0), padx=(30, 0))
    tipsInfoBtn.pack(side="left", anchor="nw", pady=(30, 0), padx=(30, 0))
    infoHomeBtn.pack(side="left", anchor="nw", pady=(30, 0), padx=(30, 0))

    # PAUSE FRAME WIDGETS
    global pauseInfoLabel, saveBtn, pauseHomeBtn
    pauseLabel = Label(pauseFrame, width=30, height=4, bg="pink", text="GAME PAUSED", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    pauseInfoLabel = Label(pauseFrame, width=30, height=6, bg="pink", text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.",
                           font=("Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    saveBtn = Btn(pauseFrame, width=25, height=1, text="Save Game", bg="light blue",
                  activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: saveGame(False))
    pauseHomeBtn = Btn(pauseFrame, width=25, height=1, text="Home", bg="light blue",
                       activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))

    # PAUSE FRAME PACKING
    pauseLabel.pack(side="top", pady=(150, 0))
    pauseInfoLabel.pack(side="top", pady=(100, 0))
    saveBtn.pack(side="top", pady=(100, 0))
    pauseHomeBtn.pack(side="top", pady=(20, 0))

    # GAME OVER FRAME WIDGETS
    global finalScoreLabel, nameInput, submitBtn
    gameOverLabel = Label(gameOverFrame, width=30, height=4, bg="pink", text="GAME OVER!", font=(
        "Comic Sans MS", 20, "bold"), borderwidth=3, relief="solid")
    finalScoreLabel = Label(gameOverFrame, width=30, height=5, bg="pink", text="", font=(
        "Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    nameInput = Entry(gameOverFrame, width=30, bg="#aeeafc", font=(
        "Comic Sans MS", 20, "bold"), justify="center")
    submitBtn = Btn(gameOverFrame, width=25, height=1, text="Submit Name", bg="light blue",
                    activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=addToLeaderboard)
    gameOverHomeBtn = Btn(gameOverFrame, width=25, height=1, text="Home", bg="light blue",
                          activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))

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
    if frameNum == 0:  # Swap to the home frame
        global paused, gameActive
        settingsFrame.pack_forget()
        leaderboardFrame.pack_forget()
        infoFrame.pack_forget()
        gameOverFrame.pack_forget()
        pauseFrame.pack_forget()
        homeFrame.pack(fill="both", expand=True)
        nameInput.delete(0, "end")  # Get rid of text in entry box
        # Disable entry box after going back home
        nameInput.configure(state="disabled")
        paused = False
        gameActive = False
        if slowed:  # Pause any remaining after loops
            gameCanvas.after_cancel(slowTextRepeatNum)
            gameCanvas.after_cancel(unslowRepeatNum)
        if invincible:
            gameCanvas.after_cancel(invincibilityTextRepeatNum)
            gameCanvas.after_cancel(disableInvincibilityRepeatNum)
    elif frameNum == 1:  # Swap to the settings frame
        homeFrame.pack_forget()
        playerColourFrame.pack_forget()
        bgFrame.pack_forget()
        keybindsFrame.pack_forget()
        cheatsFrame.pack_forget()
        settingsFrame.pack(fill="both", expand=True)
    elif frameNum == 2:  # Swap to the background colour frame
        settingsFrame.pack_forget()
        bgFrame.pack(fill="both", expand=True)
    elif frameNum == 3:  # Swap to the keybinds frame
        settingsFrame.pack_forget()
        keybindsFrame.pack(fill="both", expand=True)
    elif frameNum == 4:  # Swap to the leaderboard frame
        homeFrame.pack_forget()
        leaderboardFrame.pack(fill="both", expand=True)
    elif frameNum == 5:  # Swap to the info frame
        homeFrame.pack_forget()
        infoFrame.pack(fill="both", expand=True)
    elif frameNum == 6:  # Swap to the game over frame
        gameCanvas.pack_forget()
        gameOverFrame.pack(fill="both", expand=True)
        submitBtn.configure(bg="light blue", relief="raised",
                            command=addToLeaderboard)  # Reset submit button
        nameInput.configure(state="normal")  # Re-enable entry box
    elif frameNum == 7:  # Swap to the cheats frame
        settingsFrame.pack_forget()
        cheatsFrame.pack(fill="both", expand=True)
    else:  # Swap to the player colour frame
        settingsFrame.pack_forget()
        playerColourFrame.pack(fill="both", expand=True)


def bossKey(event):
    '''Activates whenever the boss key is pressed and displays an unsuspecting image.'''
    global gameActive, bossEnabled, paused, pauseFrameActive, randomizeRepeatNum, \
        scoreUpRepeatNum, timeRepeatNum, scoreTimeRepeatNum
    # If at menu, place boss frame on top
    if gameActive == False:
        if bossEnabled == True:
            bossEnabled = False
            bossFrame.place_forget()
        else:
            bossEnabled = True
            bossFrame.place(x=0, y=0)

    # If game active, pause the game and hide gameCanvas
    elif gameActive == True and pauseFrameActive == False:
        if bossEnabled == True:
            bossEnabled = False
            paused = False
            bossFrame.pack_forget()
            gameCanvas.pack(fill="both", expand=True)
            window.bind("<Escape>", pause)
            gameLoop()  # Re-run game loop after unpausing
        else:
            bossEnabled = True
            paused = True
            gameCanvas.pack_forget()
            bossFrame.pack(fill="both", expand=True)
            # Stop after loops
            gameCanvas.after_cancel(randomizeRepeatNum)
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
            window.unbind("<Escape>")

    # Else if the pause frame is showing, replace with boss frame
    elif pauseFrameActive == True:
        if bossEnabled == True:
            bossEnabled = False
            bossFrame.place_forget()
            pauseFrame.pack(fill="both", expand=True)
            window.bind("<Escape>", pause)
        else:
            bossEnabled = True
            pauseFrame.pack_forget()
            bossFrame.place(x=0, y=0)
            window.unbind("<Escape>")


def exitGame():
    '''Save all settings and current leaderboard state, then close the game.'''
    answer = messagebox.askquestion(
        title="Exit", message="Are you sure you want to quit?")
    if answer == "yes":
        saveSettings()
        saveLeaderboard()
        window.destroy()


# ---------------------------------------------- SETTINGS FUNCTIONS --------------------------------------------------------------------


def initialiseSettings():
    '''Initialise all the settings and read settings.txt file to get saved settings.'''
    # Initialise unsaved settings
    global triggeredKeybindChange, keybindNum, controls, bgColour, playerColour, previousBind, \
        howToPlayText, cheatCode, cheats, bossEnabled, gameActive, paused, pauseFrameActive, slowed, invincible
    triggeredKeybindChange = False  # Checks if player clicked button to change keybind
    keybindNum = 0
    previousBind = ""  # Used when unbinding previous key
    howToPlayText = "Dodge the never-ending balls as long as you can!" \
        + "\n\nThe colour of the balls indicates their speed." \
        + "\n(Black = Slow, Blue = Medium, Purple = Fast, Red = Very Fast)" \
        + "\nEvery 5 seconds, a new ball gets added at the sides, so watch out!" \
        + "\n\nThere are numerous abilities to help you out:" \
        + "\nGreen Square: +30 Points\nWhite Square: Invincibility" \
        + "\nOrange Square: Slow Time\nBlue Square: Delete 3 Random Balls" \
        + "\n\nP.S. Touching the walls is an instakill!\n\nGood Luck!"
    cheatCode = ""  # Keeps track of keys pressed to check if they enter a cheat code
    cheats = [False, False, False]  # Checks what cheats are enabled
    bossEnabled = False
    gameActive = False
    paused = False
    pauseFrameActive = False  # Used by bossKey to check if the pause frame is showing
    slowed = False
    invincible = False

    # Get saved settings from settings.txt file
    controls = []
    bgColour = ""
    playerColour = ""
    settings = open("settings.txt", "r")
    for setting in range(5):
        setting = settings.readline().strip()
        controls.append(setting)
    bgColour = settings.readline().strip()
    playerColour = settings.readline().strip()
    settings.close()

    # Check if there is a save, if so set a flag
    global saveExists
    saveFile = open("save.txt", "r")
    time = saveFile.readline().strip()
    if time == "":
        saveExists = False
    else:
        saveExists = True
    saveFile.close()


def changeBackground(bgCode):
    '''Changes the colour of the backgrounds according to user input.'''
    global bgColour
    bgColour = bgCode

    # Update each frame with new background colour
    homeFrame.configure(bg=bgColour)
    settingsFrame.configure(bg=bgColour)
    leaderboardFrame.configure(bg=bgColour)
    infoFrame.configure(bg=bgColour)
    gameOverFrame.configure(bg=bgColour)
    playerColourFrame.configure(bg=bgColour)
    bgFrame.configure(bg=bgColour)
    keybindsFrame.configure(bg=bgColour)
    cheatsFrame.configure(bg=bgColour)
    pauseFrame.configure(bg=bgColour)


def changePlayerColour(playerCode):
    '''Changes the colour of the player colour according to user input.'''
    global playerColour
    playerColour = playerCode


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
    triggeredKeybindChange = True  # Set flag saying user wants to change their keybind
    keybindNum = tempNum
    # Change back to settings button to a cancel button
    keybindsSettingsBtn.configure(text="Cancel", command=cancelKeybindChange)


def cancelKeybindChange():
    '''Used if the user decides not to bind a key after clicking a button.'''
    global triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    triggeredKeybindChange = False  # Reset variables
    keybindsPromptLabel.configure(text="Click a keybind to change")
    keybindsSettingsBtn.configure(text="Back to Settings", command=lambda: swapFrames(
        1))  # Change button back to normal


def updateKeybind(event):
    '''Updates the keybind as long as they intended to, else adds the keypress to the cheat code buffer.'''
    global controls, triggeredKeybindChange, keybindsPromptLabel, keybindsSettingsBtn
    # If they are not updating keybind, add key to cheat code
    if triggeredKeybindChange == False:
        updateCheatCode(event.keysym)

    # Only update if they pressed a button beforehand
    else:
        window.unbind(controls[keybindNum])
        controls[keybindNum] = "<" + event.keysym + \
            ">"  # Store as correct key format ("<key>")
        triggeredKeybindChange = False
        # Change label to original message
        keybindsPromptLabel.configure(text="Click a keybind to change")
        keybindsSettingsBtn.configure(text="Back to Settings", command=lambda: swapFrames(
            1))  # Change button back to normal

        # Update corresponding button and bind
        tempText = controls[keybindNum]
        tempText = tempText[1:len(tempText)-1]  # Get rid of < >
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
    '''Uses the default settings provided.'''
    global bgColour, playerColour, controls
    bgColour = "#8ec8fa"
    for control in controls:
        window.unbind(control)
    controls = ["<Up>", "<Down>", "<Left>", "<Right>", "<Control_L>"]
    initialiseKeybinds()  # Need to bind the keys again
    upBtn.configure(text="Up: Up")
    downBtn.configure(text="Down: Down")
    leftBtn.configure(text="Left: Left")
    rightBtn.configure(text="Right: Right")
    bossKeyBtn.configure(text="Boss Key: Control_L")
    changeBackground(bgColour)
    playerColour = "light blue"


def saveSettings():
    '''Save the current settings in a text file for next time.'''
    global controls, bgColour, playerColour
    settings = open("settings.txt", "w")
    for setting in controls:
        settings.write(setting + "\n")
    settings.write(bgColour + "\n")
    settings.write(playerColour)
    settings.close()


# ---------------------------------------------- LEADERBOARD FUNCTIONS -----------------------------------------------------------------------


def createLeaderboard():
    '''Creates and formats the leaderboard with headings.'''
    global leaderboard
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", font=(
        "Comic Sans MS", 15, "bold"), rowheight=35)
    style.configure("Treeview.Heading", background="pink",
                    font=("Comic Sans MS", 20, "bold"))
    leaderboard = ttk.Treeview(leaderboardFrame, columns=(
        "name", "time", "score"), show="headings")
    leaderboard.column("name", anchor="center")
    leaderboard.heading("name", text="Name:")
    leaderboard.column("time", anchor="center")
    leaderboard.heading("time", text="Time:")
    leaderboard.column("score", anchor="center")
    leaderboard.heading("score", text="Score:")
    populateLeaderboard()


def populateLeaderboard():
    '''Reads the text file 'leaderboard.txt' and populates the leaderboard.'''
    leaderboardFile = open("leaderboard.txt", "r")
    tempName = leaderboardFile.readline().strip()
    rowNum = 0
    while tempName != "":  # Until end of file is reached
        tempTime = leaderboardFile.readline().strip()
        tempScore = leaderboardFile.readline().strip()
        leaderboard.insert("", "end", iid=rowNum, values=(
            tempName, tempTime, tempScore))
        rowNum += 1
        tempName = leaderboardFile.readline().strip()
    leaderboardFile.close()


def addToLeaderboard():
    '''Take user input and add it to the leaderboard.'''
    global cheats, cheated
    for cheat in cheats:
        if cheat:
            cheated = True
    name = nameInput.get()  # Get input from entry box
    if cheated:
        finalScoreLabel.configure(
            text="Cheaters can't add their\nscore to the leaderboard :)")
    elif name == "":
        finalScoreLabel.configure(text="Field is empty.")
    else:
        finalScoreLabel.configure(text="Score Submitted!")
        submitBtn.configure(bg="red", relief="sunken", command=lambda: finalScoreLabel.configure(
            text="Already submitted your score."))
        nameInput.delete(0, "end")
        nameInput.configure(state="disabled")  # Disable entry box

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
                leaderboard.insert("", "end", iid=line,
                                   values=(treeviewData[line]))
            else:
                if placed == False:
                    leaderboard.insert("", "end", iid=line, values=(newEntry))
                    placed = True
                else:
                    leaderboard.insert("", "end", iid=line,
                                       values=(treeviewData[line-1]))

        # Place final entry
        if placed == False:
            leaderboard.insert("", "end", iid=numOfEntries, values=(newEntry))
        else:
            leaderboard.insert("", "end", iid=numOfEntries,
                               values=(treeviewData[numOfEntries-1]))


def saveLeaderboard():
    '''Writes the current state of the leaderboard to the file to save it for next time.'''
    global window
    leaderboardFile = open("leaderboard.txt", "w")
    for entry in leaderboard.get_children():
        for value in leaderboard.item(entry)["values"]:
            leaderboardFile.write(str(value)+"\n")
    leaderboardFile.close()


# ---------------------------------------------- HOW TO PLAY FUNCTIONS -----------------------------------------------------------------------


def initialiseHowToPlay():
    '''Gets the text from the howToPlay.txt file for the how to play frame.'''
    global howToPlay
    howToPlay = []
    textFile = open("howToPlay.txt", "r")
    for label in range(5):
        paragraph = ""
        tempText = textFile.readline().strip()
        while tempText != "/":
            paragraph += tempText + "\n"
            tempText = textFile.readline().strip()
        paragraph = paragraph.rstrip()
        howToPlay.append(paragraph)
    textFile.close()


def changeInfoLabel(labelText):
    '''Changes the label on the how to play frame according to user input.'''
    global howToPlayLabel
    howToPlayLabel.configure(text=labelText)


# ---------------------------------------------- CHEAT CODE FUNCTIONS -----------------------------------------------------------------------


def cancelCheatCode(event):
    '''Resets the cheat code for misinputs.'''
    global cheatCode
    cheatCode = ""


def updateCheatCode(keyName):
    '''Updates the cheat code and then checks if the player has inputted it correctly.'''
    global cheatCode, cheatsBtn
    cheatCode += keyName
    if cheatCode == "unlockcheats":
        cheatsBtn.configure(command=lambda: swapFrames(7), bg="light blue")
        messagebox.showinfo(title="UNLOCKED", message="Cheats Unlocked!")


def changeCheats(cheatNum):
    '''Enables or disables the cheat that the player chose.'''
    if cheats[cheatNum] == True:
        cheats[cheatNum] = False
    else:
        cheats[cheatNum] = True


# ---------------------------------------------- GAME FUNCTIONS -----------------------------------------------------------------------


def initialiseGame(loaded):
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop.'''
    homeFrame.pack_forget()
    global gameCanvas
    gameCanvas = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameCanvas.pack(fill="both", expand=True)

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, playerDirectionX, playerDirectionY, \
        saved, textBuffer, playerCoords, ballPos, cheated, lives, ballTextCount, slowed, slowTextCount, \
        slowCount, invincible, invincibilityTextCount, invincibilityCount, abilityCoords, difficulty
    if loaded == False:  # Only use default numbers if game wasn't loaded from save file
        time = 0
        score = 0
        numBalls = 0
        balls = []
        xSpeed = []
        ySpeed = []
        playerCoords = (935, 515, 985, 565)
        cheated = False
        lives = 3
        ballTextCount = 5
        slowed = False
        slowTextCount = 0
        slowCount = 0  # Stores how many slow time power ups they have collected
        invincible = False
        invincibilityTextCount = 0
        invincibilityCount = 0  # Stores how many invincible power ups they have collected
        abilityCoords = [(0, 0) for x in range(4)]
        difficulty = 1
    else:
        balls = []
        for ball in ballPos:
            balls.append(gameCanvas.create_oval(
                ball[0], ball[1], ball[2], ball[3], fill=ball[4], width=2))
    playerDirectionX = 5
    playerDirectionY = 0
    saved = False
    textBuffer = []  # When multiple events occur, display them one at a time

    # Create all abilities
    global abilities, abilityNum, previousAbility, upArrow, ghost, clock, delete
    upArrow = Image(file="UpArrow.png")
    ghost = Image(file="Ghost.png")
    clock = Image(file="Clock.png")
    delete = Image(file="DeleteSymbol.png")
    abilities = []
    abilities.append(gameCanvas.create_image(
        abilityCoords[0], image=upArrow, state="hidden"))  # scoreUp ability
    abilities.append(gameCanvas.create_image(
        abilityCoords[1], image=ghost, state="hidden"))  # invincibility ability
    abilities.append(gameCanvas.create_image(
        abilityCoords[2], image=clock, state="hidden"))  # slow time ability
    abilities.append(gameCanvas.create_image(
        abilityCoords[3], image=delete, state="hidden"))  # delete balls ability
    abilityNum = 0
    previousAbility = 0

    # Unhide any abilities that were showing if loaded from save
    for ability in range(4):
        if gameCanvas.coords(abilities[ability]) != [0, 0]:
            gameCanvas.itemconfigure(abilities[ability], state="normal")

    # Create player
    global player, playerColour, beenHit
    if cheats[0] == True:  # If smaller player cheat is enabled, make smaller player
        playerCoords = (
            playerCoords[0]+15, playerCoords[1]+15, playerCoords[2]-15, playerCoords[3]-15)
    player = gameCanvas.create_rectangle(
        playerCoords, fill=playerColour, outline="black", width=2)
    beenHit = False

    # Create and Modify Hearts
    global heart, heartBroken, heart1, heart2, heart3
    heart = Image(file="Heart.png")
    heartBroken = Image(file="HeartBroken.png")
    heart1 = gameCanvas.create_image(1750, 1020, image=heart)
    heart2 = gameCanvas.create_image(1800, 1020, image=heart)
    heart3 = gameCanvas.create_image(1850, 1020, image=heart)
    updateHearts()  # Update the hearts if they load the game

    # Make all text and rectangles behind the text
    global saveBtn, scoreText, invincibilityText, invincibilityTextRectangle, slowText, \
        slowTextRectangle, timeText, ballText, ballTextRectangle, countdownText, \
        countdownTextRectangle, livesText, livesTextRectangle, gameInfoText
    saveBtn.configure(text="Save Game")
    scoreText = gameCanvas.create_text(
        1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(scoreText)
    scoreTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    invincibilityText = gameCanvas.create_text(
        160, 30, text="Invincibility: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(invincibilityText)
    invincibilityTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(invincibilityTextRectangle, invincibilityText)
    slowText = gameCanvas.create_text(
        450, 30, text="Slow Time: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(slowText)
    slowTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(slowTextRectangle, slowText)
    timeText = gameCanvas.create_text(
        1600, 30, text="Time: " + str(time), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(timeText)
    timeTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(timeTextRectangle, timeText)
    ballText = gameCanvas.create_text(
        960, 30, text="Time Until Next Ball: " + str(ballTextCount), font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(ballText)
    ballTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameCanvas.lower(ballTextRectangle, ballText)
    countdownText = gameCanvas.create_text(
        960, 540, text="3", font=("Comic Sans MS", 75, "bold"))
    bbox = gameCanvas.bbox(countdownText)
    countdownTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-60, bbox[1], bbox[2]+60, bbox[3], outline="black", fill="pink", width=2)
    gameCanvas.lower(countdownTextRectangle, countdownText)
    livesText = gameCanvas.create_text(
        1665, 1020, text="Lives:", font=("Comic Sans MS", 20, "bold"))
    bbox = gameCanvas.bbox(livesText)
    livesTextRectangle = gameCanvas.create_rectangle(
        bbox[0]-25, bbox[1]-25, bbox[2]+200, bbox[3]+25, outline="black", width=2)
    gameCanvas.lower(livesTextRectangle, heart1)
    gameInfoText = gameCanvas.create_text(960, 300, text="Default", font=(
        "Comic Sans MS", 30, "bold"), state="hidden")
    gameLoop()


def countdown():
    '''Short countdown before the game starts'''
    global countdownText, countdownTextRectangle
    window.unbind("<Escape>")
    window.unbind(controls[4])
    gameCanvas.itemconfigure(countdownText, state="normal")
    gameCanvas.itemconfigure(countdownTextRectangle, state="normal")
    for i in range(3, 0, -1):
        gameCanvas.itemconfigure(countdownText, text=str(i))
        window.update()
        sleep(1)
    gameCanvas.itemconfigure(countdownText, text="Go!")
    window.update()
    sleep(1)
    gameCanvas.itemconfigure(countdownText, state="hidden")
    gameCanvas.itemconfigure(countdownTextRectangle, state="hidden")
    window.bind("<Escape>", pause)
    window.bind(controls[4], bossKey)


def gameLoop():
    '''The main game loop that repeats until the game ends, then switches to the game over screen.'''
    global gameActive, paused, randomizeRepeatNum, scoreUpRepeatNum, timeRepeatNum, \
        scoreTimeRepeatNum, slowTextRepeatNum, unslowRepeatNum, invincibilityTextRepeatNum, \
        disableInvincibilityRepeatNum, slowed, invincible
    countdown()
    window.configure(cursor="none")

    # Start all after loops
    if cheats[2] == True:
        if time % 6 == 0:  # Preserve cooldown times
            randomizeRepeatNum = gameCanvas.after(6000, randomizeAbility)
        else:
            randomizeRepeatNum = gameCanvas.after(
                (6-(time % 6))*1000, randomizeAbility)
    else:
        if time % 12 == 0:  # Preserve cooldown times
            randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)
        else:
            randomizeRepeatNum = gameCanvas.after(
                (12-(time % 12))*1000, randomizeAbility)
    timeRepeatNum = gameCanvas.after(1000, timer)
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)
    # Only start after function to spawn in scoreUp ability if it isn't already displayed
    if gameCanvas.coords(abilities[0]) == [0, 0]:
        if cheats[2] == True:
            scoreUpRepeatNum = gameCanvas.after(2000, lambda: updateCoords(0))
        else:
            scoreUpRepeatNum = gameCanvas.after(4000, lambda: updateCoords(0))
    else:
        scoreUpRepeatNum = 0

    # Create first ball only if new game
    if balls == []:
        createBall(False)
        createBall(True)

    # Keep the status of the abilities if unpaused or loaded from save file
    if slowTextCount != 0:
        if slowTextCount != 1:
            gameCanvas.itemconfigure(slowTextRectangle, fill="lime")
        else:
            gameCanvas.itemconfigure(slowTextRectangle, fill="red")
        gameCanvas.itemconfigure(
            slowText, text="Slow Time: " + str(slowTextCount))
        slowTextRepeatNum = gameCanvas.after(1000, updateSlowText)
        unslowRepeatNum = gameCanvas.after(slowTextCount*1000, unslowTime)
    if invincibilityTextCount != 0:
        if invincibilityTextCount != 1:
            gameCanvas.itemconfigure(invincibilityTextRectangle, fill="lime")
        else:
            gameCanvas.itemconfigure(invincibilityTextRectangle, fill="red")
        gameCanvas.itemconfigure(
            invincibilityText, text="Invincibility: " + str(invincibilityTextCount))
        invincibilityTextRepeatNum = gameCanvas.after(
            1000, updateInvincibilityText)
        disableInvincibilityRepeatNum = gameCanvas.after(
            invincibilityTextCount*1000, disableInvincibility)
        gameCanvas.itemconfigure(player, fill="#a1fc03")

    # Main game loop
    gameActive = True
    while gameActive and not paused:
        sleep(0.005)
        gameCanvas.move(player, playerDirectionX, playerDirectionY)
        moveBalls()
        checkPlayerCollision()
        window.update()

    # Go to game over screen once only if main game loop wasn't finished by pause
    if paused == False:
        global score
        score = int(score)
        finalScoreLabel.configure(text="You scored " + str(
            score) + " points!\n\nEnter your name to save your score\nor exit to the menu")
        # Stop after loop from randomizing abilities
        gameCanvas.after_cancel(randomizeRepeatNum)
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
        window.configure(cursor="")  # Re-enable cursor
        deathAnimation()
        swapFrames(6)  # Game Over screen


def timer():
    '''Adds one second to the universal timer'''
    global time, ballTextCount, timeRepeatNum
    time += 1
    ballTextCount -= 1
    updateBallText()
    gameCanvas.itemconfigure(timeText, text="Time: " + str(time))
    timeRepeatNum = gameCanvas.after(1000, timer)


def updateBallText():
    '''Updates the text to display the time left before the next ball spawns in.'''
    global ballTextCount
    if ballTextCount == 0:  # Create ball every 5 seconds
        ballTextCount = 5
        updateDifficulty()  # Update the difficulty every 5 seconds
        createBall(True)  # Start moving the new ball
        gameCanvas.itemconfigure(ballTextRectangle, fill="")
    elif ballTextCount == 2:  # Start warning for new ball
        gameCanvas.itemconfigure(ballTextRectangle, fill="orange")
        createBall(False)  # Create ball but don't move it yet
    elif ballTextCount == 1:
        gameCanvas.itemconfigure(ballTextRectangle, fill="red")
    gameCanvas.itemconfigure(
        ballText, text="Time Until Next Ball: " + str(ballTextCount))


def increaseScore():
    '''Increases the score by 4 every second.'''
    global score, scoreTimeRepeatNum
    score += 1
    gameCanvas.itemconfigure(scoreText, text="Score: " + str(score))
    scoreTimeRepeatNum = gameCanvas.after(250, increaseScore)


def updateHearts():
    '''Update the heart images according to the number of lives they have.'''
    global heart, heartBroken, heart1, heart2, heart3, lives
    gameCanvas.after(1500, lambda: gameCanvas.itemconfigure(
        livesTextRectangle, fill=""))
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
    global paused, pauseFrameActive, gameActive, randomizeRepeatNum, scoreUpRepeatNum, \
        timeRepeatNum, scoreTimeRepeatNum
    if gameActive == True:  # Only change paused state if playing game
        if paused:
            paused = False
            pauseFrameActive = False
            gameCanvas.pack(fill="both", expand=True)
            pauseFrame.pack_forget()
            gameLoop()  # Re-run game
        else:
            window.configure(cursor="")  # Re-enable cursor
            paused = True
            pauseFrameActive = True
            gameCanvas.pack_forget()
            pauseFrame.pack(fill="both", expand=True)
            # Stop after loops
            gameCanvas.after_cancel(randomizeRepeatNum)
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

def updateDifficulty():
    '''Updates the difficulty every 30 seconds to speed up the balls'''
    global difficulty
    if time % 30 == 0 and difficulty < 3:
        difficulty += 1
        editInfoText("Difficulty up!", 2000)  # Show the player that the difficulty went up

# ---------------------------------------------- POWER UP FUNCTIONS -----------------------------------------------------------------------


def randomizeAbility():
    '''Chooses a random ability to put on the screen, or update its position if still on the screen.'''
    global randomizeRepeatNum, previousAbility, abilityNum
    while abilityNum == previousAbility:  # New ability cannot be the same as the last one
        abilityNum = randint(1, 3)
    previousAbility = abilityNum
    updateCoords(abilityNum)
    if cheats[2] == True:  # Half ability cool down if that cheat is on
        randomizeRepeatNum = gameCanvas.after(6000, randomizeAbility)
    else:
        randomizeRepeatNum = gameCanvas.after(12000, randomizeAbility)


def updateCoords(abilityNum):
    '''Updates the coordinates of a given ability.'''
    global abilities
    xPos = randint(100, 1790)
    yPos = randint(100, 950)
    gameCanvas.coords(abilities[abilityNum], xPos, yPos)
    gameCanvas.itemconfigure(abilities[abilityNum], state="normal")


def scoreUp():
    '''Increases the score by 40 after the scoreUp power-up is collected.'''
    global score, abilities, scoreUpRepeatNum
    score += 40
    gameCanvas.itemconfigure(abilities[0], state="hidden")
    # Move to top right to prevent extra collisions
    gameCanvas.coords(abilities[0], 0, 0)
    if cheats[2] == True:  # Half ability cool down if that cheat is on
        scoreUpRepeatNum = gameCanvas.after(2000, lambda: updateCoords(0))
    else:
        scoreUpRepeatNum = gameCanvas.after(4000, lambda: updateCoords(0))
    editInfoText("+40 Score", 1000)


def invincibility(invincibleFromMain):
    '''Gain invincibility from balls after collecting the invinsible ability.'''
    global invincible, invincibilityCount, disableInvincibilityRepeatNum, beenHit
    if invincibleFromMain == True:  # If this function was triggered by collecting an ability, increase the count
        invincibilityCount += 1
    if not invincible and invincibilityCount != 0:
        invincible = True
        disableInvincibilityRepeatNum = gameCanvas.after(
            5000, disableInvincibility)
        updateInvincibilityText()
        if not beenHit:  # Only show "Invincible!" if they collected ability
            editInfoText("Invincible!", 1250)
    gameCanvas.itemconfigure(player, fill="#a1fc03")
    if not beenHit:  # Only hide ability if the invincibility didn't occur due to the player being hit
        # Move to top right to prevent extra collisions
        gameCanvas.coords(abilities[1], 0, 0)
        gameCanvas.itemconfigure(abilities[1], state="hidden")
    else:
        beenHit = False


def disableInvincibility():
    '''Disabled invincibility after 5 seconds.'''
    global invincible, invincibilityCount
    invincible = False
    gameCanvas.itemconfigure(player, fill=playerColour)
    invincibilityCount -= 1
    if invincibilityCount != 0:  # If they collected more than 1 invincible ability, give it them again
        invincibility(False)


def slowTime(slowFromMain):
    '''Slows the balls by half after collecting the slow time ability.'''
    global xSpeed, ySpeed, slowed, slowCount, unslowRepeatNum
    if slowFromMain == True:  # If this function was triggered by collecting an ability, increase the count
        slowCount += 1
    if not slowed and slowCount != 0:
        slowed = True
        xSpeed = [speed/2 for speed in xSpeed]
        ySpeed = [speed/2 for speed in ySpeed]
        unslowRepeatNum = gameCanvas.after(5000, unslowTime)
        updateSlowText()
        editInfoText("Time Slowed!", 1250)
    # Move to top right to prevent extra collisions
    gameCanvas.coords(abilities[2], 0, 0)
    gameCanvas.itemconfigure(abilities[2], state="hidden")


def unslowTime():
    '''Resets all ball speeds by doubling the speed value.'''
    global xSpeed, ySpeed, slowed, slowCount
    slowed = False
    xSpeed = [speed*2 for speed in xSpeed]
    ySpeed = [speed*2 for speed in ySpeed]
    slowCount -= 1
    if slowCount != 0:  # If they collected more than 1 slow ability, give it them again
        slowTime(False)


def deleteBalls():
    '''Deletes 3 balls randomly after collecting the delete balls ability.'''
    gameCanvas.itemconfigure(abilities[3], state="hidden")
    # Move to top right to prevent extra collisions
    gameCanvas.coords(abilities[3], 0, 0)
    global balls, numBalls, xSpeed, ySpeed
    if numBalls <= 2:  # If there are less than 3 balls on the screen, get rid of them all
        deleteNum = numBalls
        numBalls -= numBalls
    else:  # Else delete 3 balls
        deleteNum = 3
        numBalls -= 3
    for ball in range(deleteNum):
        tempBall = randint(0, len(balls)-1)
        xSpeed.pop(tempBall)
        ySpeed.pop(tempBall)
        tempBall = balls[tempBall]
        balls.remove(tempBall)
        tempCoords = gameCanvas.coords(tempBall)
        gameCanvas.coords(
            tempBall, tempCoords[0]-20, tempCoords[1]-20, tempCoords[2]+20, tempCoords[3]+20)
        window.update()
        sleep(0.25)
        gameCanvas.delete(tempBall)
    editInfoText(str(deleteNum) + " Balls Deleted", 1500)


def updateInvincibilityText():
    '''Updates the invincibility text with the amount of time left.'''
    global invincibilityTextCount, invincibilityTextRepeatNum
    if invincibilityTextCount == 0:
        invincibilityTextCount = 5
    else:
        invincibilityTextCount -= 1
    gameCanvas.itemconfigure(
        invincibilityText, text="Invincibility: " + str(invincibilityTextCount))

    # Configure colour of rectangle according to time left
    if invincibilityTextCount >= 3:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="lime")
    elif invincibilityTextCount == 2:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="orange")
    elif invincibilityTextCount == 1:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="red")

    # Call function again if timer isn't over
    if invincibilityTextCount != 0:
        invincibilityTextRepeatNum = gameCanvas.after(
            1000, updateInvincibilityText)
    else:
        gameCanvas.itemconfigure(invincibilityTextRectangle, fill="")


def updateSlowText():
    '''Updates the slow text with the amount of time left.'''
    global slowTextCount, slowTextRepeatNum
    if slowTextCount == 0:
        slowTextCount = 5
    else:
        slowTextCount -= 1
    gameCanvas.itemconfigure(slowText, text="Slow Time: " + str(slowTextCount))

    # Configure colour of rectangle according to time left
    if slowTextCount >= 3:
        gameCanvas.itemconfigure(slowTextRectangle, fill="lime")
    elif slowTextCount == 2:
        gameCanvas.itemconfigure(slowTextRectangle, fill="orange")
    elif slowTextCount == 1:
        gameCanvas.itemconfigure(slowTextRectangle, fill="red")

    # Call function again if timer isn't over
    if slowTextCount != 0:
        slowTextRepeatNum = gameCanvas.after(1000, updateSlowText)
    else:
        gameCanvas.itemconfigure(slowTextRectangle, fill="")


def editInfoText(text, time):
    '''Takes a parameter text and edits the info text correspondingly.'''
    global textBuffer
    if text != None:  # If this function was called by hideInfoText, don't add text to buffer
        textTime = [text, time]
        textBuffer.append(textTime)
    # If there isn't any other text being displayed, display it
    if len(textBuffer) == 1 or text == None:
        gameCanvas.itemconfigure(
            gameInfoText, text=textBuffer[0][0], state="normal")
        gameCanvas.after(textBuffer[0][1], hideInfoText)  # Hide the text afterwards


def hideInfoText():
    '''Hides the text that appears in the middle of the screen whenever they get an ability or lose a life.'''
    global textBuffer
    gameCanvas.itemconfigure(gameInfoText, state="hidden")
    textBuffer.pop(0)
    if textBuffer != []:  # If there is more text to display
        editInfoText(None, None)


# ---------------------------------------------- BALL FUNCTIONS -----------------------------------------------------------------------


def createBall(move):
    '''Creates a new ball and appends it to an array, along with its corresponding x and y speed and colour.'''
    # Create the ball but don't start moving it
    if not move:
        side = randint(1, 3)  # Choose a side to spawn the ball at
        if side == 1:  # Down
            xPos = randint(50, 1870)
            yPos = 1040
        elif side == 2:  # Left
            xPos = 10
            yPos = randint(50, 1030)
        else:  # Right
            xPos = 1880
            yPos = randint(50, 1030)

        # Create ball and set its speed to 0
        global numBalls
        xy = (xPos, yPos, xPos+20, yPos+20)
        balls.append(gameCanvas.create_oval(xy, fill="black", width=2))
        numBalls += 1
        xSpeed.append(0)
        ySpeed.append(0)

    # Move the ball by giving its speed and colour
    else:
        # If slow time ability is active, half speed values
        # Determine the speed based on the difficulty
        global slowed, difficulty
        if slowed == True:
            if difficulty == 1:
                speedValues = [1, 2]
            elif difficulty == 2:
                speedValues = [1, 3]
            else:
                speedValues = [1, 5]
            colourBounds = [4, 3, 2]
        else:
            if difficulty == 1:
                speedValues = [2, 4]
            elif difficulty == 2:
                speedValues = [2, 6]
            else:
                speedValues = [2, 10]
            colourBounds = [8, 6, 4]

        # Generate speed and direction
        tempX = randint(speedValues[0], speedValues[1])
        tempY = randint(speedValues[0], speedValues[1])
        xSign = randint(0, 1)
        ySign = randint(0, 1)
        if xSign == 0:
            tempX = -tempX  # Make direction Left (-x), else Right (x)
        if ySign == 0:
            tempY = -tempY  # Make direction Up (-y), else Down (y)
        xSpeed[numBalls-1] = tempX
        ySpeed[numBalls-1] = tempY

        # Determine colour of ball based on speed (Black < Blue < Purple < Red)
        averageSpeed = (abs(tempX) + abs(tempY))/2
        if averageSpeed >= colourBounds[0]:
            gameCanvas.itemconfigure(
                balls[numBalls-1], fill="#ff0000", outline="black")
        elif averageSpeed >= colourBounds[1]:
            gameCanvas.itemconfigure(
                balls[numBalls-1], fill="#d303fc", outline="black")
        elif averageSpeed >= colourBounds[2]:
            gameCanvas.itemconfigure(
                balls[numBalls-1], fill="blue", outline="black")
        else:
            gameCanvas.itemconfigure(
                balls[numBalls-1], fill="black", outline="black")


def moveBalls():
    '''Responsible for checking collisions with the wall, between balls and the player, and moving each ball.'''
    for i in range(len(balls)):
        pos = gameCanvas.coords(balls[i])
        # Check the ball for collision with wall
        if pos[3] > 1080 or pos[1] < 0:
            ySpeed[i] = -ySpeed[i]
        if pos[2] > 1920 or pos[0] < 0:
            xSpeed[i] = -xSpeed[i]

        # Check the ball for collision with other balls
        for j in range(len(balls)):
            if i == j:  # Skip if you are comparing the same ball
                continue
            pos2 = gameCanvas.coords(balls[j])
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]:
                ySpeed[i] = -ySpeed[i]
                xSpeed[i] = -xSpeed[i]
                ySpeed[j] = -ySpeed[j]
                xSpeed[j] = -xSpeed[j]

        gameCanvas.move(balls[i], xSpeed[i], ySpeed[i])


# ---------------------------------------------- PLAYER FUNCTIONS ----------------------------------------------------


def upDirection(event):
    '''Change the player's direction to up.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = 0
    playerDirectionY = -5


def downDirection(event):
    '''Change the player's direction to down.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = 0
    playerDirectionY = 5


def leftDirection(event):
    '''Change the player's direction to left.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = -5
    playerDirectionY = 0


def rightDirection(event):
    '''Change the player's direction to right.'''
    global playerDirectionX, playerDirectionY
    playerDirectionX = 5
    playerDirectionY = 0


def checkPlayerCollision():
    '''Checks if the player is touching a ball, the wall or any abilities.'''
    # Check collision with wall
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
                    or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
                hit()


def scoreUpCollision(pos):
    '''Takes the players position as argument and checks if they collided with the scoreUp ability'''
    pos2 = gameCanvas.coords(abilities[0])
    pos2 = [pos2[0]-20, pos2[1]-25, pos2[0]+20, pos2[1]+25]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
            or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        scoreUp()


def invincibleCollision(pos):
    '''Takes the players position as argument and checks if they collided with the invincible ability'''
    pos2 = gameCanvas.coords(abilities[1])
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
            or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        invincibility(True)


def slowTimeCollision(pos):
    '''Takes the players position as argument and checks if they collided with the slow time ability'''
    pos2 = gameCanvas.coords(abilities[2])
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
            or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        slowTime(True)


def deleteBallsCollision(pos):
    '''Takes the players position as argument and checks if they collided with the delete balls ability'''
    pos2 = gameCanvas.coords(abilities[3])
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
            or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        deleteBalls()


def hit():
    '''Decreases the life if the player is hit, if they are on 0 lives, end the game.'''
    global gameActive, lives, livesTextRectangle, beenHit
    lives -= 1
    updateHearts()
    if lives != 0:
        hitAnimation(True)
        beenHit = True
        # Give the player temporary invulnerability after being hit
        invincibility(True)
        gameCanvas.itemconfigure(livesTextRectangle, fill="#fc0390")
        editInfoText(str(lives) + " lives remaining", 2000)
    if lives == 0:
        gameActive = False


def hitAnimation(repeat):
    '''The animation that is played whenever the player is hit.'''
    tempCoords = gameCanvas.coords(player)
    if repeat == True:
        gameCanvas.coords(
            player, tempCoords[0]+10, tempCoords[1]+10, tempCoords[2]-10, tempCoords[3]-10)
        gameCanvas.itemconfigure(player, fill="red")
        window.update()
        sleep(0.4)
        hitAnimation(False)
    else:
        gameCanvas.coords(
            player, tempCoords[0]-10, tempCoords[1]-10, tempCoords[2]+10, tempCoords[3]+10)
        window.update()
        sleep(0.4)
        gameCanvas.itemconfigure(player, fill=playerColour)


def deathAnimation():
    '''When the player dies, shrink the player.'''
    tempCoords = gameCanvas.coords(player)
    gameCanvas.itemconfigure(player, fill="red")
    for shrink in range(5):
        for coordinate in range(4):
            if coordinate <= 1:
                if cheats[0] == True:
                    tempCoords[coordinate] += 2
                else:
                    tempCoords[coordinate] += 5
            else:
                if cheats[0] == True:
                    tempCoords[coordinate] -= 2
                else:
                    tempCoords[coordinate] -= 5
        gameCanvas.coords(player, tempCoords)
        window.update()
        sleep(0.3)


# ---------------------------------------------- SAVE/LOAD GAME FUNCTIONS --------------------------------------------------------


def saveGame(override):
    '''Saves the current state of the game into a text file that can be read from to load the game.'''
    global time, score, numBalls, lives, ballTextCount, slowed, slowTextCount, slowCount, invincible, \
        invincibilityTextCount, invincibilityCount, balls, xSpeed, ySpeed, saved, cheated
    if saved == True:
        saveBtn.configure(text="Already saved.")
    else:
        saveFile = open("save.txt", "r")
        line = saveFile.readline().strip()
        saveFile.close()
        if line != "" and override == False:
            pauseInfoLabel.configure(
                text="Do you want to override\nthe last save?")
            saveBtn.configure(text="Yes", command=lambda: overrideSave(True))
            pauseHomeBtn.configure(
                text="No", command=lambda: overrideSave(False))
            window.unbind("<Escape>")
        else:
            override = True
        if override == True:
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
            playerPos = gameCanvas.coords(player)
            # If they used the 'smaller player' cheat, increase the size back to normal
            if cheats[0] == True:
                for coordinate in range(4):
                    if coordinate <= 1:
                        saveFile.write(str(playerPos[coordinate]-15) + "\n")
                    else:
                        saveFile.write(str(playerPos[coordinate]+15) + "\n")
            else:  # Else save the normal coordinates
                for coordinate in range(4):
                    saveFile.write(str(playerPos[coordinate]) + "\n")
            for ability in abilities:
                tempCoords = gameCanvas.coords(ability)
                for coordinate in tempCoords:
                    saveFile.write(str(coordinate) + "\n")
            for variable in range(3):
                for ball in range(numBalls):
                    if variable == 0:  # Write all ball coordinates
                        ballPos = gameCanvas.coords(balls[ball])
                        for coordinate in ballPos:
                            saveFile.write(str(coordinate) + "\n")
                        saveFile.write(gameCanvas.itemcget(
                            balls[ball], "fill") + "\n")
                    elif variable == 1:  # Write all x speeds
                        saveFile.write(str(xSpeed[ball]) + "\n")
                    else:  # Write all y speeds
                        saveFile.write(str(ySpeed[ball]) + "\n")
            if cheats[0] == True or cheats[1] == True or cheats[2] == True or cheated == True:
                saveFile.write("True\n")
            else:
                saveFile.write("False\n")
            saveFile.close()
            saveBtn.configure(text="Saved!")
            saved = True
            gameCanvas.after(1000, lambda: swapFrames(0))


def overrideSave(override):
    '''Decides whether to override the save file or not.'''
    if override == True:
        pauseInfoLabel.configure(
            text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.")
        saveBtn.configure(command=lambda: saveGame(False))
        pauseHomeBtn.configure(text="Home", command=lambda: swapFrames(0))
        window.bind("<Escape>", pause)
        saveGame(True)  # Override save file
    else:
        pauseInfoLabel.configure(
            text="Press Esc to unpause.\nExit to the home menu or\nsave your current game.")
        saveBtn.configure(text="Save Game", command=lambda: saveGame(False))
        pauseHomeBtn.configure(text="Home", command=lambda: swapFrames(0))
        window.bind("<Escape>", pause)


def loadGame():
    '''Loads a game from the save.txt file, or ignores if game not found.'''
    saveFile = open("save.txt", "r")
    temp = saveFile.readline().strip()
    if temp == "":
        loadBtn.configure(text="No Game Found")
        window.after(1000, lambda: loadBtn.configure(text="Load Game"))
    else:
        global saveExists, loaded, time, score, numBalls, lives, ballTextCount, \
            slowed, slowTextCount, slowCount, invincible, invincibilityTextCount, \
            invincibilityCount, playerCoords, abilityCoords, ballPos, xSpeed, ySpeed, cheated
        saveExists = False
        loaded = True
        time = int(temp)
        score = int(saveFile.readline().strip())
        numBalls = int(saveFile.readline().strip())
        lives = int(saveFile.readline().strip())
        ballTextCount = int(saveFile.readline().strip())
        slowed = saveFile.readline().strip()
        if slowed == "False":
            slowed = False
        else:
            slowed = True
        slowTextCount = int(saveFile.readline().strip())
        slowCount = int(saveFile.readline().strip())
        invincible = saveFile.readline().strip()
        if invincible == "False":
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
        playerCoords = (playerCoords[0], playerCoords[1],
                        playerCoords[2], playerCoords[3])

        # Load the ability coordinates
        for ability in range(4):
            tempCoords = []
            for coordinate in range(2):
                coordinate = saveFile.readline().strip()
                tempCoords.append(coordinate)
            abilityCoords.append(
                (tempCoords[0], tempCoords[1]))

        # Load ball information
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
        cheated = saveFile.readline().strip()
        if cheated == "True":
            cheated = True
        else:
            cheated = False
        saveFile.close()
        open("save.txt", "w").close()  # Erase the save
        initialiseGame(True)


# ---------------------------------------------- MAIN PROGRAM --------------------------------------------------------
configureWindow()
initialiseMenu()
changeBackground(bgColour)
initialiseKeybinds()
homeFrame.pack(fill="both", expand=True)  # Start at the home page
window.mainloop()
