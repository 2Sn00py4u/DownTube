@echo off
REM Batch script to create a desktop shortcut for the executable

REM Set variables
set "EXECUTABLE_NAME=main.exe"
set "SHORTCUT_NAME=DownTube"
set "DESCRIPTION=DownTube_byFrog"
set "ICON_PATH=%~dp0assets\logo\logoIco.ico"

REM Get the path to the Desktop
set "DESKTOP_PATH=%USERPROFILE%\Desktop"

REM Create the VBS script to create the shortcut
set "VBS_SCRIPT=%TEMP%\create_shortcut.vbs"
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%VBS_SCRIPT%"
echo sLinkFile = "%DESKTOP_PATH%\%SHORTCUT_NAME%.lnk" >> "%VBS_SCRIPT%"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%VBS_SCRIPT%"
echo oLink.TargetPath = "%~dp0%EXECUTABLE_NAME%" >> "%VBS_SCRIPT%"
echo oLink.WorkingDirectory = "%~dp0" >> "%VBS_SCRIPT%"
echo oLink.Description = "%DESCRIPTION%" >> "%VBS_SCRIPT%"
if exist "%ICON_PATH%" (
    echo oLink.IconLocation = "%ICON_PATH%" >> "%VBS_SCRIPT%"
)
echo oLink.Save >> "%VBS_SCRIPT%"

REM Run the VBS script to create the shortcut
cscript //nologo "%VBS_SCRIPT%"

REM Clean up the VBS script
del "%VBS_SCRIPT%"

echo Shortcut created on the desktop.
pause
