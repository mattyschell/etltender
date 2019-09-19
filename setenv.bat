REM ME ONLY TAKE THIS OUT LATER FREND
set PATH=c:\Users\mschell\AppData\Local\Programs\Python\Python37;%PATH%
set PATH=c:\Users\mschell\AppData\Local\Programs\Python\Python37\Scripts;%PATH%
virtualenv %USERPROFILE%\.virtualenv\etltender
REM this puts virtualenv \Scripts at front of path
%USERPROFILE%\.virtualenv\etltender\Scripts\activate.bat
REM from any virtualenv, includes OWSLib
pip install -r requirements.txt
REM wheel downloaded from the famous GOHLKE on 20190919 
REM https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
REM Python 37 on x64 Windows, includes full ogr distribution and python bindings
REM Does not include the OCI driver that would be too EZ
REM will install to the virtual env
pip install src\main\resources\GDAL-3.0.1-cp37-cp37m-win_amd64.whl
