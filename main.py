import customtkinter as ctk
from menu import *
from fileHandler import setFileframe,downfiles, refreshFilelog
import os



def Setup(root, name: str, resizable):
    #Basic
    refreshFilelog()
    windowScaleX,windowScaleY=SettingsReadResolution()
    root.geometry(f"{windowScaleX}x{windowScaleY}")
    SettingsReadMode()
    
    root.title(name)
    try:
        root.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\logo\logoIco.ico"))
    except:
        pass

    root.resizable(resizable,resizable)
    if resizable == False:
        root.minsize(windowScaleX,windowScaleY)
        root.maxsize(windowScaleX,windowScaleY)
    

def restart(root):
    downfiles.clear()
    root.destroy()
    main()
    

def main():
    root = ctk.CTk()
    windowScaleXs,windowScaleYs = SettingsReadResolution()
    windowSize = (windowScaleXs,windowScaleYs)
    Setup(root, "Downtube", False)
    root.grid_rowconfigure(0, minsize=windowSize[1])


    fileFrame = ctk.CTkScrollableFrame(root)
    fileFrameStylize(fileFrame, windowSize)
    fileFrame.grid(row=0,column=3,padx=10, sticky="nsew")
    setFileframe(fileFrame, windowSize)

    menuFrame = ctk.CTkFrame(root)
    menuFrameStylize(menuFrame, windowSize)
    menuFrame.grid(row=0, column=0, sticky="nsew", pady=10)

    placeHolder = ctk.CTkFrame(root)
    placeHolderStylize(placeHolder,windowSize)
    placeHolder.grid(row=0, column=1, sticky="nsew", pady=10, padx= 10)

    leavePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\leave\leave100.png")
    leaveButton = ctk.CTkButton(menuFrame, hover_color="#d5aba6", command=leave)
    menuButtonStylize(leaveButton,leavePath)
    leaveButton.pack(side="bottom", anchor="sw",padx=2, pady=10)

    restartPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\restart\restart100.png")
    restartButton = ctk.CTkButton(menuFrame, hover_color="#d5aba6", command= lambda: restart(root))
    menuButtonStylize(restartButton,restartPath)
    restartButton.pack(side="bottom", anchor="sw",padx=2, pady=10)

    addPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\add\add100.png")
    addButton = ctk.CTkButton(menuFrame, hover_color="#d7f8cf", command= lambda: add(root, windowSize, placeHolder, fileFrame))
    menuButtonStylize(addButton,addPath)
    addButton.pack(padx=2, pady=10)

    settingsPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\settings\settings100.png")
    settingsButton = ctk.CTkButton(menuFrame, hover_color="#DDEAFF", command= lambda: settings(root, windowSize, placeHolder, fileFrame))
    menuButtonStylize(settingsButton,settingsPath)
    settingsButton.pack(padx=2, pady=10)

    logoPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\logo\logo100.png")
    logoButton = ctk.CTkButton(menuFrame, hover_color="#E4D0FF", command= lambda: logo(root, windowSize, placeHolder))
    menuButtonStylize(logoButton,logoPath)
    logoButton.pack(padx=2, pady=10)


    root.mainloop()

if __name__ == "__main__":
    main()