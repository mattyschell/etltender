REM notes on setup from python 3.7
REM reminder on standard setup patterns, hard coded for now
set PATH=c:\Users\mschell\AppData\Local\Programs\Python\Python37
set PATH=%PATH%;c:\Users\mschell\AppData\Local\Programs\Python\Python37\Scripts
pip install virtualenv
REM mkdir %USERPROFILE%\.virtualenv
virtualenv %USERPROFILE%\.virtualenv\etltender
REM this puts virtualenv \Scripts at front of path
%USERPROFILE%\.virtualenv\etltender\Scripts\activate.bat
REM may need this later
REM set PATH=%PATH%;"C:\Program Files\QGIS 3.4\bin"
pip install six
pip install python-dateutil
pip install pytz
pip install requests
REM this earlier version avoids error "Proj executable not found. Please set PROJ_DIR variable."
pip install pyproj==1.9.6 
pip install OWSLib
pip freeze --requirements requirements.txt
REM from any virtualenv
REM pip install -r requirements.txt
