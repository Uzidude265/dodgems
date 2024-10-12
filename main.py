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
        bgFrame, keybindsFrame, cheatsFrame, pauseFrame
    homeFrame = Frame(window)
    settingsFrame = Frame(window)
    leaderboardFrame = Frame(window)
    infoFrame = Frame(window)
    gameOverFrame = Frame(window)
    playerColourFrame = Frame(window)
    bgFrame = Frame(window)
    keybindsFrame = Frame(window)
    cheatsFrame = Frame(window)
    pauseFrame = Frame(window)

    # HOME FRAME WIDGETS
    global logo, loadBtn
    logo = Image(file="Dodgems.png")
    homeLabel = Label(homeFrame, image=logo, highlightthickness=10)
    playBtn = Btn(homeFrame, width=25, height=1, text="Play", bg="light blue", activebackground="cyan", font=(
        "Comic Sans MS", 15, "bold"), command=lambda event: initialiseGame(event, loaded=False))
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
    global upBtn, downBtn, leftBtn, rightBtn, keybindsSettingsBtn, keybindsPromptLabel
    # Remove the < > from the controls to add to the corresponding button's text
    tempUp = controls[0]
    tempUp = tempUp[1:len(tempUp)-1]
    tempDown = controls[1]
    tempDown = tempDown[1:len(tempDown)-1]
    tempLeft = controls[2]
    tempLeft = tempLeft[1:len(tempLeft)-1]
    tempRight = controls[3]
    tempRight = tempRight[1:len(tempRight)-1]
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
    keybindsSettingsBtn = Btn(keybindsFrame, width=25, height=1, text="Back to Settings", bg="light blue",
                              activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(1))

    # KEYBIND FRAME PACKING
    keybindsLabel.pack(side="top", pady=(150, 0))
    keybindsPromptLabel.pack(side="top", pady=(30, 0))
    upBtn.pack(side="top", pady=(45, 0))
    downBtn.pack(side="top", pady=(10, 0))
    leftBtn.pack(side="top", pady=(10, 0))
    rightBtn.pack(side="top", pady=(10, 0))
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
    finalScoreLabel = Label(gameOverFrame, width=30, height=6, bg="pink", text="", font=(
        "Comic Sans MS", 18, "bold"), borderwidth=3, relief="solid")
    nameInput = Entry(gameOverFrame, width=30, bg="#aeeafc", font=(
        "Comic Sans MS", 20, "bold"), justify="center")
    submitBtn = Btn(gameOverFrame, width=25, height=1, text="Submit", bg="light blue",
                    activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=addToLeaderboard)
    gameOverHomeBtn = Btn(gameOverFrame, width=25, height=1, text="Home", bg="light blue",
                          activebackground="cyan", font=("Comic Sans MS", 15, "bold"), command=lambda: swapFrames(0))

    # GAME OVER FRAME PACKING
    gameOverLabel.pack(side="top", pady=(150, 0))
    finalScoreLabel.pack(side="top", pady=(50, 0))
    nameInput.pack(side="top", pady=(70, 0))
    submitBtn.pack(side="top", pady=(70, 0))
    gameOverHomeBtn.pack(side="top", pady=(20, 0))


def swapFrames(frameNum, event=None):
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
        window.unbind("<Return>")  # Unbind the submit/enter button and escape
        window.bind("<Return>", lambda event: initialiseGame(event, loaded=False))
        window.unbind("<Escape>")
        print("Escape unbinded for home screen")
        paused = False
        gameActive = False
        if slowed:  # Pause any remaining after loops
            gameFrame.after_cancel(slowTextRepeatNum)
            gameFrame.after_cancel(unslowRepeatNum)
        if invincible:
            gameFrame.after_cancel(invincibilityTextRepeatNum)
            gameFrame.after_cancel(disableInvincibilityRepeatNum)
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
        gameFrame.pack_forget()
        gameOverFrame.pack(fill="both", expand=True)
        submitBtn.configure(bg="light blue", relief="raised",
                            command=addToLeaderboard)  # Reset submit button
        nameInput.configure(state="normal")  # Re-enable entry box
        window.bind("<Return>", addToLeaderboard)
        window.bind("<Escape>", lambda event: swapFrames(0, event))
    elif frameNum == 7:  # Swap to the cheats frame
        settingsFrame.pack_forget()
        cheatsFrame.pack(fill="both", expand=True)
    else:  # Swap to the player colour frame
        settingsFrame.pack_forget()
        playerColourFrame.pack(fill="both", expand=True)


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
        howToPlayText, cheatCode, cheats, gameActive, paused, pauseFrameActive, slowed, invincible
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
    gameActive = False
    paused = False
    slowed = False
    invincible = False

    # Get saved settings from settings.txt file
    controls = []
    bgColour = ""
    playerColour = ""
    settings = open("settings.txt", "r")
    for setting in range(4):
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
    window.bind("<BackSpace>", cancelCheatCode)
    window.bind("<Key>", updateKeybind)
    window.bind("<Return>", lambda event: initialiseGame(event, loaded=False))


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
        else:
            rightBtn.configure(text="Right: " + tempText)
            window.bind(controls[keybindNum], rightDirection)


def defaultSettings():
    '''Uses the default settings provided.'''
    global bgColour, playerColour, controls
    bgColour = "#8ec8fa"
    for control in controls:
        window.unbind(control)
    controls = ["<Up>", "<Down>", "<Left>", "<Right>"]
    initialiseKeybinds()  # Need to bind the keys again
    upBtn.configure(text="Up: Up")
    downBtn.configure(text="Down: Down")
    leftBtn.configure(text="Left: Left")
    rightBtn.configure(text="Right: Right")
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
        "rank", "name", "score", "time", "difficulty"), show="headings")
    leaderboard.column("rank", anchor="center")
    leaderboard.heading("rank", text="Rank:")
    leaderboard.column("name", anchor="center")
    leaderboard.heading("name", text="Name:")
    leaderboard.column("score", anchor="center")
    leaderboard.heading("score", text="Score:")
    leaderboard.column("time", anchor="center")
    leaderboard.heading("time", text="Time:")
    leaderboard.column("difficulty", anchor="center")
    leaderboard.heading("difficulty", text="Difficulty:")
    populateLeaderboard()


def populateLeaderboard():
    '''Reads the text file 'leaderboard.txt' and populates the leaderboard.'''
    leaderboardFile = open("leaderboard.txt", "r")
    tempRank = leaderboardFile.readline().strip()
    rowNum = 0
    while tempRank != "":  # Until end of file is reached
        tempName = leaderboardFile.readline().strip()
        tempScore = leaderboardFile.readline().strip()
        tempTime = leaderboardFile.readline().strip()
        tempDifficulty = leaderboardFile.readline().strip()
        leaderboard.insert("", "end", iid=rowNum, values=(
            tempRank, tempName, tempScore, tempTime, tempDifficulty))
        rowNum += 1
        tempRank = leaderboardFile.readline().strip()
    leaderboardFile.close()


def addToLeaderboard(event=None):
    '''Take user input and add it to the leaderboard.'''
    global cheats, cheated
    print("Attempting to add to leaderboard")
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
        count = 1
        placed = False
        for line in range(numOfEntries):
            if score <= int(treeviewData[line][2]):
                leaderboard.insert("", "end", iid=line,
                                   values=(treeviewData[line]))
            else:
                if placed == False:
                    newEntry = [count, name, str(score), str(time), str(difficulty)]
                    leaderboard.insert("", "end", iid=line, values=(newEntry))
                    placed = True
                else:
                    entry = treeviewData[line-1]
                    entry[0] = str(count)  # Update the rank by one
                    leaderboard.insert("", "end", iid=line,
                                       values=(entry))
            count += 1

        # Place final entry
        if placed == False:
            newEntry = [count, name, str(score), str(time), str(difficulty)]
            leaderboard.insert("", "end", iid=numOfEntries, values=(newEntry))
        else:
            entry = treeviewData[numOfEntries-1]
            entry[0] = str(count )  # Update the rank by one
            leaderboard.insert("", "end", iid=numOfEntries,
                               values=(entry))


def saveLeaderboard():
    '''Writes the current state of the leaderboard to the file to save it for next time.'''
    global window
    leaderboardFile = open("leaderboard.txt", "w")
    for entry in leaderboard.get_children():
        for value in leaderboard.item(entry)["values"]:
            leaderboardFile.write(str(value)+"\n")
    leaderboardFile.close()

def checkRanking(score):
    '''Takes the player's score and returns the rank where they would be placed on the leaderboard.'''
    rank = 1

    for line in leaderboard.get_children():
        row = leaderboard.item(line)["values"]

        # If the player's score is greater than this row, that is their rank
        if score > int(row[2]):
            return rank
        else:
            rank += 1

    # If they are last place
    return rank

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


def initialiseGame(event, loaded):
    '''Sets up all of the variables and conditions in order to play the game, then starts the game loop.'''
    homeFrame.pack_forget()
    global gameFrame
    gameFrame = Canvas(window, width=1920, height=1080, bg=bgColour)
    gameFrame.pack(fill="both", expand=True)
    window.unbind("<Return>") # Unbind start button

    # Create all of the variables needed
    global time, score, numBalls, balls, xSpeed, ySpeed, playerDirectionX, playerDirectionY, \
        saved, textBuffer, playerCoords, ballPos, cheated, lives, ballTextCount, slowed, slowTextCount, \
        slowCount, invincible, invincibilityTextCount, invincibilityCount, difficulty
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
        difficulty = 1
    else:
        balls = []
        for ball in ballPos:
            balls.append(gameFrame.create_oval(
                ball[0], ball[1], ball[2], ball[3], fill=ball[4], width=2))
    playerDirectionX = 7
    playerDirectionY = 0
    saved = False
    textBuffer = []  # When multiple events occur, display them one at a time

    # Create all abilities
    global abilities, abilityNum, previousAbility, upArrow, ghost, clock, delete
    upArrow = Image(file="UpArrow.png")
    ghost = Image(file="Ghost.png")
    clock = Image(file="Clock.png")
    delete = Image(file="DeleteSymbol.png")
    abilities = [None, None, None, None]
    abilityNum = 0
    previousAbility = 0

    # Create player
    global player, warpedPlayer, playerColour, beenHit
    if cheats[0] == True:  # If smaller player cheat is enabled, make smaller player
        playerCoords = (
            playerCoords[0]+15, playerCoords[1]+15, playerCoords[2]-15, playerCoords[3]-15)
    player = gameFrame.create_rectangle(
        playerCoords, fill=playerColour, outline="black", width=2)
    warpedPlayer = gameFrame.create_rectangle(
        playerCoords, fill=playerColour, outline="black", width=2, state="hidden")
    beenHit = False

    # Create and Modify Hearts
    global heart, heartBroken, heart1, heart2, heart3
    heart = Image(file="Heart.png")
    heartBroken = Image(file="HeartBroken.png")
    heart1 = gameFrame.create_image(1750, 1020, image=heart)
    heart2 = gameFrame.create_image(1800, 1020, image=heart)
    heart3 = gameFrame.create_image(1850, 1020, image=heart)
    updateHearts()  # Update the hearts if they load the game

    # Make all text and rectangles behind the text
    global saveBtn, scoreText, invincibilityText, invincibilityTextRectangle, slowText, \
        slowTextRectangle, timeText, ballText, ballTextRectangle, countdownText, \
        countdownTextRectangle, livesText, livesTextRectangle, gameInfoText, \
        difficultyText, difficultyTextRectangle
    saveBtn.configure(text="Save Game")
    scoreText = gameFrame.create_text(
        1800, 30, text="Score: " + str(score), font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(scoreText)
    scoreTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    invincibilityText = gameFrame.create_text(
        160, 30, text="Invincibility: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(invincibilityText)
    invincibilityTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameFrame.lower(invincibilityTextRectangle, invincibilityText)
    slowText = gameFrame.create_text(
        450, 30, text="Slow Time: 0", font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(slowText)
    slowTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameFrame.lower(slowTextRectangle, slowText)
    timeText = gameFrame.create_text(
        1600, 30, text="Time: " + str(time), font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(timeText)
    timeTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameFrame.lower(timeTextRectangle, timeText)
    ballText = gameFrame.create_text(
        960, 30, text="Time Until Next Ball: " + str(ballTextCount), font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(ballText)
    ballTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1], bbox[2]+25, bbox[3], outline="black", width=2)
    gameFrame.lower(ballTextRectangle, ballText)
    countdownText = gameFrame.create_text(
        960, 540, text="3", font=("Comic Sans MS", 75, "bold"))
    bbox = gameFrame.bbox(countdownText)
    countdownTextRectangle = gameFrame.create_rectangle(
        bbox[0]-60, bbox[1], bbox[2]+60, bbox[3], outline="black", fill="pink", width=2)
    gameFrame.lower(countdownTextRectangle, countdownText)
    livesText = gameFrame.create_text(
        1665, 1020, text="Lives:", font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(livesText)
    livesTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1]-25, bbox[2]+200, bbox[3]+25, outline="black", width=2)
    gameFrame.lower(livesTextRectangle, heart1)
    gameInfoText = gameFrame.create_text(960, 300, text="Default", font=(
        "Comic Sans MS", 30, "bold"), state="hidden")
    difficultyText = gameFrame.create_text(
        140, 1030, text="Difficulty: 1", font=("Comic Sans MS", 20, "bold"))
    bbox = gameFrame.bbox(difficultyText)
    difficultyTextRectangle = gameFrame.create_rectangle(
        bbox[0]-25, bbox[1]-15, bbox[2]+25, bbox[3]+15, outline="black", width=2)
    gameFrame.lower(difficultyTextRectangle, difficultyText)
    gameLoop()


def countdown():
    '''Short countdown before the game starts'''
    global countdownText, countdownTextRectangle
    gameFrame.itemconfigure(countdownText, state="normal")
    gameFrame.itemconfigure(countdownTextRectangle, state="normal")
    for i in range(3, 0, -1):
        gameFrame.itemconfigure(countdownText, text=str(i))
        window.update()
        sleep(1)
    gameFrame.itemconfigure(countdownText, text="Go!")
    window.update()
    sleep(1)
    gameFrame.itemconfigure(countdownText, state="hidden")
    gameFrame.itemconfigure(countdownTextRectangle, state="hidden")
    window.bind("<Escape>", pause)


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
            randomizeRepeatNum = gameFrame.after(6000, randomizeAbility)
        else:
            randomizeRepeatNum = gameFrame.after(
                (6-(time % 6))*1000, randomizeAbility)
    else:
        if time % 12 == 0:  # Preserve cooldown times
            randomizeRepeatNum = gameFrame.after(12000, randomizeAbility)
        else:
            randomizeRepeatNum = gameFrame.after(
                (12-(time % 12))*1000, randomizeAbility)
    timeRepeatNum = gameFrame.after(1000, timer)
    scoreTimeRepeatNum = gameFrame.after(250, increaseScore)
    # Only start after function to spawn in scoreUp ability if it isn't already displayed
    if not abilities[0]:
        if cheats[2] == True:
            scoreUpRepeatNum = gameFrame.after(2000, lambda: createAbility(0))
        else:
            scoreUpRepeatNum = gameFrame.after(4000, lambda: createAbility(0))
    else:
        scoreUpRepeatNum = 0

    # Create first ball only if new game
    if balls == []:
        createBall(False)
        createBall(True)

    # Keep the status of the abilities if unpaused or loaded from save file
    if slowTextCount != 0:
        if slowTextCount != 1:
            gameFrame.itemconfigure(slowTextRectangle, fill="lime")
        else:
            gameFrame.itemconfigure(slowTextRectangle, fill="red")
        gameFrame.itemconfigure(
            slowText, text="Slow Time: " + str(slowTextCount))
        slowTextRepeatNum = gameFrame.after(1000, updateSlowText)
        unslowRepeatNum = gameFrame.after(slowTextCount*1000, unslowTime)
    if invincibilityTextCount != 0:
        if invincibilityTextCount != 1:
            gameFrame.itemconfigure(invincibilityTextRectangle, fill="lime")
        else:
            gameFrame.itemconfigure(invincibilityTextRectangle, fill="red")
        gameFrame.itemconfigure(
            invincibilityText, text="Invincibility: " + str(invincibilityTextCount))
        invincibilityTextRepeatNum = gameFrame.after(
            1000, updateInvincibilityText)
        disableInvincibilityRepeatNum = gameFrame.after(
            invincibilityTextCount*1000, disableInvincibility)
        gameFrame.itemconfigure(player, fill="#a1fc03")

    # Main game loop
    gameActive = True
    while gameActive and not paused:
        sleep(0.01)  # TODO Play around with time and speed of balls/player to reduce lag
        movePlayer()
        moveBalls()
        checkPlayerCollision()
        window.update()

    # Go to game over screen once only if main game loop wasn't finished by pause
    if paused == False:
        global score
        score = int(score)
        finalScoreLabel.configure(text="You scored " + str(
            score) + " points!\nYour rank is " + str(checkRanking(score)) + " on the leaderboard\n\nEnter your name to submit\nyour score to the leaderboard")
        # Stop after loop from randomizing abilities
        gameFrame.after_cancel(randomizeRepeatNum)
        gameFrame.after_cancel(timeRepeatNum)
        gameFrame.after_cancel(scoreTimeRepeatNum)
        if scoreUpRepeatNum != 0:
            gameFrame.after_cancel(scoreUpRepeatNum)
        if slowed:
            gameFrame.after_cancel(slowTextRepeatNum)
            gameFrame.after_cancel(unslowRepeatNum)
        if invincible:
            gameFrame.after_cancel(invincibilityTextRepeatNum)
            gameFrame.after_cancel(disableInvincibilityRepeatNum)
        window.configure(cursor="")  # Re-enable cursor
        window.unbind("<Escape>")  # Get rid of pause function
        print("Escape unbinded for game over")
        deathAnimation()
        swapFrames(6)  # Game Over screen
        print("Swapped to game over screen")


def timer():
    '''Adds one second to the universal timer'''
    global time, ballTextCount, timeRepeatNum
    time += 1
    ballTextCount -= 1
    updateBallText()
    gameFrame.itemconfigure(timeText, text="Time: " + str(time))
    timeRepeatNum = gameFrame.after(1000, timer)


def updateBallText():
    '''Updates the text to display the time left before the next ball spawns in.'''
    global ballTextCount
    if ballTextCount == 0:  # Create ball every 5 seconds
        ballTextCount = 5
        updateDifficulty(True)  # Update the difficulty every 5 seconds
        createBall(True)  # Start moving the new ball
        gameFrame.itemconfigure(ballTextRectangle, fill="")
    elif ballTextCount == 2:  # Start warning for new ball
        gameFrame.itemconfigure(ballTextRectangle, fill="orange")
        createBall(False)  # Create ball but don't move it yet
    elif ballTextCount == 1:
        gameFrame.itemconfigure(ballTextRectangle, fill="red")
    gameFrame.itemconfigure(
        ballText, text="Time Until Next Ball: " + str(ballTextCount))


def increaseScore():
    '''Increases the score by 4 every second.'''
    global score, scoreTimeRepeatNum
    score += 1
    gameFrame.itemconfigure(scoreText, text="Score: " + str(score))
    scoreTimeRepeatNum = gameFrame.after(250, increaseScore)


def updateHearts():
    '''Update the heart images according to the number of lives they have.'''
    global heart, heartBroken, heart1, heart2, heart3, lives
    gameFrame.after(1500, lambda: gameFrame.itemconfigure(
        livesTextRectangle, fill=""))
    if lives == 3:
        gameFrame.itemconfigure(heart1, image=heart)
        gameFrame.itemconfigure(heart2, image=heart)
        gameFrame.itemconfigure(heart3, image=heart)
    elif lives == 2:
        gameFrame.itemconfigure(heart1, image=heartBroken)
        gameFrame.itemconfigure(heart2, image=heart)
        gameFrame.itemconfigure(heart3, image=heart)
    elif lives == 1:
        gameFrame.itemconfigure(heart1, image=heartBroken)
        gameFrame.itemconfigure(heart2, image=heartBroken)
        gameFrame.itemconfigure(heart3, image=heart)
    else:
        gameFrame.itemconfigure(heart1, image=heartBroken)
        gameFrame.itemconfigure(heart2, image=heartBroken)
        gameFrame.itemconfigure(heart3, image=heartBroken)


def pause(event):
    '''Pause or unpause the game, and display the paused frame.'''
    global paused, pauseFrameActive, gameActive, randomizeRepeatNum, scoreUpRepeatNum, \
        timeRepeatNum, scoreTimeRepeatNum
    if gameActive == True:  # Only change paused state if playing game
        if paused:
            paused = False
            pauseFrameActive = False
            gameFrame.pack(fill="both", expand=True)
            pauseFrame.pack_forget()
            gameLoop()  # Re-run game
        else:
            window.configure(cursor="")  # Re-enable cursor
            paused = True
            pauseFrameActive = True
            gameFrame.pack_forget()
            pauseFrame.pack(fill="both", expand=True)
            # Stop after loops
            gameFrame.after_cancel(randomizeRepeatNum)
            gameFrame.after_cancel(timeRepeatNum)
            gameFrame.after_cancel(scoreTimeRepeatNum)
            if scoreUpRepeatNum != 0:
                gameFrame.after_cancel(scoreUpRepeatNum)
            if slowed:
                gameFrame.after_cancel(slowTextRepeatNum)
                gameFrame.after_cancel(unslowRepeatNum)
            if invincible:
                gameFrame.after_cancel(invincibilityTextRepeatNum)
                gameFrame.after_cancel(disableInvincibilityRepeatNum)

def updateDifficulty(increase):
    '''Updates the difficulty every 30 seconds to speed up the balls'''
    global difficulty

    # If we are increasing the difficulty, then raise it by one, until we hit difficulty 5
    if increase == True:
        if time % 30 == 0 and difficulty < 5:
            difficulty += 1

            # Edit the difficulty text
            gameFrame.itemconfigure(difficultyText, text="Difficulty: " + str(difficulty))
            gameFrame.itemconfigure(difficultyTextRectangle, fill="lime")
            gameFrame.after(2000, lambda: updateDifficulty(False))  # After two seconds, disable the fill

            # Show respective info text
            if difficulty < 5:
                editInfoText("Difficulty up!", 2000)
            else:
                editInfoText("Final Difficulty!!", 2000)

    # If we aren't increasing the difficulty, we are disabling the fill of the text
    else:
        gameFrame.itemconfigure(difficultyTextRectangle, fill="")

# ---------------------------------------------- POWER UP FUNCTIONS -----------------------------------------------------------------------


def randomizeAbility():
    '''Chooses a random ability to put on the screen, or update its position if still on the screen.'''
    global randomizeRepeatNum, previousAbility, abilityNum, abilities, gameFrame
    availableAbilities = []

    # Only add the ability if it is hidden and it wasn't the last ability
    for i in range(1, 4):
        if not abilities[i] and i != previousAbility:
            # The delete balls ability only available after difficulty 2
            if i == 3:
                if difficulty >= 2:
                    availableAbilities.append(i)
            else:
                availableAbilities.append(i)
    
    # If all abilities are on screen, choose a random one to move, or choose from the hidden ones
    if availableAbilities == []:
        choices = [1,2,3]
        del choices[i-1]
        abilityNum = choices[randint(0, 1)]
        updateAbilityCoords(abilityNum)
    elif len(availableAbilities) == 1:
        abilityNum = availableAbilities[0]
        createAbility(abilityNum)
    else:
        abilityNum = availableAbilities[randint(0, len(availableAbilities)-1)]
        createAbility(abilityNum)

    previousAbility = abilityNum
    if cheats[2] == True:  # Half ability cool down if that cheat is on
        randomizeRepeatNum = gameFrame.after(6000, randomizeAbility)
    else:
        randomizeRepeatNum = gameFrame.after(12000, randomizeAbility)


def updateAbilityCoords(abilityNum):
    '''Updates the coordinates of an ability'''
    global abilities
    xPos = randint(100, 1790)
    yPos = randint(100, 950)
    if not abilities[abilityNum]:
        createAbility(abilityNum)
    gameFrame.coords(abilities[abilityNum], xPos, yPos)

def createAbility(abilityNum):
    '''Creates new ability.'''
    global abilities, upArrow, ghost, clock, delete
    xPos = randint(100, 1790)
    yPos = randint(100, 950)
    image = None
    match abilityNum:
        case 0:
            image = upArrow
        case 1:
            image = ghost
        case 2:
            image = clock
        case 3:
            image = delete
    abilities[abilityNum] = gameFrame.create_image(xPos, yPos, image=image)


def scoreUp():
    '''Increases the score by 50 after the scoreUp power-up is collected.'''
    global score, abilities, scoreUpRepeatNum
    score += 50
    if cheats[2] == True:  # Half ability cool down if that cheat is on
        scoreUpRepeatNum = gameFrame.after(2000, lambda: createAbility(0))
    else:
        scoreUpRepeatNum = gameFrame.after(4000, lambda: createAbility(0))
    editInfoText("+50 Score", 1000)


def invincibility(invincibleFromMain):
    '''Gain invincibility from balls after collecting the invinsible ability.'''
    global invincible, invincibilityCount, disableInvincibilityRepeatNum, beenHit
    if invincibleFromMain == True:  # If this function was triggered by collecting an ability, increase the count
        invincibilityCount += 1
    if not invincible and invincibilityCount != 0:
        invincible = True
        disableInvincibilityRepeatNum = gameFrame.after(
            5000, disableInvincibility)
        updateInvincibilityText()
        if not beenHit:  # Only show "Invincible!" if they collected ability
            editInfoText("Invincible!", 1250)
    gameFrame.itemconfigure(player, fill="#a1fc03")
    gameFrame.itemconfigure(warpedPlayer, fill="#a1fc03")
    if beenHit:  # Only hide ability if the invincibility didn't occur due to the player being hit
        beenHit = False


def disableInvincibility():
    '''Disabled invincibility after 5 seconds.'''
    global invincible, invincibilityCount
    invincible = False
    gameFrame.itemconfigure(player, fill=playerColour)
    gameFrame.itemconfigure(warpedPlayer, fill=playerColour)
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
        unslowRepeatNum = gameFrame.after(5000, unslowTime)
        updateSlowText()
        editInfoText("Time Slowed!", 1250)


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
        tempCoords = gameFrame.coords(tempBall)
        gameFrame.coords(
            tempBall, tempCoords[0]-20, tempCoords[1]-20, tempCoords[2]+20, tempCoords[3]+20)
        window.update()
        sleep(0.33)
        gameFrame.delete(tempBall)
    editInfoText(str(deleteNum) + " Balls Deleted", 1500)


def updateInvincibilityText():
    '''Updates the invincibility text with the amount of time left.'''
    global invincibilityTextCount, invincibilityTextRepeatNum
    if invincibilityTextCount == 0:
        invincibilityTextCount = 5
    else:
        invincibilityTextCount -= 1
    gameFrame.itemconfigure(
        invincibilityText, text="Invincibility: " + str(invincibilityTextCount))

    # Configure colour of rectangle according to time left
    if invincibilityTextCount >= 3:
        gameFrame.itemconfigure(invincibilityTextRectangle, fill="lime")
    elif invincibilityTextCount == 2:
        gameFrame.itemconfigure(invincibilityTextRectangle, fill="orange")
    elif invincibilityTextCount == 1:
        gameFrame.itemconfigure(invincibilityTextRectangle, fill="red")

    # Call function again if timer isn't over
    if invincibilityTextCount != 0:
        invincibilityTextRepeatNum = gameFrame.after(
            1000, updateInvincibilityText)
    else:
        gameFrame.itemconfigure(invincibilityTextRectangle, fill="")


def updateSlowText():
    '''Updates the slow text with the amount of time left.'''
    global slowTextCount, slowTextRepeatNum
    if slowTextCount == 0:
        slowTextCount = 5
    else:
        slowTextCount -= 1
    gameFrame.itemconfigure(slowText, text="Slow Time: " + str(slowTextCount))

    # Configure colour of rectangle according to time left
    if slowTextCount >= 3:
        gameFrame.itemconfigure(slowTextRectangle, fill="lime")
    elif slowTextCount == 2:
        gameFrame.itemconfigure(slowTextRectangle, fill="orange")
    elif slowTextCount == 1:
        gameFrame.itemconfigure(slowTextRectangle, fill="red")

    # Call function again if timer isn't over
    if slowTextCount != 0:
        slowTextRepeatNum = gameFrame.after(1000, updateSlowText)
    else:
        gameFrame.itemconfigure(slowTextRectangle, fill="")


def editInfoText(text, time):
    '''Takes a parameter text and edits the info text correspondingly.'''
    global textBuffer
    if text != None:  # If this function was called by hideInfoText, don't add text to buffer
        textTime = [text, time]
        textBuffer.append(textTime)
    # If there isn't any other text being displayed, display it
    if len(textBuffer) == 1 or text == None:
        gameFrame.itemconfigure(
            gameInfoText, text=textBuffer[0][0], state="normal")
        gameFrame.after(textBuffer[0][1], hideInfoText)  # Hide the text afterwards


def hideInfoText():
    '''Hides the text that appears in the middle of the screen whenever they get an ability or lose a life.'''
    global textBuffer
    gameFrame.itemconfigure(gameInfoText, state="hidden")
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
        balls.append(gameFrame.create_oval(xy, fill="black", width=2))
        numBalls += 1
        xSpeed.append(0)
        ySpeed.append(0)

    # Move the ball by giving its speed and colour
    else:
        # If slow time ability is active, half speed values
        # Determine the speed based on the difficulty
        global slowed, difficulty
        if slowed == True:
            if difficulty == 1:  # TODO Play around with time and speed of balls/player to reduce lag
                speedValues = [1, 2]
            elif difficulty == 2:
                speedValues = [1, 4]
            elif difficulty == 3:
                speedValues = [2, 5]
            elif difficulty == 4:
                speedValues = [3, 5]
            else:
                speedValues = [3, 6]
            colourBounds = [5, 4, 2]
        else:
            if difficulty == 1:
                speedValues = [2, 4]
            elif difficulty == 2:
                speedValues = [2, 8]
            elif difficulty == 3:
                speedValues = [4, 10]
            elif difficulty == 4:
                speedValues = [6, 10]
            else:
                speedValues = [6, 12]
            colourBounds = [10, 8, 4]

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
            gameFrame.itemconfigure(
                balls[numBalls-1], fill="#ff0000", outline="black")
        elif averageSpeed >= colourBounds[1]:
            gameFrame.itemconfigure(
                balls[numBalls-1], fill="#d303fc", outline="black")
        elif averageSpeed >= colourBounds[2]:
            gameFrame.itemconfigure(
                balls[numBalls-1], fill="blue", outline="black")
        else:
            gameFrame.itemconfigure(
                balls[numBalls-1], fill="black", outline="black")


def moveBalls():
    '''Responsible for checking collisions with the wall, between balls and the player, and moving each ball.'''
    for i in range(len(balls)):
        pos = gameFrame.coords(balls[i])
        # Check the ball for collision with wall
        if pos[3] > 1080 or pos[1] < 0:
            ySpeed[i] = -ySpeed[i]
        if pos[2] > 1920 or pos[0] < 0:
            xSpeed[i] = -xSpeed[i]

        # Check the ball for collision with other balls
        for j in range(len(balls)):
            if i == j:  # Skip if you are comparing the same ball
                continue
            pos2 = gameFrame.coords(balls[j])
            if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1]:
                ySpeed[i] = -ySpeed[i]
                xSpeed[i] = -xSpeed[i]
                ySpeed[j] = -ySpeed[j]
                xSpeed[j] = -xSpeed[j]

        gameFrame.move(balls[i], xSpeed[i], ySpeed[i])


# ---------------------------------------------- PLAYER FUNCTIONS ----------------------------------------------------

# TODO Play around with time and speed of balls/player to reduce lag
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


def movePlayer():
    '''Moves the player, and handles any logic to do with moving across boundaries'''
    gameFrame.move(player, playerDirectionX, playerDirectionY)

    mainPlayerPos = gameFrame.coords(player)
    warpedPlayerPos = gameFrame.coords(warpedPlayer)

    # Check if main player is off screen on all 4 sides
    if mainPlayerPos[0] < 0:  # Left
        distanceOffScreen = 0 - mainPlayerPos[0]
        newX1Coord = 1920 - distanceOffScreen
        gameFrame.coords(warpedPlayer, newX1Coord, mainPlayerPos[1], newX1Coord+50, mainPlayerPos[3])
        gameFrame.itemconfig(warpedPlayer, state="normal")
    elif mainPlayerPos[1] < 0:  # Up
        distanceOffScreen = 0 - mainPlayerPos[1]
        newY1Coord = 1080 - distanceOffScreen
        gameFrame.coords(warpedPlayer, mainPlayerPos[0], newY1Coord, mainPlayerPos[2], newY1Coord+50)
        gameFrame.itemconfig(warpedPlayer, state="normal")
    elif mainPlayerPos[2] > 1920:  # Right
        distanceOffScreen = mainPlayerPos[2] - 1920
        newX2Coord = 0 + distanceOffScreen
        gameFrame.coords(warpedPlayer, newX2Coord-50, mainPlayerPos[1], newX2Coord, mainPlayerPos[3])
        gameFrame.itemconfig(warpedPlayer, state="normal")
    elif mainPlayerPos[3] > 1080:  # Down
        distanceOffScreen = mainPlayerPos[3] - 1080
        newY2Coord = 0 + distanceOffScreen
        gameFrame.coords(warpedPlayer, mainPlayerPos[0], newY2Coord-50, mainPlayerPos[2], newY2Coord)
        gameFrame.itemconfig(warpedPlayer, state="normal")

    # If warped player is entirely on screen and visible, replace this with main player
    if (warpedPlayerPos[3] <= 1080 and warpedPlayerPos[1] >= 0 and warpedPlayerPos[2] <= 1920 and warpedPlayerPos[0] >= 0 and gameFrame.itemcget(warpedPlayer, "state") == "normal") \
        and (mainPlayerPos[1] > 1080 or mainPlayerPos[3] < 0 or mainPlayerPos[0] > 1920 or mainPlayerPos[2] < 0):
        gameFrame.coords(player, warpedPlayerPos)
        gameFrame.itemconfig(warpedPlayer, state="hidden")
    # Hide warped player if player is entirely on screen
    elif mainPlayerPos[3] <= 1080 and mainPlayerPos[1] >= 0 and mainPlayerPos[2] <= 1920 and mainPlayerPos[0] >= 0:
        gameFrame.itemconfig(warpedPlayer, state="hidden")


def checkPlayerCollision():
    '''Checks if the player is touching a ball, the wall or any abilities.'''
    # Check collision with wall
    global gameActive, cheats, abilities, lives
    positions = []
    positions.append(gameFrame.coords(player))
    if gameFrame.itemcget(warpedPlayer, "state") == "normal":
        positions.append(gameFrame.coords(warpedPlayer))

    for pos in positions:

        # Check collision with all abilities
        scoreUpCollision(pos)
        invincibleCollision(pos)
        slowTimeCollision(pos)
        deleteBallsCollision(pos)

        # Only check if player has collided with any ball if invincibility is disabled
        if cheats[1] != True and invincible != True:
            for i in range(len(balls)):
                pos2 = gameFrame.coords(balls[i])
                if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
                        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
                    hit()


def scoreUpCollision(pos):
    '''Takes the players position as argument and checks if they collided with the scoreUp ability'''
    global abilities
    # Don't check if ability doesn't exist
    if not abilities[0]:
        return
    pos2 = gameFrame.coords(abilities[0])
    if not pos2:
        return
    pos2 = [pos2[0]-20, pos2[1]-25, pos2[0]+20, pos2[1]+25]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        gameFrame.delete(abilities[0])
        abilities[0] = None
        scoreUp()


def invincibleCollision(pos):
    '''Takes the players position as argument and checks if they collided with the invincible ability'''
    # Don't check if ability doesn't exist
    if not abilities[1]:
        return
    pos2 = gameFrame.coords(abilities[1])
    if not pos2:
        return
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        gameFrame.delete(abilities[1])
        abilities[1] = None
        invincibility(True)


def slowTimeCollision(pos):
    '''Takes the players position as argument and checks if they collided with the slow time ability'''
    # Don't check if ability doesn't exist
    if not abilities[2]:
        return
    pos2 = gameFrame.coords(abilities[2])
    if not pos2:
        return
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        gameFrame.delete(abilities[2])
        abilities[2] = None
        slowTime(True)


def deleteBallsCollision(pos):
    '''Takes the players position as argument and checks if they collided with the delete balls ability'''
    # Don't check if ability doesn't exist
    if not abilities[3]:
        return
    pos2 = gameFrame.coords(abilities[3])
    pos2 = [pos2[0]-20, pos2[1]-20, pos2[0]+20, pos2[1]+20]
    if pos[0] < pos2[2] and pos[2] > pos2[0] and pos[1] < pos2[3] and pos[3] > pos2[1] \
        or pos[0] > pos2[2] and pos[2] < pos2[0] and pos[1] > pos2[3] and pos[3] < pos2[1]:
        gameFrame.delete(abilities[3])
        abilities[3] = None
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
        gameFrame.itemconfigure(livesTextRectangle, fill="#fc0390")
        editInfoText(str(lives) + " lives remaining", 2000)
    if lives == 0:
        gameActive = False


def hitAnimation(repeat):
    '''The animation that is played whenever the player is hit.'''
    tempCoords = gameFrame.coords(player)
    warpedTempCoords = gameFrame.coords(warpedPlayer)
    if repeat == True:
        gameFrame.coords(
            player, tempCoords[0]+10, tempCoords[1]+10, tempCoords[2]-10, tempCoords[3]-10)
        gameFrame.coords(
            warpedPlayer, warpedTempCoords[0]+10, warpedTempCoords[1]+10, warpedTempCoords[2]-10, warpedTempCoords[3]-10)
        gameFrame.itemconfigure(player, fill="red")
        gameFrame.itemconfigure(warpedPlayer, fill="red")
        window.update()
        sleep(0.4)
        hitAnimation(False)
    else:
        gameFrame.coords(
            player, tempCoords[0]-10, tempCoords[1]-10, tempCoords[2]+10, tempCoords[3]+10)
        gameFrame.coords(
            warpedPlayer, warpedTempCoords[0]-10, warpedTempCoords[1]-10, warpedTempCoords[2]+10, warpedTempCoords[3]+10)
        window.update()
        sleep(0.4)
        gameFrame.itemconfigure(player, fill=playerColour)
        gameFrame.itemconfigure(warpedPlayer, fill=playerColour)


def deathAnimation():
    '''When the player dies, shrink the player.'''
    tempCoords = gameFrame.coords(player)
    warpedTempCoords = gameFrame.coords(warpedPlayer)
    gameFrame.itemconfigure(player, fill="red")
    gameFrame.itemconfigure(warpedPlayer, fill="red")
    for shrink in range(5):
        for coordinate in range(4):
            if coordinate <= 1:
                if cheats[0] == True:
                    tempCoords[coordinate] += 2
                    warpedTempCoords[coordinate] += 2
                else:
                    tempCoords[coordinate] += 5
                    warpedTempCoords[coordinate] += 5
            else:
                if cheats[0] == True:
                    tempCoords[coordinate] -= 2
                    warpedTempCoords[coordinate] -= 2
                else:
                    tempCoords[coordinate] -= 5
                    warpedTempCoords[coordinate] -= 5
        gameFrame.coords(player, tempCoords)
        gameFrame.coords(warpedPlayer, warpedTempCoords)
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
            playerPos = gameFrame.coords(player)
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
                tempCoords = gameFrame.coords(ability)
                for coordinate in tempCoords:
                    saveFile.write(str(coordinate) + "\n")
            for variable in range(3):
                for ball in range(numBalls):
                    if variable == 0:  # Write all ball coordinates
                        ballPos = gameFrame.coords(balls[ball])
                        for coordinate in ballPos:
                            saveFile.write(str(coordinate) + "\n")
                        saveFile.write(gameFrame.itemcget(
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
            gameFrame.after(1000, lambda: swapFrames(0))


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
            invincibilityCount, playerCoords, ballPos, xSpeed, ySpeed, cheated
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
        initialiseGame(None, True)


# ---------------------------------------------- MAIN PROGRAM --------------------------------------------------------
configureWindow()
initialiseMenu()
changeBackground(bgColour)
initialiseKeybinds()
homeFrame.pack(fill="both", expand=True)  # Start at the home page
window.mainloop()
