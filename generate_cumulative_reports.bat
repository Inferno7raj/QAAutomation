@echo off

setlocal

set "allureExecutablePath=C:\Users\www.abcom.in\AppData\Roaming\npm\node_modules\allure-commandline\bin\allure" 

REM Generate cumulative reports
"%allureExecutablePath%" generate "%1" -o "%2"

endlocal
