@echo off
setlocal
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
cd %~dp0

if "%1"=="-u" (
	if "%2"=="--all" (
		vrrtepcli_update_prog.cmd
		goto end
	) else (
		call vrrtepcli_update.cmd
		echo.
		echo Vrrtepcli dictionary updated.
		goto end
	)
)

if "%1"=="uninstall" (
	uninstall_vcli.cmd
	goto end
)

if "%1"=="-h" (
	echo.
	echo Vrrtep Command-line Interface Na'vi Translator v1.95.0
	echo by Tirea Aean. Licensed under GNU General Public License.
	echo Windows version by Swoka Ikran
	echo.
	echo Usage: vrrtepcli [-args][word]
	echo ----------------
	echo valid arguments:
	echo ----------------
	echo -l : translate from a local language to Na'vi
	echo ----------------
	echo local languages:
	echo ----------------
	echo -eng : english [default if no language specified]
	echo -ptbr : Brazillian Portuguese
	echo -sv : Swedish
	echo -hu : Hungarian
	echo -nl : Dutch
	echo -est : Estonian
	echo -de : German
	echo ---------------------------------
	echo -i : show possible Na'vi infix
	echo ---------------------------------
	echo -n : translate from Na'vi to local language [default if no -l, overrides -l]
	echo ---------------------------------
	echo -r : na'vi rhyming dictionary
	echo ---------------------------------
	echo -s : na'vi word scramble game
	echo ---------------------------------
	echo -q : na'vi quiz game 
	echo      TIP: Use -l and language options to play the other way
	echo  	  with localized questions and Na'vi answers.
	echo ---------------------------------
	echo -h : show this help menu
	echo ---------------------------------
	echo -u : update the vrrtepcli dictionaries
	echo -v : check dictionary version
	echo ---------------------------------
	goto end
)
chgcolor 0b
echo Vrrtep CLI v1.95.0 by Tirea Aean
echo Windows version by Swoka Ikran
chgcolor 0a
echo Standalone version
echo.
chgcolor 07

if "%1"=="-v" (

	echo Dictionary version:
	type dictversion.txt
	goto end
)


if "%1"=="-explorer" (
	set vcli_explorer=1
	shift /1
)

REM End non-program functions (updater/help/etc.)

chcp | FindStr .*437 > NUL
if %ERRORLEVEL% GTR 0 (
	chcp 437
	echo.
)
if "%1"=="" goto run

REM Check if it's a string
set /A loop=%1
if "%loop%"=="0" goto run

REM If not, loop %1 number of times
set total=%loop%
set counter=1
set /A shiftbase=2
set args=

:findArgs
echo %2 | FindStr \-.* > NUL
if %ERRORLEVEL% GTR 0 goto loop
set /A shiftbase=%shiftbase%+1
set args=%args% %2
shift /2
goto findArgs

:loop

if "%2" == "" (
	demoncli.exe -n
)
if not "%2" == "" (
	demoncli.exe %args% %2
	shift /2
)
SET /A counter=%counter%+1

if %counter% GTR %total% goto end
goto loop

:run
if "%1" == "" (
	demoncli.exe -n
	goto end
)
if not "%1" == "" (
	demoncli.exe %1 %2 %3 %4 %5 %6 %7
	goto end
)
:end
if "%vcli_explorer%"=="1" goto run
endlocal