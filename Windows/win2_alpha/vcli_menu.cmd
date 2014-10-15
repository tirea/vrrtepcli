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
REM
REM    This Menu utilizes ChgColor by James K. Lawless (open source under MIT license)
REM    Source and docs: http://www.mailsend-online.com/blog/setting-text-color-in-a-batch-file.html

cd %~dp0
cls
REM Default settings
set VC_PARAM=
set LANG=ENG
set DIRECT=N2L
set INFIX=0
set SCRAMBLE=0
set QUIZ=0
set RHYME=0
set UDPATE=0

REM Load the last used language so non-English users don't have to choose every time
if exist "%~dp0user_settings.bat" call "%~dp0user_settings.bat"

:_drawMenu
cls
set CHOICE=
chgcolor 0B
echo   +========================================================+
echo   ^|       Language        ^|     Translation Direction      ^|
echo   ^|                       ^|                                ^|
if "%LANG%" == "ENG" (
	if "%DIRECT%"=="N2L" (
	 	echo   ^|  [*]  ^(E^)nglish       ^|  [*]  ^(N^)a'vi-to-Local         ^|
	) else (
		echo   ^|  [*]  ^(E^)nglish       ^|  [ ]  ^(N^)a'vi-to-Local         ^|
	)
) else (
	if "%DIRECT%"=="N2L" (
	 	echo   ^|  [ ]  ^(E^)nglish       ^|  [*]  ^(N^)a'vi-to-Local         ^|
	) else (
		echo   ^|  [ ]  ^(E^)nglish       ^|  [ ]  ^(N^)a'vi-to-Local         ^|
	)
)
if "%LANG%" == "PTBR" (
	if "%DIRECT%"=="L2N" (
	 	echo   ^|  [*]  ^(P^)ortugese     ^|  [*]  ^(L^)ocal-to-Na'vi         ^|
	) else (
		echo   ^|  [*]  ^(P^)ortugese     ^|  [ ]  ^(L^)ocal-to-Na'vi         ^|
	)
) else (
	if "%DIRECT%"=="L2N" (
	 	echo   ^|  [ ]  ^(P^)ortugese     ^|  [*]  ^(L^)ocal-to-Na'vi         ^|
	) else (
		echo   ^|  [ ]  ^(P^)ortugese     ^|  [ ]  ^(L^)ocal-to-Na'vi         ^|
	)
)
if "%LANG%"=="SV" (
 		echo   ^|  [*]  ^(S^)wedish       ^|                                ^|
) else (
		echo   ^|  [ ]  ^(S^)wedish       ^|                                ^|
)
if "%LANG%"=="HU" (
 		echo   ^|  [*]  ^(H^)ungarian     ^|--------------------------------^|
) else (
		echo   ^|  [ ]  ^(H^)ungarian     ^|--------------------------------^|
)
if "%LANG%"=="NL" (
 		echo   ^|  [*]  ^(D^)utch         ^|                                ^|
) else (
		echo   ^|  [ ]  ^(D^)utch         ^|                                ^|
)
if "%LANG%"=="EST" (
	if "%INFIX%"=="1" (
 		echo   ^|  [*]  Est^(o^)nian      ^|  [*]  Show ^(I^)nfix locations   ^|
	) else (
		echo   ^|  [*]  Est^(o^)nian      ^|  [ ]  Show ^(I^)nfix locations   ^|
	)
) else (
	if "%INFIX%"=="1" (
 		echo   ^|  [ ]  Est^(o^)nian      ^|  [*]  Show ^(I^)nfix locations   ^|
	) else (
		echo   ^|  [ ]  Est^(o^)nian      ^|  [ ]  Show ^(I^)nfix locations   ^|
	)
)
if "%LANG%"=="DE" (
 		echo   ^|  [*]  ^(G^)erman        ^|                                ^|
) else (
		echo   ^|  [ ]  ^(G^)erman        ^|                                ^|
)

echo   ^|                       ^|                                ^|
echo   +--------------------------------------------------------+
echo   ^|  Additional functions:                                 ^|
echo   ^|                                                        ^|
if "%SCRAMBLE%"=="1" (
echo   ^|  [*] S^(c^)ramble Game                                   ^|
) else (
echo   ^|  [ ] S^(c^)ramble Game                                   ^|
)
if "%QUIZ%"=="1" (
echo   ^|  [*] ^(Q^)uiz Game                                       ^|
) else (
echo   ^|  [ ] ^(Q^)uiz Game                                       ^|
)
if "%RHYME%"=="1" (
echo   ^|  [*] ^(R^)hyming Dictionary                              ^|
) else (
echo   ^|  [ ] ^(R^)hyming Dictionary                              ^|
)
if "%UPDATE%"=="1" (
echo   ^|  [*] ^(U^)pdate Dictionary                               ^|
) else (
echo   ^|  [ ] ^(U^)pdate Dictionary                               ^|
)


echo   ^|                                                        ^|
echo   ^|  E^(X^)IT Program                                        ^|
echo   +--------------------------------------------------------+
echo Press the letter within parentheses to select that option.
echo Leave blank to start program with the options shown.
echo.
set /P CHOICE=Choose an option: 

if /I "%CHOICE%"=="E" set LANG=ENG
if /I "%CHOICE%"=="P" set LANG=PTBR
if /I "%CHOICE%"=="S" set LANG=SV
if /I "%CHOICE%"=="H" set LANG=HU
if /I "%CHOICE%"=="D" set LANG=NL
if /I "%CHOICE%"=="O" set LANG=EST
if /I "%CHOICE%"=="G" set LANG=DE
if /I "%CHOICE%"=="N" set DIRECT=N2L

if /I "%CHOICE%"=="L" (
	set DIRECT=L2N
	if "%SCRAMBLE%"=="1" (
		chgcolor 0e
		echo Scramble is selected and does not support localization.
		chgcolor 0f
		echo Scramble has been de-selected.
		echo Press a key...
		set SCRAMBLE=0
		pause > NUL
	)
)

if /I "%CHOICE%"=="I" (
	if "%INFIX%"=="1" (
		set INFIX=0
	) else (
		set INFIX=1
	)
)
if /I "%CHOICE%"=="C" (
	if "%SCRAMBLE%"=="1" (
		set SCRAMBLE=0
		set DIRECT=E2L
	) else (
		set SCRAMBLE=1
		set DIRECT=
		set QUIZ=0
		set RHYME=0
		set INFIX=0
		set UPDATE=0
	)
)
if /I "%CHOICE%"=="Q" (
	if "%QUIZ%"=="1" (
		set QUIZ=0
	) else (
		set QUIZ=1
		set SCRAMBLE=0
		set RHYME=0
		set INFIX=0
		set UPDATE=0
	)
)
if /I "%CHOICE%"=="R" (
	if "%RHYME%"=="1" (
		set RHYME=0
	) else (
		set RHYME=1
		set SCRAMBLE=0
		set QUIZ=0
		set DIRECT=0
		set INFIX=0
		set UPDATE=0
	)
)

if /I "%CHOICE%"=="U" (
	if "%UPDATE%"=="1" (
		set UPDATE=0
	) else (
		set UPDATE=1
		set RHYME=0
		set SCRAMBLE=0
		set QUIZ=0
		set DIRECT=0
		set INFIX=0
	)
)
if /I "%CHOICE%"=="X" goto end
if /I "%CHOICE%"=="" goto run
goto _drawMenu


:run
chgcolor 07
REM If update, do it and quit
if "%UPDATE%"=="1" (
	call vrrtepcli_update.cmd
	goto end
)

REM Start with the loop command
set VC_PARAM=-explorer

REM If Quiz, delete the loop command and set to -q
if "%QUIZ%"=="1" set VC_PARAM=-q

REM Rhyme feature
if "%RHYME%"=="1" set VC_PARAM=%VC_PARAM% -r

REM Localization support
if "%DIRECT%"=="L2N" (
	set VC_PARAM=%VC_PARAM% -l
)

REM Languages
if "%LANG%"=="ENG" set VC_PARAM=%VC_PARAM% -eng
if "%LANG%"=="PTBR" set VC_PARAM=%VC_PARAM% -ptbr
if "%LANG%"=="SV" set VC_PARAM=%VC_PARAM% -sv
if "%LANG%"=="HU" set VC_PARAM=%VC_PARAM% -hu
if "%LANG%"=="NL" set VC_PARAM=%VC_PARAM% -nl
if "%LANG%"=="EST" set VC_PARAM=%VC_PARAM% -est
if "%LANG%"=="DE" set VC_PARAM=%VC_PARAM% -de

REM Infix feature
if "%INFIX%"=="1" set VC_PARAM=%VC_PARAM% -i

REM These override anything else if set. They can't be used with other flags
if "%SCRAMBLE%"=="1" set VC_PARAM=-s

echo Launch arguments: %VC_PARAM%
echo.
echo set LANG=%LANG%>"%~dp0user_settings.bat"

call vrrtepcli %VC_PARAM%
pause
:end