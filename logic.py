from sys import exit
import customtkinter as ctk
import os, threading, re
from PIL import Image
from pyglet import font
from style import *
from download import *
from otherTasks import *


font.add_file(r"fonts\Nunito\Static\Nunito-Bold.ttf")
customFont = "Nunito"

def NameSyntax(inputString):
    cleanedString = re.sub(r'[^A-Za-z0-9 ()]', '', inputString)
    return cleanedString

def leave():
    exit()

def add(root, size: tuple, place, fileFrame):
    addFrame = ctk.CTkFrame(root)
    addFrameStylize(addFrame,size)
    addFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    addFrame.propagate(False)
    place.grid_remove()

    HeadlinepathImg = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\logo\logoG100.png"))
    HeadlineLabel = ctk.CTkLabel(addFrame, text="Add          File",font=(customFont,28,"bold"),text_color="#343638",image=ctk.CTkImage(HeadlinepathImg,HeadlinepathImg,(60,60)))
    HeadlineLabel.pack(padx=10,pady=25)
    
    def on_focus_out(event):
        addFrame.focus()

    loadingLabel = ctk.CTkLabel(addFrame, text="", font=("Arial Black",30), fg_color="transparent", text_color="#343638")
    loadingLabel.pack(padx=10, pady=10, side="bottom")
    
    def proofDownload():
        vidurl = urlEntry.get()
        vidname= nameEntry.get()
        viddir = dirEntry.get()
        vidformat = formatCombo.get()
        if vidurl and vidname and vidformat and len(vidname)<21 and vidname == NameSyntax(vidname):
            if not viddir:
                viddir = getStaticDownPath()
                addingFile = os.path.join(viddir,f"{vidname}.mp4")
                if os.path.exists(addingFile):
                    loadingLabel.configure(text="file already exists", text_color="red")
                else:
                    thread = threading.Thread(target=Download, args=(vidurl, vidname, viddir, vidformat, loadingLabel, fileFrame,size))
                    thread.start()
                

            else:
                addingFile = os.path.join(viddir,f"{vidname}.mp4")
                if os.path.exists(addingFile):
                    loadingLabel.configure(text="file already exists", text_color="red")
                else:
                    thread = threading.Thread(target=Download, args=(vidurl, vidname, viddir, vidformat, loadingLabel, fileFrame,size))
                    thread.start()
        else:
            loadingLabel.configure(text="Syntax Error",text_color="red")

    
    urlEntry = ctk.CTkEntry(addFrame, font=(customFont,20))
    urlEntryStylize(urlEntry)
    urlEntry.pack(padx=10,pady=40)
    urlEntry.bind('<Return>',on_focus_out)

    preferenceFrame = ctk.CTkFrame(addFrame)
    preferenceFrameStylize(preferenceFrame)
    preferenceFrame.pack(pady=20,padx=10,expand=True)

    nameLabel = ctk.CTkLabel(preferenceFrame, text="Save as: ",text_color="#343638", font=(customFont,20))
    nameLabel.grid(row=0,column=0,padx=10,pady=20)

    nameEntry = ctk.CTkEntry(preferenceFrame, font=(customFont,20))
    nameEntryStylize(nameEntry)
    nameEntry.grid(row=0,column=1,padx=10,pady=20)
    nameEntry.bind('<Return>',on_focus_out)

    dirLabel = ctk.CTkLabel(preferenceFrame, text="Savingpath: ",text_color="#343638", font=(customFont,20))
    dirLabel.grid(row=1,column=0,padx=10,pady=20)

    dirEntry = ctk.CTkEntry(preferenceFrame, font=(customFont,20))
    nameEntryStylize(dirEntry)
    dirEntry.grid(row=1,column=1,padx=10,pady=20)
    dirEntry.configure(placeholder_text="default")
    dirEntry.configure(state="readonly")
    dirEntry.bind('<Return>',on_focus_out)

    formatLabel = ctk.CTkLabel(preferenceFrame, text="Format: ",text_color="#343638", font=(customFont,20))
    formatLabel.grid(row=2,column=0,padx=10,pady=20)

    formatCombo = ctk.CTkComboBox(preferenceFrame, values=["audio","video"], width=130, height=50, state="readonly")
    formatComboStylize(formatCombo)
    formatCombo.grid(row=2,column=1,padx=10,pady=20)
    formatCombo.set("audio")

    downLabel = ctk.CTkLabel(preferenceFrame, text="ready? ",text_color="#343638", font=(customFont,20))
    downLabel.grid(row=3,column=0,padx=10,pady=20)

    downPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\download\download100.png")
    downImg = Image.open(downPath)
    downImage = ctk.CTkImage(downImg,downImg,(80,80))
    downloadBtn = ctk.CTkButton(preferenceFrame, width=100, height=100, corner_radius=15, hover_color="#83D76F",
                                 image=downImage, text=None, fg_color="transparent", command=proofDownload)
    downloadBtn.grid(row=3, column=1, padx=20,pady=20)


def settings(root, size: tuple, place, fileFrame):
    settingsFrame = ctk.CTkFrame(root)
    settingsFrameStylize(settingsFrame,size)
    settingsFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    settingsFrame.propagate(False)

    place.grid_remove()

    tabView = ctk.CTkTabview(settingsFrame,corner_radius=15)
    tabViewStylize(tabView)
    tabView.pack(padx=20,pady=20,expand=True)
    tabView.add("general")
    tabView.add("help")

    def on_focus_out(event):
            settingsFrame.focus()

    def setDarkmode(state):
        if state == True:
            ctk.set_appearance_mode("dark")
            with open(getStaticLogpath("settingsLog.txt"),"r") as settingsLog:
                lines = settingsLog.readlines()
                settings= lines[0].split(";")
                settings[0]="Darkmode=True"
                with open(getStaticLogpath("settingsLog.txt"),"w") as settingsLog2:
                    newSettings=""
                    for i in range(len(settings)-1):
                        newSettings = newSettings + f"{settings[i]};"

                    newSettings = newSettings + settings[len(settings)-1]
                    settingsLog2.write(newSettings)
                   

        elif state == False:
            ctk.set_appearance_mode("light")
            with open(getStaticLogpath("settingsLog.txt"),"r") as settingsLog3:
                lines = settingsLog3.readlines()
                settings= lines[0].split(";")
                settings[0]="Darkmode=False"
                with open(getStaticLogpath("settingsLog.txt"),"w") as settingsLog4:
                    newSettings=""
                    for i in range(len(settings)-1):
                        newSettings = newSettings + f"{settings[i]};"

                    newSettings = newSettings + settings[len(settings)-1]
                    settingsLog4.write(newSettings)
            

    def setWinResolution(size):
            with open(getStaticLogpath("settingsLog.txt"),"r") as settingsLogRes:
                lines = settingsLogRes.readlines()
                settings= lines[0].split(";")
                resSetting= f"Resolution={size}"
                settings[1] = resSetting
                with open(getStaticLogpath("settingsLog.txt"),"w") as settingsLogRes2:
                    newSettings=""
                    for i in range(len(settings)-1):
                        newSettings = newSettings + f"{settings[i]};"

                    newSettings = newSettings + settings[len(settings)-1]
                    settingsLogRes2.write(newSettings)
            


    
    appereanceLabel = ctk.CTkLabel(tabView.tab("general"), text="Appereance:", font=(customFont,28,"bold"),text_color="#343638")
    appereanceLabel.grid(row=0, column=0,pady=25,padx=5)

    winSizeLabel = ctk.CTkLabel(tabView.tab("general"), text="Windowsize:", font=(customFont,22),text_color="#343638")
    winSizeLabel.grid(row=1, column=0,pady=20,padx=5)

    winSizeCombo = ctk.CTkComboBox(tabView.tab("general"), values=["1200x700","1400x700","1200x900","1400x900"], state="readonly")
    winSizeCombo.grid(row=1, column=1,pady=20,padx=15)

    winSizeCheck = ctk.CTkButton(tabView.tab("general"), command=lambda: setWinResolution(winSizeCombo.get()),hover_color="#d7f8cf")
    winSizeCheckImgpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\check\check100.png")
    settingsButtonStylize(winSizeCheck, winSizeCheckImgpath)
    winSizeCheck.grid(row=1, column=2,pady=20,padx=10)

    modeLabel = ctk.CTkLabel(tabView.tab("general"), text="Darkmode:", font=(customFont,22),text_color="#343638")
    modeLabel.grid(row=3, column=0,pady=20,padx=5)
    
    modeSwitch = ctk.CTkSwitch(tabView.tab("general"),command=lambda: setDarkmode(modeSwitch.get()))
    modeSwitchStylize(modeSwitch)
    modeSwitch.grid(row=3, column=1,pady=20,padx=5)

    filesLabel = ctk.CTkLabel(tabView.tab("general"), text="Files:", font=(customFont,28,"bold"),text_color="#343638")
    filesLabel.grid(row=4, column=0,pady=25,padx=5)

    delFileLabel = ctk.CTkLabel(tabView.tab("general"), text="delete file:", font=(customFont,22),text_color="#343638")
    delFileLabel.grid(row=5, column=0,pady=20,padx=5)

    delEntry = ctk.CTkEntry(tabView.tab("general"), font=(customFont,16))
    delEntryStylize(delEntry)
    delEntry.grid(row=5,column=1,padx=5,pady=20)
    delEntry.bind('<Return>',on_focus_out)

    delFPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\delete\delete100.png")
    delFButton = ctk.CTkButton(tabView.tab("general"), hover_color="#d5aba6", command=lambda: deleteFile(delproof,delEntry.get(),fileFrame,size))
    settingsButtonStylize(delFButton,delFPath)
    delFButton.grid(row=5,column=2,padx=5,pady=20)

    delAllLabel = ctk.CTkLabel(tabView.tab("general"), text="delete all:", font=(customFont,22),text_color="#343638")
    delAllLabel.grid(row=6, column=0,pady=20,padx=5)

    delAPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\delete\delete100.png")
    delAButton = ctk.CTkButton(tabView.tab("general"), hover_color="#d5aba6", command=lambda:deleteAll(delproof,fileFrame))
    settingsButtonStylize(delAButton,delAPath)
    delAButton.grid(row=6,column=1,padx=5,pady=20)

    delproof = ctk.CTkLabel(tabView.tab("general"), text="", font=(customFont,16),text_color="#0064FF")
    delproof.grid(row=7, column=1,pady=0,padx=5)

    Hint = ctk.CTkLabel(settingsFrame, text="after changing the Windowsize, you may have to restart the app", font=(customFont,16),text_color="#0064FF")
    Hint.pack(pady=10,padx=5,side=ctk.BOTTOM)

    LogsLabel = ctk.CTkLabel(tabView.tab("help"), text="Logs:", font=(customFont,28,"bold"),text_color="#343638")
    LogsLabel.grid(row=0, column=0,pady=10,padx=5)

    ErrorLogLabel = ctk.CTkLabel(tabView.tab("help"), text="Errorlog:", font=(customFont,22),text_color="#343638")
    ErrorLogLabel.grid(row=1, column=0,pady=10,padx=5)
    
    openLabel = ctk.CTkLabel(tabView.tab("help"), text="click here to open", font=(customFont,16),text_color="#0064FF").grid(row=1, column=1,pady=10,padx=5)
    ErrorLogPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\errorLog\error100.png")
    ErrorlogButton = ctk.CTkButton(tabView.tab("help"), hover_color="#E7CF88", command=openErrorLog)
    settingsButtonStylize(ErrorlogButton,ErrorLogPath)
    ErrorlogButton.grid(row=1,column=2,padx=5,pady=10)

    DocsLabel = ctk.CTkLabel(tabView.tab("help"), text="Documentation:", font=(customFont,28,"bold"),text_color="#343638")
    DocsLabel.grid(row=2, column=0,pady=10,padx=5)

    UsingLabel = ctk.CTkLabel(tabView.tab("help"), text="How to use:", font=(customFont,22),text_color="#343638")
    UsingLabel.grid(row=3, column=0,pady=10,padx=5)

    openLabel1 = ctk.CTkLabel(tabView.tab("help"), text="click here to open", font=(customFont,16),text_color="#0064FF").grid(row=3, column=1,pady=10,padx=5)
    UseDownPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\open\open100.png")
    UseButton = ctk.CTkButton(tabView.tab("help"), hover_color="#C6B4E2", command=openUsage)
    settingsButtonStylize(UseButton,UseDownPath)
    UseButton.grid(row=3,column=2,padx=5,pady=10)

    AGBLabel = ctk.CTkLabel(tabView.tab("help"), text="AGBs:", font=(customFont,22),text_color="#343638")
    AGBLabel.grid(row=4, column=0,pady=10,padx=5)

    openLabel1 = ctk.CTkLabel(tabView.tab("help"), text="click here to open", font=(customFont,16),text_color="#0064FF").grid(row=4, column=1,pady=10,padx=5)
    AGBPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\open\open100.png")
    AGBButton = ctk.CTkButton(tabView.tab("help"), hover_color="#C6B4E2", command=openAGB)
    settingsButtonStylize(AGBButton,AGBPath)
    AGBButton.grid(row=4,column=2,padx=5,pady=10)

    supportLabel = ctk.CTkLabel(tabView.tab("help"), text="Support:", font=(customFont,28,"bold"),text_color="#343638")
    supportLabel.grid(row=5, column=0,pady=10,padx=5)

    joinDiscLabel = ctk.CTkLabel(tabView.tab("help"), text="join our Discord", font=(customFont,18),text_color="#343638")
    joinDiscLabel.grid(row=6, column=0,pady=10,padx=5)

    DiscPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\links\discord100.png")
    DiscButton = ctk.CTkButton(tabView.tab("help"), hover_color="#C6D7E5", command=joinDiscord)
    settingsButtonStylize(DiscButton,DiscPath)
    DiscButton.grid(row=6,column=2,padx=5,pady=10)

    GitLabel = ctk.CTkLabel(tabView.tab("help"), text="GitHub docs", font=(customFont,18),text_color="#343638")
    GitLabel.grid(row=7, column=0,pady=10,padx=5)

    GitPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\links\github100.png")
    GitButton = ctk.CTkButton(tabView.tab("help"), hover_color="#C6D7E5", command=gitRepo)
    settingsButtonStylize(GitButton,GitPath)
    GitButton.grid(row=7,column=2,padx=5,pady=10)

    SettingsSet(winSizeCombo,modeSwitch)


def SettingsSet(winCombo,modeSwitch):
    logPath = getStaticLogpath("settingsLog.txt")
    state = modeSwitch.get()
    with open(logPath,"r") as log:
        lines = log.readlines()
        settings= lines[0].split(";")
        if settings[0] == "Darkmode=True" and state == False:
            modeSwitch.select(True)
        elif settings[0] == "Darkmode=False" and state == True: 
            modeSwitch.select(False)
        if settings[1] == "Resolution=1200x700":
            winCombo.set("1200x700")
        elif settings[1] == "Resolution=1400x700":
            winCombo.set("1400x700")
        elif settings[1] == "Resolution=1200x900":
            winCombo.set("1200x900")
        elif settings[1] == "Resolution=1400x900":
            winCombo.set("1400x900")


def SettingsReadMode():
    logPath = getStaticLogpath("settingsLog.txt")
    with open(logPath,"r") as log:
        lines = log.readlines()
        settings= lines[0].split(";")
        if settings[0] == "Darkmode=True":
            ctk.set_appearance_mode("dark")
        else: 
            ctk.set_appearance_mode("light")


def SettingsReadResolution():
    logPath = getStaticLogpath("settingsLog.txt")
    with open(logPath,"r") as log:
        lines = log.readlines()
        settings= lines[0].split(";")
        
        resSettings = settings[1].split("=")
    windowSize = resSettings[1].split("x")
    return int(windowSize[0]), int(windowSize[1])
        


def logo(root, size: tuple, place):
    logoFrame = ctk.CTkFrame(root)
    logoFrameStylize(logoFrame,size)
    logoFrame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    logoFrame.propagate(False)
    place.grid_remove()

    def on_focus_out(event):
        logoFrame.focus()

    loadingLabel = ctk.CTkLabel(logoFrame, text="", font=("Arial Black",30), fg_color="transparent", text_color="#343638")
    loadingLabel.pack(padx=10, pady=10, side="bottom")

    def proofDownload():
        vidurl = urlEntry.get()
        vidname= nameEntry.get()
        viddir = dirEntry.get()
        vidformat = formatCombo.get()
        if vidurl and vidname and vidformat and viddir:
            addingFile = os.path.join(viddir,f"{vidname}.mp4")
            if os.path.exists(addingFile):
                loadingLabel.configure(text="file already exists", text_color="red")

            if not os.path.exists(viddir):
                loadingLabel.configure(text="directory doesnt exists", text_color="red")

            else:
                thread = threading.Thread(target=CustomDownload, args=(vidurl, vidname, viddir, vidformat, loadingLabel))
                thread.start()       
        else:
            loadingLabel.configure(text="Syntaxerror",text_color="red")


    LogopathImg = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\logo\logo100.png"))
    LogoLabel = ctk.CTkLabel(logoFrame, text="Customdownload",font=(customFont,28,"bold"),text_color="#343638",image=ctk.CTkImage(LogopathImg,LogopathImg,(60,60)))
    LogoLabel.pack(padx=10,pady=25)


    urlEntry = ctk.CTkEntry(logoFrame, font=(customFont,20))
    urlEntryStylize(urlEntry)
    urlEntry.pack(pady=10,padx=10)
    urlEntry.bind('<Return>',on_focus_out)

    customDownloadFrame = ctk.CTkFrame(logoFrame)
    customDownloadFrameStylize(customDownloadFrame)
    customDownloadFrame.pack(padx = 20, pady=20, expand=False)


    nameEntry = ctk.CTkEntry(customDownloadFrame, font=(customFont,20))
    nameEntryStylize(nameEntry)
    nameEntry.configure(placeholder_text="save as ...")
    nameEntry.grid(row=0,column=0,padx=10,pady=15, sticky = "w")
    nameEntry.bind('<Return>',on_focus_out)


    dirEntry = ctk.CTkEntry(customDownloadFrame, font=(customFont,20))
    nameEntryStylize(dirEntry)
    dirEntry.configure(placeholder_text= "enter savingpath ...")
    dirEntry.grid(row=1,column=0,padx=10,pady=20, sticky = "w")
    dirEntry.bind('<Return>',on_focus_out)

    formatCombo = ctk.CTkComboBox(customDownloadFrame, values=["audio","video"], width=130, height=50, state="readonly")
    formatComboStylize(formatCombo)
    formatCombo.grid(row=2,column=0,padx=10,pady=15)
    formatCombo.set("audio")


    downPath =  os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\download\download100.png")
    downImg = Image.open(downPath)
    downImage = ctk.CTkImage(downImg,downImg,(80,80))
    downloadBtn = ctk.CTkButton(customDownloadFrame, width=100, height=100, corner_radius=15, hover_color="#a7afcc",
                                 image=downImage, text=None, fg_color="transparent", command=proofDownload)
    downloadBtn.grid(row=1, column=1, padx=20,pady=10)
    
    enjoyFilesLabel = ctk.CTkLabel(logoFrame, text="Enjoy your Files ",font=(customFont,24,"bold"),text_color="#343638")
    enjoyFilesLabel.pack(padx=10,pady=15)

    customSettingsFrame = ctk.CTkFrame(logoFrame)
    customDownloadFrameStylize(customSettingsFrame)
    customSettingsFrame.pack(padx = 20, pady=10, expand=False)

    PlaylistPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\play\customPlay100.png")
    PlaylistButton = ctk.CTkButton(customSettingsFrame, hover_color="#a7afcc", command=lambda:playPlaylist("normal"))
    settingsButtonStylize(PlaylistButton,PlaylistPath)
    PlaylistButton.configure(text="In Order", font=(customFont,18),text_color="#343638")
    PlaylistButton.grid(row=0,column=0,padx=10,pady=10)

    ShuffleModePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\custom\shuffle100.png")
    ShuffleModeButton = ctk.CTkButton(customSettingsFrame, hover_color="#a7afcc", command=lambda:playPlaylist("shuffle"))
    settingsButtonStylize(ShuffleModeButton,ShuffleModePath)
    ShuffleModeButton.configure(text="Shufflemode", font=(customFont,18),text_color="#343638")
    ShuffleModeButton.grid(row=0,column=1,padx=10,pady=10)

