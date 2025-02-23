import os, time, glob, subprocess, sys, yt_dlp
import customtkinter as ctk
from pyglet import font
from PIL import Image



def download_video(video_url, output_dir, file_name, stream_type="video"):
    ydl_opts = {
        'format': 'bestaudio/best' if stream_type == 'audio' else 'best',
        'outtmpl': f'{output_dir}/{file_name}.%(ext)s', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }] if stream_type == 'audio' else {}  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


def getStaticLogpath(log:str):
    downBasepath = os.getcwd()
    return os.path.join(downBasepath, "logs", log)

def getStaticDownPath():
    downBasepath = os.getcwd()
    return os.path.join(downBasepath, "downloads")

font.add_file(r"fonts\Nunito\Static\Nunito-Bold.ttf")
customFont = "Nunito"

def fileFontsize(text):
    maxLength = 20 
    minFontSize = 11
    maxFontSize = 30

    textLength = len(text)
    if textLength > maxLength:
        fontSize = minFontSize
    else:
        fontSize = maxFontSize - int((textLength / maxLength) * (maxFontSize - minFontSize))
    return fontSize

downfiles = []


def openFile(path):
    if os.path.exists(path):
        try:
            if sys.platform.startswith('win'):
                os.startfile(path)
            elif sys.platform.startswith('linux'):
                subprocess.run(['xdg-open',path])
            elif sys.platform.startswith('darwin'):
                subprocess.run(['open',path])
            else:
                pass
        except Exception as e:
            pass
    else:
        pass

def addFileToFrame(frame,row,col, name, format):
    settedwidth =0
    if format[0]== 1400:
        settedwidth = 190
    elif format[0] == 1200:
        settedwidth = 160
    
    fileToAddFrame = ctk.CTkFrame(frame,width=settedwidth,height=100,corner_radius=5,fg_color=("#313338","#FFE4CE"))
    fileToAddFrame.grid(row=row,column= col, padx=10, pady=10)
    fileToAddFrame.propagate(False)
    nameLbl = ctk.CTkLabel(fileToAddFrame, text=name, font=(customFont,fileFontsize(name),"bold"), text_color=("#ffffff","#313338"))
    nameLbl.pack(padx=10,pady=5)
    playPath= os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\play\customPlay100.png")
    playImg = Image.open(playPath)
    playbutton = ctk.CTkButton(fileToAddFrame,width=90,height=40,text="play",font=(customFont,30),
                               text_color=("#ffffff","#313338"), image=ctk.CTkImage(playImg,playImg,(40,40)), 
                               hover_color=("#dddddd","#ccb6a4"),fg_color="transparent", command=lambda:openFile(os.path.join(getStaticDownPath(),f"{name}.mp4")))
    playbutton.pack(padx=10,pady=5)
    downfiles.append((name,frame.winfo_children()[len(frame.winfo_children())-1]))
    with open(getStaticLogpath("fileLog.txt"),"r") as fileLog:
            lines = fileLog.readlines()
            fileNames= lines[0].split(";")
            fileNames.append(name)
            with open(getStaticLogpath("fileLog.txt"),"w") as fileLog2:
                newNames=""
                for i in range(len(fileNames)-1):
                    newNames = newNames + f"{fileNames[i]};"

                newNames = newNames + fileNames[len(fileNames)-1]
                fileLog2.write(newNames)
    

def setFileToFrame(frame,row,col, name, format):
    settedwidth =0
    if format[0]== 1400:
        settedwidth = 190
    elif format[0] == 1200:
        settedwidth = 160
    
    fileToAddFrame = ctk.CTkFrame(frame,width=settedwidth,height=100,corner_radius=5,fg_color=("#313338","#FFE4CE"))
    fileToAddFrame.grid(row=row,column= col, padx=10, pady=10)
    fileToAddFrame.propagate(False)
    nameLbl = ctk.CTkLabel(fileToAddFrame, text=name, font=(customFont,fileFontsize(name),"bold"), text_color=("#ffffff","#313338"))
    nameLbl.pack(padx=10,pady=5)
    playPath=os.path.join(os.path.dirname(os.path.abspath(__file__)),r"assets\play\customPlay100.png")
    playImg = Image.open(playPath)
    playbutton = ctk.CTkButton(fileToAddFrame,width=90,height=40,text="play",font=(customFont,30),
                               text_color=("#ffffff","#313338"), image=ctk.CTkImage(playImg,playImg,(40,40)), 
                               hover_color=("#dddddd","#ccb6a4"),fg_color="transparent", command=lambda:openFile(os.path.join(getStaticDownPath(),f"{name}.mp4")))
    playbutton.pack(padx=10,pady=5)
    downfiles.append((name,frame.winfo_children()[len(frame.winfo_children())-1]))

    

def filePosition():
    directory = getStaticDownPath()
    pattern = os.path.join(directory, '*.mp4')
    mp4Files = glob.glob(pattern)
    numMp4Files = len(mp4Files)
    return ((numMp4Files-1)//3,(numMp4Files-1)%3)

    
def setFileframe(frame, format):
    fileNames = []
    with open(getStaticLogpath("fileLog.txt"),"r") as fileLog:
        lines = fileLog.readlines()
        Names = lines[0].split(";")
        if len(Names) >=2:
            for i in range(len(Names)):
                if i !=0:
                    fileNames.append(Names[i])
            
            col = 0
            for i in range(len(fileNames)):
                if col>2:
                    col=0
                row = 0 + i//3
                setFileToFrame(frame,row,col,fileNames[i], format)
                col +=1
    


def Download(url,name, path, format, loading, fileFrame, winsize):
    loading.configure(text="WAIT...", text_color="#343638")
    try:
        if format =="video":
            download_video(url, path, name, "video")
            loading.configure(text="DONE!")
            row=filePosition()[0]
            col=filePosition()[1]
            addFileToFrame(fileFrame,row,col,name, winsize)
            setFileframe(fileFrame, winsize)

        elif format=="audio":
            download_video(url, path, name, "audio")
            loading.configure(text="DONE!")
            row=filePosition()[0]
            col=filePosition()[1]
            addFileToFrame(fileFrame,row,col,name, winsize)
            setFileframe(fileFrame, winsize)



    except Exception as e:
        loading.configure(text="[error] check Log", text_color="red")
        current_time_struct = time.localtime()
        current_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
        
        with open(getStaticLogpath("errorLog.txt"),"r") as errorLogD:
            lines = errorLogD.readlines()
            if len(lines) >= 11:
                lines.pop(0)
                with open(getStaticLogpath("errorLog.txt"),"w") as errorLogD1:
                    errorLogD1.write("")
                    with open(getStaticLogpath("errorLog.txt"),"a") as errorLogD2:
                        for line in lines:
                            errorLogD2.write(line)

        with open(getStaticLogpath("errorLog.txt"),"a") as errorLogA:
            errorLogA.write(f"error: {e} | time: {current_time_formatted} \n")

        

def CustomDownload(url,name, path, format, loading):
    loading.configure(text="WAIT...", text_color="#343638")
    try:
        if format =="video":
            download_video(url, path, name, "video")
            loading.configure(text="DONE!")
            openFile(f"{path}\\{name}.mp4")


        elif format=="audio":
            download_video(url, path, name, "audio")
            loading.configure(text="DONE!")
            openFile(f"{path}\\{name}.mp4")



    except Exception as e:
        loading.configure(text="[error] check Log", text_color="red")
        current_time_struct = time.localtime()
        current_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
        
        with open(getStaticLogpath("errorLog.txt"),"r") as errorLogD:
            lines = errorLogD.readlines()
            if len(lines) >= 11:
                lines.pop(0)
                with open(getStaticLogpath("errorLog.txt"),"w") as errorLogD1:
                    errorLogD1.write("")
                    with open(getStaticLogpath("errorLog.txt"),"a") as errorLogD2:
                        for line in lines:
                            errorLogD2.write(line)

        with open(getStaticLogpath("errorLog.txt"),"a") as errorLogA:
            errorLogA.write(f"error: {e} | time: {current_time_formatted} \n")
        


def deleteAll(delproof, frame):
    directory = getStaticDownPath()
    pattern = os.path.join(directory,"*.mp4","*.mp3")
    mp4Files = glob.glob(pattern)
    proofcount = 0
    if len(mp4Files) != 0:
        for file in mp4Files:
            try:
                os.remove(file)
                proofcount +=1
            except Exception as e:
                current_time_struct = time.localtime()
                current_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
                
                with open(getStaticLogpath("errorLog.txt"),"r") as errorLogD:
                    lines = errorLogD.readlines()
                    if len(lines) >= 11:
                        lines.pop(0)
                        with open(getStaticLogpath("errorLog.txt"),"w") as errorLogD1:
                            errorLogD1.write("")
                            with open(getStaticLogpath("errorLog.txt"),"a") as errorLogD2:
                                for line in lines:
                                    errorLogD2.write(line)

                with open(getStaticLogpath("errorLog.txt"),"a") as errorLogA:
                    errorLogA.write(f"error: {e} | time: {current_time_formatted} \n")
                

        if proofcount == len(mp4Files):
            delproof.configure(text="files deleted", text_color="#0064FF")
        else:
            delproof.configure(text="[error] check Log!", text_color="red")
        
        for widget in frame.winfo_children():
            widget.destroy()

        with open(getStaticLogpath("fileLog.txt"),"w") as fileLogD:
            fileLogD.write("[DownloadedFilesDoc:\]")

        

        downfiles.clear()

    else:
        delproof.configure(text="no files existing", text_color="black")


def deleteFile(delproof, name,frame, size):
    directory = os.path.join(getStaticDownPath(),f"{name}.mp4")
    if os.path.exists(directory) != True:
        directory = os.path.join(getStaticDownPath(),f"{name}.mp3")
        
    if os.path.exists(directory):
        try:
            os.remove(directory)
            delproof.configure(text="file deleted", text_color="#0064FF")

            
            with open(getStaticLogpath("fileLog.txt"),"r") as fileLog:
                lines = fileLog.readlines()
                fileNames= lines[0].split(";")
                fileNames = list(fileNames)
                fileNames.remove(name)
                with open(getStaticLogpath("fileLog.txt"),"w") as fileLog2:
                    newNames=""
                    for i in range(len(fileNames)-1):
                        newNames = newNames + f"{fileNames[i]};"

                    newNames = newNames + fileNames[len(fileNames)-1]
                    fileLog2.write(newNames)
            
            for widget in frame.winfo_children():
                widget.destroy()

            downfiles.clear()
            setFileframe(frame,size)

        
        except Exception as e:
            current_time_struct = time.localtime()
            current_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time_struct)
                
            with open(getStaticLogpath("errorLog.txt"),"r") as errorLogD:
                lines = errorLogD.readlines()
                if len(lines) >= 11:
                    lines.pop(0)
                    with open(getStaticLogpath("errorLog.txt"),"w") as errorLogD1:
                        errorLogD1.write("")
                        with open(getStaticLogpath("errorLog.txt"),"a") as errorLogD2:
                            for line in lines:
                                errorLogD2.write(line)

            with open(getStaticLogpath("errorLog.txt"),"a") as errorLogA:
                errorLogA.write(f"error: {e} | time: {current_time_formatted} \n")    
            delproof.configure(text="[error] check Log!", text_color="red")
    else:
         delproof.configure(text="file does'nt exists", text_color="black")
