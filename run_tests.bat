rmdir /s /q.\allure-latest-results
mkdir .\allure-latest-results

setlocal

set "currentDir=%CD%"

REM Define dir paths

set "cumulativeResultsDir=%currentDir%\allure-cumulative-results"
set "latestResultsDir=%currentDir%\allure-latest-results"
set "cumulativeReportsDir=%currentDir%\allure-cumulative-reports"
set "latestReportsDir=%currentDir%\allure-latest-reports"
set "apacheCumulativeReportsDir=C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\cumulative-reports"
set "apachelatestReportsDir=C:\Program Files\Apache Software Foundation\Tomcat 9.0\webapps\latest-reports"

REM Check if the directory already exists 
if not exist "%cumulativeResultsDir%" (
	REM If not, create the directory
	mkdir "%cumulativeResultsDir%"
	echo Directory created cumulativeResultsDir%"
) else (
	echo Directory "%cumulativeResultsDir%" already exists in "%currentDir%", skipping dir creation
)	


py.test.exe --alluredir="%latestResultsDir%" .\src\tests\smoke\test_case_01.py

echo %latestResultsDir%

echo %cumulativeResultsDir%

xcopy "%latestResultsDir%\*" "%cumulativeResultsDir%\" /s/


call generate_latest_reports.bat %latestReportsDir% %latestResultsDir%

xcopy "%cumulativeReportsDir%\history" "%cumulativeResultsDir%\history" /E/I/H/K/Y

call generate_cumulative_reports.bat XcumulativeReportsDir% cumulativeResultsDir%

xcopy "%latestResultsDir%\*" "%cumulativeResultsDir%\" /s /y

xcopy "%cumulativeReportsDir%\*" "%apacheCumulativeReportsDir%\" /s /y

endlocal

