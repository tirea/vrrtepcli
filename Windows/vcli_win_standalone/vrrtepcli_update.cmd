
@echo off
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
SETLOCAL
:START
IF "%1"=="/NH" GOTO SKIPHEADER
echo VrrtepCLI Updater for Windows
echo By Swoka Ikran 
echo (portions from Linux version by Tirea Aean)
echo.
:SKIPHEADER
SET /A TOTALFILES=11
SET /A OKFILES=0
SET /A FAILEDFILES=0
cd %~dp0
if not exist .\dltemp md .\dltemp
cd dltemp
if exist *.txt del *.txt
echo Downloading %TOTALFILES% files
call :Get_File http://tirea.learnnavi.org/dictionarydata/localizedWords.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/metaWords.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/naviwords.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/de.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/eng.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/est.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/hu.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/nl.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/ptbr.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/sv.txt
call :Get_File http://tirea.learnnavi.org/dictionarydata/dictversion.txt
echo.
echo   Downloaded %OKFILES% of %TOTALFILES% files.
echo   (%FAILEDFILES% failed)

if "%FAILEDFILES%" NEQ "0" goto DLERROR
:INSTALL
echo.
echo Installing Updates
echo.
cd "%~dp0"
if exist metaWords.txt del metaWords.txt
if exist localizedWords.txt del localizedWords.txt
if exist naviwords.txt del naviwords.txt
if exist de.txt del de.txt
if exist eng.txt del eng.txt
if exist est.txt del est.txt
if exist hu.txt del hu.txt
if exist nl.txt del nl.txt
if exist ptbr.txt del ptbr.txt
if exist sv.txt del sv.txt
if exist dictVersion.txt del dictversion.txt
echo.
move /Y "%~dp0dltemp\*.txt" "%CD%"
echo.
echo Update Finished.
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
SET /P UC=[T]ry again, [I]gnore and install anyway, or [E]xit :
IF "%UC%" EQU "" GOTO PRMPT
IF "%UC%" EQU "e" GOTO END
IF "%UC%" EQU "i" GOTO INSTALL
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
rd /Q .\dltemp 2>NUL 
endlocal