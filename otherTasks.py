import subprocess,os,glob,random,webbrowser,sys


def getBasepath():
    return os.getcwd()
    
def getDownPath():
    downBasepath = os.getcwd()
    return os.path.join(downBasepath, "downloads")

def playPlaylist(mode:str):
    downfilesDir = getDownPath()
    pattern = os.path.join(downfilesDir,"*.mp4","*.mp3")
    mediaFiles = glob.glob(pattern)

    if mode == "shuffle":
        random.shuffle(mediaFiles)
    elif mode == "normal":
        mediaFiles.sort(key=os.path.getctime)

    
    with open(os.path.join(getBasepath(),"playlist.m3u"), "w") as playlistlog:
        playlistlog.write("#EXTM3U\n")
        for file in mediaFiles:
            playlistlog.write(f"{file}\n")

    if sys.platform.startswith('win'):
        os.startfile(os.path.join(getBasepath(),"playlist.m3u"))
    elif sys.platform.startswith('linux'):
        subprocess.run(['xdg-open', os.path.join(getBasepath(),"playlist.m3u")])
    elif sys.platform.startswith('darwin'):
        subprocess.run(['open', os.path.join(getBasepath(),"playlist.m3u")])
    else:
        pass

def openErrorLog():
    try:
        errorlogpath = os.path.join(getBasepath(),r"logs\errorLog.txt")
        subprocess.run(["explorer",errorlogpath])
    except:
        pass

def joinDiscord():
    try:
        url = "https://discord.gg/SH5esJ25TA"
        webbrowser.open(url)

    except Exception as e:
        pass

def gitRepo():
    try:
        url = "https://github.com/dudeLikesFrogs/DownTube"
        webbrowser.open(url)

    except Exception as e:
        pass

def openAGB():
    try:
        url = "https://github.com/dudeLikesFrogs/DownTube/blob/main/AGBs.pdf"
        webbrowser.open(url)
    except Exception as e:
        pass

def openUsage():
    try:
        url = "https://github.com/dudeLikesFrogs/DownTube/blob/main/DocUsage.pdf"
        webbrowser.open(url)
    except Exception as e:
        pass

    