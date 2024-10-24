@echo off
echo Setting up the environment for the NAOqi Python SDK...
REM change the path below to your Python installation
set PYTHONPATH=C:\Python27\Lib\site-packages\qi
echo Starting Choregraphe...
REM change the path below to your Choregraphe installation
set CHOREGRAPHE_PATH=C:\Program Files (x86)\Softbank Robotics\Choregraphe Suite 2.8\bin
start "" "%CHOREGRAPHE_PATH%"\choregraphe_launcher.exe
:waitForPort
SET /P PORT="Enter NAO's IP address and NAOqi port number separated by a colon (:) "
if "%PORT%"=="" (
echo You must enter a port number.
goto waitForPort
)
echo starting naoqiconnection.exe at port %PORT%...
REM change the path below to the dist folder in your clone of the repository
cd C:\Users\LDGer\ProjectsVSC\robot-jumpstarter-python3\python27\dist
start naoqiconnection.exe --qi-url=%PORT% 2>&1