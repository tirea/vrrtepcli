echo off
cls
title Build vCLI Package
cd %~dp0
if "%1" == "" ( 
	set target=%cd%\vcli_win
) else (
	set target=%1
)

if "%2" == "" ( 
	set target2=..\vcli_win_standalone
) else (
	set target2=%2
)

echo BUILD SCRIPT FOR VCLI 1.9
echo Written by SacredBanshee
echo.
echo BUILDVC: Building package...
copy /Y compile.py vcli_win\compile.py
cd %target%
python compile.py py2exe
echo.
echo.
echo BUILDSA: Assembling package...
copy /Y "%target%\dist\*.*" "%target2%"
del "%target2%\demoncli.exe"
ren "%target2%\vrrtepcli.exe" demoncli.exe
del "%target%\compile.py"
rd /s /q "%target%\dist"
rd /s /q "%target%\build"
del "%target%\*.pyc"
if exist "%~dp0vcli_win\user_settings.bat" del "%~dp0vcli_win\user_settings.bat"
if exist "%~dp0vcli_win_standalone\user_settings.bat" del "%~dp0vcli_win_standalone\user_settings.bat"
echo Finished. Press a key to exit.
pause >NUL