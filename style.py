from PIL import Image
import customtkinter as ctk


def fileFrameStylize(fileFrame, windowSize):
    fileFrameStyle = {
        "width": windowSize[0]/2-50,
        "height": windowSize[1]-50,
        "fg_color": ("#FFE4CE","#313338"),
        "bg_color": "transparent",
        "corner_radius": 20

    }
    fileFrame.configure(**fileFrameStyle)

def placeHolderStylize(place, size):
    placeHolderStyle = {
        "width": size[0]/2-100,
        "height": size[1]-50,
        "fg_color": "transparent",
        "corner_radius": 20
    }
    place.configure(**placeHolderStyle)

def menuFrameStylize(menuFrame, windowSize):
    menuFrameStyle = {
        "width": 70,
        "height": windowSize[1],
        "fg_color": ("#FFE4CE","#313338"),
        "bg_color": "transparent",
        "corner_radius": 20
    }
    menuFrame.configure(**menuFrameStyle)

def menuButtonStylize(button, imgPath):
    icon = Image.open(imgPath)
    buttonStyle = {
        "image": ctk.CTkImage(icon,icon,(40,40)),
        "width": 60,
        "height": 60,
        "fg_color": "transparent",
        "text":None,
        "corner_radius":15
     
    }
    button.configure(**buttonStyle)

def addFrameStylize(frame,size):
    addFrameStyle = {
        "width": size[0]/2-100,
        "height": size[1]-50,
        "fg_color": "#d7f8cf",
        "corner_radius": 20
    }
    frame.configure(**addFrameStyle)

def settingsFrameStylize(frame,size):
    settingsFrameStyle = {
        "width": size[0]/2-100,
        "height": size[1]-50,
        "fg_color": "#DDEAFF",
        "corner_radius": 20
    }
    frame.configure(**settingsFrameStyle)

def logoFrameStylize(frame,size):
    logoFrameStyle = {
        "width": size[0]/2-100,
        "height": size[1]-50,
        "fg_color": "#E4D0FF",
        "corner_radius": 20
    }
    frame.configure(**logoFrameStyle)

def urlEntryStylize(entry):
    entryStyle ={
        "width": 400,
        "height": 30,
        "placeholder_text": "Enter url...",
        "text_color":("#343638","#eeeeee")

    }
    entry.configure(**entryStyle)

def preferenceFrameStylize(preferenceFrame):
    preferenceFrameStyle = {
        "fg_color":"#aac4a4",
        "width":400,
        "height":500,
        "corner_radius":20,
        "border_width":2,
        "border_color":"#343638"
    }
    preferenceFrame.configure(**preferenceFrameStyle)

def nameEntryStylize(entry):
    entryStyle ={
        "width": 200,
        "height": 20,
        "placeholder_text": "Enter here...",
        "text_color":("#343638","#eeeeee")

    }
    entry.configure(**entryStyle)

def formatComboStylize(box):
    formatComboStyle = {
        "width":130,
        "height":50,
        "dropdown_text_color":("#343638","#ffffff"),
        "dropdown_hover_color":("#ffffff" ,"#565b5e")
    }
    box.configure(**formatComboStyle)

def tabViewStylize(tabView):
    tabViewStyle = {
        "width":400,
        "height":600,
        "fg_color":"#b0bbcc",
        "border_color":"#343638",
        "border_width":4,
        "text_color":"#ffffff",
        "segmented_button_fg_color":"#343638",
        "segmented_button_unselected_color": "#343638",
        "segmented_button_unselected_hover_color":"#9bc1ff",
        "segmented_button_selected_color":"#607599",
        "segmented_button_selected_hover_color": "#607599"
    }
    tabView.configure(**tabViewStyle)

def modeSwitchStylize(switch):
    modeSwitchStyle ={
        "text":"",
        "width": 40,
        "height":20,
        "border_color":"#343638",
        "border_width":2,
        "button_color":"#343638",
        "progress_color":"#368cd6"
    }
    switch.configure(**modeSwitchStyle)

def winsizeCheckStylize(check, imgpath):
    img = Image.open(imgpath)
    checkStyle = {
        "image": ctk.CTkImage(img,img,(30,30)),
        "width": 30,
        "height": 30,
        "fg_color": "#d7f8cf",
        "hover_color":"#aac4a4",
        "text":None,
        "corner_radius":13,
        "border_color":"#343638",
        "border_width":2
    }
    check.configure(**checkStyle)

def delEntryStylize(entry):
    entryStyle ={
        "width": 150,
        "height": 18,
        "placeholder_text": "Enter name...",
        "text_color":("#343638","#eeeeee")
    }
    entry.configure(**entryStyle)

def settingsButtonStylize(button, imgPath):
    icon = Image.open(imgPath)
    buttonStyle = {
        "image": ctk.CTkImage(icon,icon,(40,40)),
        "width": 50,
        "height": 50,
        "fg_color": "transparent",
        "text":None,
        "corner_radius":10 
    }
    button.configure(**buttonStyle)

def customDownloadFrameStylize(customdownFrame):
    customDownFrameStyle = {
        "fg_color":"#d1dbff",
        "width":400,
        "height":500,
        "corner_radius":20,
        "border_width":2,
        "border_color":"#343638"
    }
    customdownFrame.configure(**customDownFrameStyle)