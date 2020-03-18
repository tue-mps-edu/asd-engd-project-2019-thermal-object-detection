@echo off
Color 0A

if "%~1" neq "" goto :%~1

:: Start installation of the object detection api
:----------------------------------
@Echo Welcome to the installation of object detection API.
SET mypath=%~dp0
setx tensorflow_training %mypath% 
cd /d %mypath%
cd "third_party"
cd "../"

:: Installing conda virtual environment
:-------------------------------------- 

for /f "delims=" %%F in ('where anaconda') do set target=%%F 
set directorynew1=%target%"\..\
cd /d "%directorynew1%"
setx directorynew "%cd%"
set root="%cd%"
call %root%\activate.bat %root%
cd /d "%Location%"
cd "environment"
call conda env create -f tf1_12_gpu.yml
call conda activate tf1_12_gpu
cd "../"
call conda develop %cd%\third_party\models\research\slim
call conda develop %cd%\third_party\models\research\object_detection
call conda develop %cd%\third_party\models\research\slim\nets
call conda develop %cd%\third_party\models\research\object_detection\protos
call conda develop %cd%\third_party\protoc-3.11.4-win64\bin
setx Path "%cd%\third_party\models\research\slim;%cd%\third_party\protoc-3.11.4-win64\bin;%cd%\third_party\models\research\object_detection\protos;%cd%\third_party\models\research\slim\nets;%cd%\third_party\models\research\object_detection;%Path%" /m
setx Path "C:\Windows\System32;C:\Program Files\Git\cmd;C:\Program Files\Git\bin;%Path%" 
cd /d "third_party\models\research"
msg * A restart is requried to install rest of the script. Please save your work and press ok!
pause
@Echo Confirm to continue with the restart
pause

call :markReboot stuff2
goto :eof

pause
:stuff2

::............................................................
REM  --> Check for permissions
   IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges in order to continue installation...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

::.............................................................

cd /d "%tensorflow_training%"
cd "thermal_object_detection"
set root="%directorynew%"
call %root%\activate.bat %root%
call conda activate tf1_12_gpu
cd "third_party\models\research"
protoc object_detection/protos/*.proto --python_out=.
pip install git+https://github.com/philferriere/cocoapi.git#egg=pycocotools^&subdirectory=PythonAPI
python setup.py build
python setup.py install
cd "../"
cd "../"
cd "../"
cd tensorflow_training
python model_builder_test.py
@Echo The installation is now successful! Press any key to exit the script...
pause

exit
cmd /k

:markReboot
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce /t REG_SZ /d "\"%~dpf0\" %~1" /v  RestartMyScript /f 
shutdown /r /t 0