echo off
cls
title VrrtepCLI
set /P args=Enter any arguments you want to use: 
vrrtepcli -explorer %args%
pause