
echo off
REM    Vrrtep CLI is free software: you can redistribute it and/or modify
REM    it under the terms of the GNU General Public Licence as published by
REM    the Free Software Foundation, either version 3 of the Licence, or
REM    (at your option) any later version.
REM
REM    Vrrtep CLI is distributed in the hope that it will be useful,
REM    but WITHOUT ANY WARRANTY; without even the implied warranty of
REM    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM    GNU General Public License for more details.
REM
REM    You should have received a copy of the GNU General Public License
REM    along with Vrrtep CLI.  If not, see <http://www.gnu.org/licenses/>

:START
SET /A TOTALFILES=1
SET /A OKFILES=0
SET /A FAILEDFILES=0
cd %~dp0

REM Post-update code
if "%1"=="/PF" (
	chgcolor 0a
	echo Updating dictionaries
	chgcolor 07
	echo.
	call "%~dp0vrrtepcli_update.cmd" /NH
	set APPVERSION=
	if exist "updscript.cmd" del "updscript.cmd"
	chgcolor 0a
	echo Finished.
	chgcolor 07
	goto END
)

chgcolor 0e
echo VrrtepCLI Program Updater for Windows
echo By Swoka Ikran 
echo (portions from Linux version by Tirea Aean)
echo.
chgcolor 07
if exist "updscript.cmd" del "updscript.cmd"
echo Downloading update script
call :Get_File http://swokaikran.skxawng.lu/vcli_win/common/updscript.cmd

echo.
echo   Downloaded %OKFILES% of %TOTALFILES% files.
echo   (%FAILEDFILES% failed)

if "%FAILEDFILES%" NEQ "0" goto DLERROR
:INSTALL
echo.
chgcolor 0c
echo Installing program update
chgcolor 07
updscript.cmd
GOTO END
:DLERROR
echo.
echo **********************
echo *  Download failed!  *
echo **********************
echo.
echo %FAILEDFILES% of %TOTALFILES% failed to download.
echo.
:PRMPT
SET /P UC=[T]ry again, or [E]xit :
IF "%UC%" EQU "" GOTO PRMPT
IF "%UC%" EQU "e" GOTO END
IF "%UC%" EQU "t" GOTO START

GOTO END
:Get_File
echo Downloading: %1
"%~dp0wget.exe" -q %1
if errorlevel 1 ( 
	SET /A FAILEDFILES=%FAILEDFILES%+1
	GOTO:END
)
if errorlevel 0 ( 
	SET /A OKFILES=%OKFILES%+1
)
GOTO:END

:END
