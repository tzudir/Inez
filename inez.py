import sys, math, random, pyttsx3, webbrowser, datetime, time, urllib3, string, platform, json, pyautogui, vlc, os
import urllib.request, requests, re, pafy
from bs4 import *
import speech_recognition as sr
from PyQt5 import QtGui, QtCore, QtWidgets

##lists and dictionaries
conjunctions = ['For', 'And', 'Nor', 'But', 'Or', 'Yet', 'So', 'After', 'Although', 'As', 'Because', 'Before', 'If',
                'Once', 'Since', 'Though', 'Unless', 'Until', 'When', 'Where', 'While']

prepositions = ['About', 'Above', 'Across', 'After', 'Against', 'Along', 'Amid', 'Among', 'Around', 'At', 'Before',
                'Behind', 'Below', 'Beneath', 'Beside', 'Besides', 'Between', 'Beyond', 'By', 'Down', 'In', 'Inside',
                'Into', 'Near', 'Of', 'Off', 'On', 'Onto', 'Opposite', 'Outside', 'Over', 'Past', 'To', 'Toward',
                'Towards', 'Under', 'Underneath', 'Until', 'Up', 'Upon', 'Versus', 'Via', 'With', 'Within']

articles = ['A', 'An', 'The']

specialChars = {'hyphen': '-', 'Dash': '-', 'dot': '.', 'full stop': '.', 'comma': ',', 'exclamation mark': '!',
                'forward slash': '/', 'backslash': '\\', 'backward slash': '\\', 'at the rate': '@', 'hash': '#',
                'dollar sign': '$', 'percent sign': '%', 'caret': '^', 'circumflex': '^', 'ampercent': '&',
                'and sign': '&', 'Asterisk': '*', 'asterisk': '*', 'parentheses open': '(', 'parentheses close': ')',
                'parentheses': '()', 'round bracket open': '(', 'round bracket close': ')', 'plus sign': '+',
                'vertical bar': '|', 'pipe sign': '|', 'curly bracket open': '{', 'curly bracket close': '}',
                'square bracket open': '[', 'square bracket close': ']', 'angle bracket open': '<',
                'angle bracket close': '>', 'question mark': '?', 'tilde': '~', 'grave sign': '`',
                'double inverted quotes': '"', 'double inverted comma': '"', 'inverted quotes': "'",
                'inverted comma': "'", 'single inverted quotes': "'", 'single inverted comma': "'", 'colon': ':',
                'semicolon': ';'}

mExtTypes = [['.mp3', '.wav', '.wma', '.m4a', '.xspf'],
             ['.mp4', '.mkv', '.avi', '.webm', '.3gp', '.gif', '.wmv', '.mov', '.vob', '.flv']]

#greetings
greets = ['hi', 'hello', 'hello there', 'hi there', 'hey', 'hey there', 'namaste', 'hola','Howdy']

#questions
toggleListening = [
    ['start listening', 'listen', 'Inez listen', 'start listening', 'Inez start listening',
     'resume listening'],
    ['on hold', 'stop listening', 'stop listening', 'Inez stop listening', 'pause listening']]

helpcom = ['show all commands', 'show help', 'help', 'show commands', 'show help commands', 'all commands']

info = ['summarize the project', 'project summary', 'tell me something about you in details', 'details about you',
        'your project summary', 'project summary and details', 'project details']
        
closing = ['terminate conversation', 'terminate now', 'exit chat', 'exit now', 'terminate', 'close chat',
           'close conversation', 'close yourself', 'exit conversation', 'end now', 'end chat', 'end conversation']

botcall = ['how is everything Inez', 'Inez how are you', 'how are you', 'how are you Inez', 'how are you doing',
           'how are you doing Inez', 'how is everything going on', "what's up Inez"]

frequest = [['what is the time right now', "what's the time right now", 'what time is it right now', "what's the time",
             'what time is it in the clock', 'what is the time', "what's the time now", 'what time is it now',
             'tell me the time'],
            ["what's the date today", 'what is the date today', "today's date is", "tell me today's date",
             "today's date is"],
            ["what is today's day", "what's today's day", 'what is the day today', "today's day is",
             "tell me today's day"]]

greets2 = ['hey Inez', 'hi Inez', 'hello Inez']

readycheck = ['Inez', 'you there Inez', 'are you there Inez', 'Inez are you there', 'Inez you there',
              'are you ready', 'Inez are you ready', 'you ready Inez', 'Inez you ready']

botintro = ['who are you', "what's your name", 'who am I talking to', 'what are you', 'what is your name',
            'what are you called', 'what do people call you']

weatherRep = ['how is the weather today', 'current weather conditions', 'how is the weather', 'weather conditions',
              'weather forecast']

typeMode = ['typing mode on', 'typing mode off']

joke_request = ['tell me a joke', 'tell a joke', 'please tell a joke']

whereAbouts = ['where am I', 'what is my location', 'what is my current location', "what's my location",
               "what's my current location", 'get my location', 'what is this place']

mPlayerToggle = [['play', 'start playing', 'resume playing', 'play that', 'play media'],
                 ['pause', 'hold it', 'pause media', 'pause that'],
                 ['stop', 'stop playing', 'stop media', 'close media']]

mMediaType = [['song', 'music'], ['video', 'visual'], ['movie', 'film']]

automateKBoard = [
    ['close', 'close that', 'close the program', 'close active window', 'close this program', 'close this'],
    ['new tab', 'open new tab', 'start new tab', 'open in new tab', 'make new tab', 'start in new tab'],
    ['enter', 'press enter', 'press return', 'type enter', 'type return', 'press enter button', 'press return button',
     'press enter key', 'press return key', 'enter key'],
    ['press right enter', 'right enter', 'press right enter button', 'press right return', 'press right return button',
     'right enter key', 'press right enter key', 'press right return key', 'right return key'],
    ['backspace', 'press backspace', 'press backspace button', 'type backspace', 'backspace key',
     'press backspace key'], ['delete', 'delete key', 'press delete key', 'press delete', 'press delete button'],
    ['tab', 'tab key', 'tab button', 'press tab key', 'press tab button', 'press tab'],
    ['shift', 'left shift', 'press left shift', 'left shift key', 'press left shift key', 'press left shift button',
     'press shift', 'press shift key', 'press shift button', 'left shift button'],
    ['right shift', 'right shift key', 'right shift button', 'press right shift key', 'press right shift button'],
    ['caps lock', 'press caps lock', 'caps lock key', 'caps lock button', 'press caps lock key',
     'press caps lock button'],
    ['num lock', 'press num lock', 'num lock key', 'num lock button', 'press num lock key', 'press num lock button'],
    ['control', 'left control', 'control button', 'control key', 'left control key', 'left control button',
     'press control key', 'press control button', 'press left control key', 'press left control button'],
    ['alter', 'left alter', 'press left alter', 'press alter', 'alter key', 'left alter key', 'alter button',
     'left alter button', 'press alter key', 'press alter button', 'press left alter key', 'press left alter button'],
    ['right alter', 'right alter key', 'right alter button', 'press right alter', 'press right alter key',
     'press right alter button'],
    ['right control', 'right control key', 'right control button', 'press right control', 'press right control key',
     'press right control button'],
    ['escape', 'press escape', 'escape key', 'escape button', 'press escape key', 'press escape button'],
    ['page up', 'page up key', 'scroll down', 'scroll right', 'page up button', 'press page up', 'press page up key',
     'press page up button'],
    ['page down', 'page down key', 'scroll up', 'scroll left', 'page down button', 'press page down',
     'press page down key', 'press page down button'],
    ['space', 'space bar', 'space bar key', 'space bar button', 'press space bar', 'press space bar key',
     'press space bar button'],
    ['screenshot', 'new screenshot', 'take screenshot', 'create screenshot', 'click a screenshot', 'get screenshot',
     'get a screenshot', 'click screenshot']]

#replies
botans = ['I am fine...', 'I am doing great...', 'I\'m fine, thank you...', 'I am glad you asked, thank you...',
          'Everything is good... thank you...', 'Everything is great...', 'Everything Seems good...']

compos = ['At your service', 'Ask me', 'Waiting for your command', 'Tell me something to do', 'How can I help you?']

byes = ['until next time', 'bye bye', 'see you soon', 'chao', 'goodbye', 'catch you later', 'see you next time',
        'see you later']

introans = ['I am Inez, your virtual personal assistant', 'They call me "Inez"', 'People call me "Inez"',
            'My name is Inez']

readyans = ['I am online and ready...', 'Ready', 'Up and running...', 'Always ready to help and assist...']

projectDetails = "Inez is a virtual assistant developed for better accessiblity and interactivity in an open source environment. This vitual assistant is used to perform some regular tasks like - Getting Date, Time or Day, Simple arithmetic calculations, and Even searching almost anything on internet. These tasks can be performed just by using some voice commands. The project is developed in python."
 
webSearch = ['found something...', 'This is what I found...', 'Here is what I found on the Internet...',
             'Here is what I found...', 'Found something...', 'I got this on the Internet...']

jokes = ['What do you call a can opener that does not work? A cant opener!', 'Did you hear about the Italian chef who died? He pasta-way',
          'What is Forrest Gumps email password? 1forrest1', 'Whats red and bad for your teeth? A brick',
          'Why dont dinosaurs talk? Because they are dead']

#properties for objects and modules:
Bot = "Inez"

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 40)

global opr

mic_recog = sr.Recognizer()
mic = sr.Microphone()

#all functions
def listenToggle(
    command): 
    if(command in toggleListening[1]):
        while True:
            with mic as source:
                audio = mic_recog.listen(source)

            try:
                value = mic_recog.recognize_google(audio)

                if str is bytes:
                    toggleCommand = ("{}".format(value).encode("utf-8"))
                    
                    if (toggleCommand in toggleListening[0]):
                        break
                
                else:
                    toggleCommand = ("{}".format(value))

                    if (toggleCommand in toggleListening[0]):
                        break
            
            except sr.UnknownValueError:
                print("Unable to understand")

#play multimedia
def playMedia(mName, mFilePath):
    for root, dirs, files in os.walk(mFilePath):
        for fileFound in files:
            global mediaName
            if (((mName.lower() in fileFound.lower()) and (mFilePath == 'C:/Users/realj/Music/'))):
                mFileExt = os.path.splitext(fileFound)
                if (mFileExt[1] in mExtTypes[0]):
                    mediaName = os.path.join(root, fileFound)
            
            elif (((mName.lower() in fileFound.lower()) and ((mFilePath == 'C:/Users/realj/Videos/')))):
                mFileExt = od.path.splitext(fileFound)
                if (mFileExt[1] in mExtTypes[1]):
                    mediaName = os.path.join(root, fileFound)

#multimedia state toggle
def mMediaToggle(command): 
    if (command in mPlayerToggle[0]):
        try:
            playMFile.play()
        except:
            print("Playing media operation cannot be performed")
    elif(command in mPlayerToggle[1]):
        try:
            playMFile.pause()
        except:
            print("pausing media operations not possible")
    elif (command in mPlayerToggle[2]):
        try:
            playMFile.stop()
        except:
            print("Stopping media operations cannot be performed")

#toggle typing mode
def getTypeData():
    engine.say("Typing Mode is turned on..")
    engine.runAndWait()

    while True:
        with mic as source:
            audio = mic_recog.listen(source)
        try:
            value = mic_recog.recognize_google(audio)

            if str is bytes:
                typeData = ("{}".format(value).encode("utf-8"))
                if (typeData == typeMode[1]):
                    break
                elif any(typeData in subl for subl in automateKBoard):
                    keyBoardAutomater(typeData)
                elif (typeData in specialChars):
                    pyautogui.typewrite(typeData)
                else:
                    pyautogui.typewrite((typeData), interval=0.05)

            else:
                typeData = ("{}".format(value))
                if (typeData == typeMode[1]):
                    break
                elif any(typeData in subl for subl in automateKBoard):
                    keyBoardAutomater(typeData)
                elif (typeData in specialChars):
                    pyautogui.typewrite(typeData)
                else:
                    pyautogui.typewrite((typeData), interval=0.05)

        except sr.UnknownValueError:
            engine.say("Please repeat !")
            engine.runAndWait()

    engine.say("Typing mode is turned off")
    engine.runAndWait()

#activate windows operation
def keyBoardAutomater(
        inputCommand):
    if (inputCommand in automateKBoard[0]):
        pyautogui.hotkey('altleft', 'f4')
    elif (inputCommand in automateKBoard[1]):
        pyautogui.hotkey('ctrlleft', 't')
    elif (inputCommand in automateKBoard[2]) or (inputCommand in automateKBoard[3]):
        pyautogui.hotkey('enter')
    elif (inputCommand in automateKBoard[4]):
        pyautogui.hotkey('backspace')
    elif (inputCommand in automateKBoard[5]):
        pyautogui.hotkey('delete')
    elif (inputCommand in automateKBoard[6]):
        pyautogui.hotkey('tab')
    elif (inputCommand in automateKBoard[7]):
        pyautogui.hotkey('shiftleft')
    elif (inputCommand in automateKBoard[8]):
        pyautogui.hotkey('shiftright')
    elif (inputCommand in automateKBoard[9]):
        pyautogui.hotkey('capslock')
    elif (inputCommand in automateKBoard[10]):
        pyautogui.hotkey('numlock')
    elif (inputCommand in automateKBoard[11]):
        pyautogui.hotkey('ctrlleft')
    elif (inputCommand in automateKBoard[12]):
        pyautogui.hotkey('altleft')
    elif (inputCommand in automateKBoard[13]):
        pyautogui.hotkey('altright')
    elif (inputCommand in automateKBoard[14]):
        pyautogui.hotkey('ctrlright')
    elif (inputCommand in automateKBoard[15]):
        pyautogui.hotkey('escape')
    elif (inputCommand in automateKBoard[16]):
        pyautogui.hotkey('pgup')
    elif (inputCommand in automateKBoard[17]):
        pyautogui.hotkey('pgdn')
    elif (inputCommand in automateKBoard[18]):
        pyautogui.hotkey('space')
    elif (inputCommand in automateKBoard[19]):
        pyautogui.hotkey('win', 'prtscr')
    elif (inputCommand == typeMode[0]):
        getTypeData()

#Get Location
def getLoc(): 
    f = urllib.request.urlopen('https://ip-api.com/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    location_city = location['city']
    location_state = location['regionName']
    location_country = location['country']
    location_zip = location['zip']
    reply = ("Your current location is : %s, %s, %s.") % (location_city, location_state, location_country)
    engine.say(reply)
    txt.insertPlainText(Bot + " : " + reply + "\n")


def getLocalWeather():
    f = urllib.request.urlopen('https://ip-api.com/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    location_city = location['city']
    location_state = location['regionName']
    location_country = location['country']
    location_zip = location['zip']

    f = urllib.request.urlopen("https://api.wunderground.com/api/73a91fc9316a85f8/geolookup/conditions/q/" + location_country + "/" + location_city + ".json")
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    weatherType = parsed_json['current_observation']['weather']
    temp_c = parsed_json['current_observation']['temp_c']
    degSym = u'\xb0'
    reply = ("Current temperature in %s is %s" + degSym + "C,with % weather.") % (location, temp_c, weatherType)
    engine.say(reply)
    txt.insertPlainText(Bot + " : " + reply + "\n")
    f.close()
    engine.runAndWait()

now = datetime.datetime.now()
t1 = ''


def tick():
    global t1
    t2 = time.strftime("%I:%M:%S %p")
    if t2 != t1:
        t1 = t2


def timing():
    tick()
    reply = ("Current time is " + t1)
    engine.say(reply)
    txt1 = txt.toPlainText()
    txt.insertPlainText(Bot + " :\nTime is : " + reply + "\n")
    engine.runAndWait()


date = now.strftime("%d-%B-%Y")
day = now.strftime("%A")

class guiWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(guiWindow, self).__init__()
        self.setGeometry(300, 150, 750, 500)
        self.setWindowTitle("Inez")
        self.setWindowIcon(QtGui.QIcon("ryan.jpeg"))
        self.setStyleSheet('background-color: #FDFEFE;')
        self.setFixedSize(1000, 850)

        global txt

        # creating label
        self.label = QtWidgets.QLabel(self)
        # loading image
        self.pixmap = QtGui.QPixmap('cats.png')
        # adding image to label
        self.label.setPixmap(self.pixmap)
        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())
        #self.label.setGeometry(400, 200, 400, 400)

        txt = QtWidgets.QTextEdit(self)
        txt.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        txt.setStyleSheet("QTextEdit {background-color: #FDFEFE; color: black; font-size: 14px; font-weight: bold;}")
        txt.setGeometry(250, 350, 500, 350)
        txt.setReadOnly(1)
        #txt.setVisible(False)

        self.process = QtWidgets.QProgressBar(self)
        self.process.setGeometry(250, 300, 585, 30)
        self.process.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: Yellow;"
                    "border-radius: 15px;"
                  "}")
        #self.process.setVisible(False)

        #self.closebtn()
        self.prnt()
        self.show()

    def prnt(self):
        btn1 = QtWidgets.QPushButton("Start", self)
        btn1.setStyleSheet('QPushButton {background-color: #ffd4aa; color: black; font-weight: bold; font-size: 23px; border-radius: 15px; border :5px solid ; border-top-color : black; border-left-color :black; border-right-color :black; border-bottom-color : black;}') 
        btn1.clicked.connect(self.inez)
        font = QtGui.QFont('SansSerif')
        btn1.setFont(font)
        btn1.resize(160, 55)
        btn1.move(400, 200)
        btn1.show()

    #main program body
    def inez(self):
        try:
            with mic as source:
                mic_recog.adjust_for_ambient_noise(source)

            start = "\nWelcome"  # User interaction starts here
            reply = (start)
            engine.say(reply)
            txt.insertPlainText(reply)
            engine.runAndWait()

            while True:
                with mic as source:
                    mic_recog.adjust_for_ambient_noise(source)

                txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())

                quest = random.choice(compos)
                engine.say(quest)
                txt.insertPlainText("\n\n" + quest + " : \n")
                engine.runAndWait()
                txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())

                with mic as source:
                    audio = mic_recog.listen(source)
                process = ("Processing...\n")
                txt.insertPlainText(process)
                self.completed = 0
                while self.completed < 100:
                    self.completed += 0.001
                    self.process.setValue(self.completed)

                try:
                    value = mic_recog.recognize_google(audio)

                    comms = ("{}".format(value))
                    print("You -> " + comms)
                        # Starts checking for the reply from here
                    if comms in greets or comms in greets2:  # If Command was a greeting
                        reply = random.choice(greets)
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply.capitalize() + "!\n")
                        engine.runAndWait()

                    elif comms in info:
                        reply = projectDetails
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply + "\n")
                        engine.runAndWait()

                    elif comms in helpcom:  # If command was to list all available commands
                        reply = "Following commands are stored for interaction and usage right now..."
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply + "\n")

                        txt.insertPlainText("Greeting commands -\n")
                        for i in range(8):
                            reply = greets[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        for i in range(3):
                            reply = greets2[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        txt.insertPlainText("\nIntroductory commands -\n")
                        for i in range(7):
                            reply = botintro[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        txt.insertPlainText("\nClosing commands -\n")
                        for i in range(12):
                            reply = closing[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        txt.insertPlainText("\nInteraction commands -\n")
                        for i in range(5):
                            reply = botcall[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        for i in range(9):
                            reply = readycheck[i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        txt.insertPlainText("\nTime, Date and Day commands -\n")
                        for i in range(9):
                            reply = frequest[0][i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        for i in range(5):
                            reply = frequest[1][i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        for i in range(5):
                            reply = frequest[2][i]
                            txt.insertPlainText("\t-> " + reply + "\n")

                        txt.insertPlainText("\n Project info commands -\n")
                        for i in range(6):
                            reply = info[i]
                            txt.insertPlainText("\t->" + reply + "\n")

                        txt.insertPlainText("\n##### END OF COMMANDS #####\n")
                        engine.runAndWait()

                    elif comms in botintro:  # Commands for bot intro
                        reply = random.choice(introans)
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply)

                    elif comms in botcall:  # Interactive commands
                        reply = random.choice(botans)
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply)
                        engine.runAndWait()

                    elif comms in readycheck:  # Interactive commands
                        reply = random.choice(readyans)
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply)
                        engine.runAndWait()

                    elif comms in frequest[0]:  # Commands to know - Time, Date or Day.
                        timing()

                    elif comms in frequest[1]:
                        reply = date
                        engine.say("Today's date is " + reply)
                        txt.insertPlainText(Bot + " : " + "today's date is : " + reply + "\n")
                        engine.runAndWait()

                    elif comms in frequest[2]:
                        reply = day
                        engine.say("The day today is : " + reply)
                        txt.insertPlainText(Bot + " : " + "The day today is - " + reply + "\n")
                        engine.runAndWait()

                    elif comms in toggleListening[1]:
                        listenToggle(comms)

                    elif comms in weatherRep:  # Command to get 'weather' information for current location of execution
                        getLocalWeather()

                    elif (comms in automateKBoard) or (comms in typeMode):  # Automate keyboard keys and shortcuts
                        keyBoardAutomater(comms)

                    elif comms in whereAbouts:  # Automatically locate the location of execution
                        getLoc()

                    elif ((comms in mPlayerToggle[0]) or (comms in mPlayerToggle[1]) or (
                        comms in mPlayerToggle[2])):
                        mMediaToggle(comms)

                    elif (comms in joke_request):
                        reply = random.choice(jokes)
                        engine.say(reply)
                        txt.insertPlainText(Bot + " : " + reply)


                    elif (comms.startswith(
                                'play')):  # Condition for playing or starting a multimedia file (Song/Video/Music)
                                video_id = "_"
                                url = 'http://youtube.com/watch?v=' + video_id
                                video = pafy.new(url)
                                best = video.getbest()
                                playurl = best.url
                                player = vlc.MediaPlayer(playurl)
                                player.audio_set_volume(100)
                                if callback:
                                    callback()
                                player.play()
                                time.sleep(5)
                                while player.is_playing():
                                    time.sleep(1)
                                endcallback()
                                
                
                    elif (comms in closing) or (comms in byes):  # Commands to Exit program
                            reply = random.choice(byes)
                            engine.say(reply)

                            txt.insertPlainText(Bot + " : " + reply.capitalize() + "...\n")
                            engine.runAndWait()
                            sys.exit()

                    elif ('search' in comms) or ('search' and 'for' in comms) or ('define' in comms) or (
                            ('what' and 'is') in comms) or ((
                                                                'who' and 'is') in comms):  # Use 'Search', 'Search For', 'Define', 'who is' or 'what is' to find any definition online.
                        try:
                                commlist = (string.capwords(comms)).split()
                                listlen = len(commlist)
                                if (((commlist[0] == 'Define') or (commlist[0] == 'Search')) and (listlen <= 1)) or (((
                                        commlist[0] == 'What' and commlist[1] == 'Is') or (
                                        commlist[0] == 'Who' and commlist[1] == 'Is') or (
                                        commlist[0] == 'Search' and commlist[1] == 'For')) and (listlen <= 2)):
                                    raise

                                elif (commlist[0] == 'Define') or (commlist[0] == 'Search') or (
                                        commlist[0] == 'Search' and commlist[1] == 'For') or (
                                        commlist[0] == 'What' and commlist[1] == 'Is') or (
                                        commlist[0] == 'Who' and commlist[1] == 'Is') or (
                                        commlist[0] == 'Who' and commlist[1] == 'Are'):
                                    for x in range(listlen - 1):
                                        if (commlist[x] in conjunctions) or (commlist[x] in prepositions) or (
                                            commlist[x] in articles):
                                            commlist[x] = commlist[x].lower()

                                    if commlist[0] == 'Define':
                                        commlist.remove('Define')
                                    elif (commlist[0] == 'Search' and commlist[1] == 'for'):
                                        commlist.remove('Search')
                                        commlist.remove('for')
                                    elif commlist[0] == 'Search':
                                        commlist.remove('Search')
                                    elif (commlist[0] == 'What' and commlist[1] == 'Is'):
                                        commlist.remove('What')
                                        commlist.remove('Is')
                                    elif (commlist[0] == 'Who' and commlist[1] == 'Is'):
                                        commlist.remove('Who')
                                        commlist.remove('Is')
                                    elif (commlist[0] == 'Who' and commlist[1] == 'Are'):
                                        commlist.remove('Who')
                                        commlist.remove('Are')

                                    searchstr = commlist
                                    try:
                                        '''searchstr = "_".join(commlist)
                                        txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())
                                        wiki_search = ("https://en.wikipedia.org/wiki/" + searchstr)
                                        page = urllib.request.urlopen(wiki_search)
                                        soup = BeautifulSoup(page, "html.parser")
                                        reply = soup.find('h1', {'class': 'firstHeading'})
                                        txt.insertPlainText("\n" + reply.text + ":-\n")
                                        reply = soup.find('p')
                                        txt.insertPlainText("\t" + reply.text + "\n")
                                        engine.say(reply.text)'''

                                        searchstr = "_".join(commlist)
                                        txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())
                                        wiki_search = ("https://en.wikipedia.org/wiki/" + searchstr)
                                        page = urllib2.urlopen(wiki_search)
                                        soup = BeautifulSoup(page, "html.parser")
                                        reply = soup.find('h1', {'class': 'firstHeading'})
                                        txt.insertPlainText("\n" + reply.text + ":-\n")
                                        reply = soup.find('p')
                                        txt.insertPlainText("\t" + reply.text + "\n")
                                        engine.say(reply.text)

                                    except:
                                        searchstr = commlist
                                        search = random.choice(webSearch)
                                        concSay = " ".join(searchstr)
                                        engine.say(search + "about" + concSay)
                                        searchstr = "+".join(searchstr)
                                        webbrowser.open('http://www.google.com/search?q=' + searchstr)

                        except:
                                searchstr = commlist
                                search = random.choice(webSearch)
                                concSay = " ".join(searchstr)
                                engine.say(search + "about" + concSay)
                                searchstr = "+".join(searchstr)
                                webbrowser.open('http://www.google.com/search?q=' + searchstr)

                        
                    elif ('calculate' in comms):  # 'Calculate' for calculating arithmetic operations
                            commlist = comms.split()
                            try:
                                if (commlist[2] == '+') or (commlist[2] == 'subtracted') or (
                                    commlist[2] == 'added') or (commlist[2] == 'times') or (
                                    commlist[2] == 'multiplied') or (commlist[2] == 'divided') or (
                                    commlist[2] == 'into') or (commlist[2] == 'upon') or (commlist[2] == 'minus') or (
                                    commlist[2] == 'by') or (commlist[2] == 'x') or (commlist[2] == '-') or (
                                    commlist[2] == '/'):
                                    opr = commlist[2]

                                    # Basic arithmetic calculations -
                                    def calc():
                                        if (opr == '+') or (opr == 'added') or (opr == 'plus'):
                                            res = num1 + num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The sum would be ' + sol)
                                            engine.say('The sum would be ' + sol)
                                            txt.insertPlainText(Bot + " : " + n1 + ' + ' + n2 + ' = ' + sol + "\n")

                                        elif (opr == '-') or (opr == 'minus') or (opr == 'subtracted'):
                                            res = num1 - num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The difference would be ' + sol)
                                            engine.say('The difference would be ' + sol)
                                            txt.insertPlainText(Bot + " : " + n1 + ' - ' + n2 + ' = ' + sol + "\n")

                                        elif (opr == 'x') or (opr == 'into') or (opr == 'multiplied') or (
                                            opr == 'times'):
                                            res = num1 * num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The product would be ' + sol)
                                            engine.say('The product would be ' + sol)
                                            txt.insertPlainText(Bot + " : " + n1 + ' x ' + n2 + ' = ' + sol + "\n")

                                        elif (opr == '/') or (opr == 'divided') or (opr == 'upon') or (opr == 'by'):
                                            res = num1 / num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The result of division would be ' + sol)
                                            engine.say('The result would be ' + sol)
                                            txt.insertPlainText(Bot + " : " + n1 + ' / ' + n2 + ' = ' + sol + "\n")

                                        else:
                                            reply = "Only four basic arithmetic operations allowed right now..."
                                            engine.say(reply)
                                            txt.insertPlainText(reply + "\n")
                                            engine.runAndWait()

                                    if (commlist[3] == 'to') or (commlist[3] == 'by') or (commlist[3] == 'with'):
                                        oprprep = commlist[3]
                                        num1 = float(commlist[1])
                                        num2 = float(commlist[4])
                                        calc()
                                    else:
                                        num1 = float(commlist[1])
                                        num2 = float(commlist[3])
                                        calc()

                            except:
                                txt.insertPlainText('Sorry, couldn\'t understand that...\nPlease try again...')

                    else:
                            txt.insertPlainText(Bot + " =>\n" + "You said : '" + comms + "'\n")

                except sr.UnknownValueError as e:
                    txt.insertPlainText('Sorry, couldn\'t understand that... \nPlease try again...')

                except sr.RequestError as e:
                    reply = "Sorry, can't process at this time... \nCheck your internet connection...\n\nTerminating the program...\n"
                    engine.say(reply)
                    txt.insertPlainText(reply)
                    engine.runAndWait()
                    sys.exit()

                finally:
                    txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())

        except KeyboardInterrupt:
            pass


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = guiWindow()
    sys.exit(app.exec_())

run()