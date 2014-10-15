echo off
echo Installer for VrrtepCLI (Windows Version)
echo.
pathtool /a
if errorlevel 1 goto root
:user
cd %~dp0
if not exist "%userprofile%\.vrrtepcli" (
	md "%userprofile%\.vrrtepcli"
	echo Created folder %userprofile%\.vrrtepcli
)
copy /Y *.* "%userprofile%\.vrrtepcli"

echo.
REM Update the path
pathtool /i
if errorlevel 255 (
	echo.
	echo Path updating failed. You will be required to
	echo CD to %userprofile%\.vrrtepcli to use this program.
	echo.
)
cd "%userprofile%\.vrrtepcli"
:finish
echo.
echo Finished. It's advised you close this command prompt 
echo and open a new one so PATH changes can take effect.
echo.

goto end


:root
set /p ASKUSER=Do you want to install vCLI for all users (Y/N)? [Default: N]
if "%ASKUSER%"=="" GOTO user
if "%ASKUSER%"=="N" GOTO user
if "%ASKUSER%"=="n" GOTO user
echo Installing for all users
echo.
if not exist "%allusersprofile%\Application.vrrtepcli" (
	md "%allusersprofile%\.vrrtepcli"
	echo Created folder %allusersprofile%\.vrrtepcli
)
copy /Y *.* "%allusersprofile%\.vrrtepcli"

echo.
REM Update the path
pathtool /ia
if errorlevel 255 (
	echo.
	echo Path updating failed. You will be required to
	echo CD to %allusersprofile%\.vrrtepcli to use this program.
	echo.
)
cd "%allusersprofile%\.vrrtepcli"
goto finish
:end
pause
