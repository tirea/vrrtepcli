echo off
echo Uninstaller for VrrtepCLI (Windows Version)
cd %~dp0

pathtool /a
if errorlevel 1 goto root
:user

pathtool /u
cd "%userprofile%"
if exist "%userprofile%\.vrrtepcli" (
	rd /s /q "%userprofile%\.vrrtepcli"
	echo Deleted folder and contents: %userprofile%\.vrrtepcli
)
echo Finished.
goto end

:root
if not exist "%allusersprofile%\.vrrtepcli" goto user
if not exist "%userprofile%\.vrrtepcli" goto nouser

echo.
echo Which copy of vrrtepCLI do you want to remove?
echo 1) System-wide copy
echo 2) Current user's copy
echo.
set /P ASKUSER=[1/2]:
if "%ASKUSER%"=="2" goto user
if "%ASKUSER%"=="" goto user

:nouser
pathtool /ua
cd "%allusersprofile%"
if exist "%allusersprofile%\.vrrtepcli" (
	rd /s /q "%allusersprofile%\.vrrtepcli"
	echo Deleted folder and contents: %allusersprofile%\.vrrtepcli
)
echo Finished.
goto end

:end
pause