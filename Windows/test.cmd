setlocal
cd %~dp0
set LOG="%CD%\VCLITEST.LOG"
set TT=18
set PYTHONIOENCODING=UTF-8
echo off
cls
title VCLI-RAT
if exist "%LOG%" del "%LOG%"
copy /Y "empty.utf" %LOG% > NUL
if "%1" == "" ( 
	cd vcli_win
) else (
	cd "%1"
)
if "%2" == "" ( 
	set DELAY=1500
) else (
	set DELAY=%2
)

echo RaxAppTest Script for VCLI 1.9x
echo Written by SacredBanshee
echo.
echo Part of the vCLI project
echo.
call :wlog TestLog from RaxAppTest for VCLI
call :wlog Started on %date% at %time%
call :wlog .
call :wlog Source located in: %cd%
call :wlog ****Begin Tests****
echo. >> %LOG%
call :wlog Running Test 1 of %TT% (Arguments: E-N) ( -l "run" ):
python vrrtepcli.py -l "run" >> %LOG% 2>&1

call :wlog Running Test 2 of %TT% (Arguments: E-N Unicode fault) ( -l "do not" ):
python vrrtepcli.py -l "do not" >> %LOG% 2>&1

call :wlog Running Test 3 of %TT% (Arguments: N-E) ( plltxe ):
python vrrtepcli.py plltxe >> %LOG% 2>&1

call :wlog Running Test 4 of %TT% (Arguments: N-E Unicode fault) ( nìmun ):
echo (Expected result is NOT FOUND due to limitations) >> %LOG%
python vrrtepcli.py nìmun >> %LOG% 2>&1

call :wlog Running Test 5 of %TT% (Arguments: Infixation) ( -l -i hunt ):
python vrrtepcli.py -l -i hunt >> %LOG% 2>&1

call :wlog Running Test 6 of %TT% (Interactive Na'vi-English):
start "" "%~dp0\SK.exe" skxawng VCLI-RAT %DELAY% 1
call :wlog Input value: skxawng
python vrrtepcli.py >> %LOG% 2>&1

call :wlog Running Test 7 of %TT% (Interactive English-Na'vi):
start "" "%~dp0\SK.exe" converse VCLI-RAT %DELAY% 1
call :wlog Input value: converse
python vrrtepcli.py -l >> %LOG% 2>&1

call :wlog Running Test 8 of %TT% (Scramble output check):
start "" "%~dp0\SK.exe" WRONGANSWER VCLI-RAT 1500 6
start "" "%~dp0\SK.exe" /quit VCLI-RAT 9500 1
python vrrtepcli.py -s >> %LOG% 2>&1

call :wlog Running Test 9 of %TT% (Scramble answer check):
start "" "%~dp0\SK.exe" ans VCLI-RAT 2000 3
start "" "%~dp0\SK.exe" /quit VCLI-RAT 6500 1
python vrrtepcli.py -s >> %LOG% 2>&1

call :wlog Running Test 10 of %TT% (Quiz check, part 1):
start "" "%~dp0\SK.exe" 1 VCLI-RAT 1500 6
start "" "%~dp0\SK.exe" 5 VCLI-RAT 9500 1
python vrrtepcli.py -q >> %LOG% 2>&1

call :wlog Running Test 11 of %TT% (Quiz check, part 2):
start "" "%~dp0\SK.exe" 1 VCLI-RAT 1500 6
start "" "%~dp0\SK.exe" 5 VCLI-RAT 9500 1
python vrrtepcli.py -q -l >> %LOG% 2>&1

call :wlog Running Test 12 of %TT% (Quiz answer function check):
start "" "%~dp0\SK.exe" 4 VCLI-RAT 1500 6
start "" "%~dp0\SK.exe" 5 VCLI-RAT 9500 1
python vrrtepcli.py -q >> %LOG% 2>&1

call :wlog Running Test 13 of %TT% (Rhyming Dictionary, interactive):
start "" "%~dp0\SK.exe" taron VCLI-RAT 1500 1
python vrrtepcli.py -r >> %LOG% 2>&1

call :wlog Running Test 14 of %TT% (Rhyming Dictionary, arguments):
python vrrtepcli.py -r tswayon >> %LOG% 2>&1

call :wlog Running Test 15 of %TT% (-s -n exclusivity test):
python vrrtepcli.py -s -n >> %LOG% 2>&1

call :wlog Running Test 16 of %TT% (Na'vi-Na'vi infixation):
python vrrtepcli.py -i -n yom >> %LOG% 2>&1

call :wlog Running Test 17 of %TT% (IPA anti-crash, part 1):
python vrrtepcli.py -ipa -n yom >> %LOG% 2>&1

call :wlog Running Test 18 of %TT% (IPA anti-crash, part 2):
python vrrtepcli.py -i -n -ipa yom >> %LOG% 2>&1


call :wlog Finished running tests.
echo.


goto end
REM Logger function
:Wlog
echo %* >> %LOG%
echo %*
GOTO:EOF
:end
echo. >> %LOG%
call :wlog Testing concluded on %date% at %time%
CD %~dp0
set PYTHONIOENCODING=
endlocal
echo Close this window to exit.
:hang
goto hang
