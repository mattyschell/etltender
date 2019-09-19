REM notes on setup from python 3.7
REM reminder on standard setup patterns, hard coded for now
REM python ENVs 
set PATH=c:\Users\mschell\AppData\Local\Programs\Python\Python37
set PATH=%PATH%;c:\Users\mschell\AppData\Local\Programs\Python\Python37\Scripts
REM GDAL ENVs
REM I use GDAL as included in QGIS, it is easy 
REM alternatively set up standalone GDAL (yikes) http://www.gisinternals.com/
REM or use your local PostGIS install C:\Program Files\PostgreSQL\10\bin 
set PATH=%PATH%;"C:\Program Files\QGIS 3.4\bin"
set GDAL_DATA="C:\Program Files\QGIS 3.4\share\gdal"
REM virtualenv
pip install virtualenv
REM mkdir %USERPROFILE%\.virtualenv
virtualenv %USERPROFILE%\.virtualenv\etltender
REM this puts virtualenv \Scripts at front of path
%USERPROFILE%\.virtualenv\etltender\Scripts\activate.bat
pip install six
pip install python-dateutil
pip install pytz
pip install requests
REM this earlier version avoids error "Proj executable not found. Please set PROJ_DIR variable."
pip install pyproj==1.9.6 
pip install OWSLib
pip freeze --requirement requirements.txt
REM from any virtualenv
REM pip install -r requirements.txt
