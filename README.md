## ETLTender

### 

The ETLTender project is intendered to extract spatial data from some sources
(Web Feature Service, Socrata Open Data, etc) and load them to internal 
databases.  

### Dependencies

* Python3 with virtualenv and pip
* A client for target database(s) with SQLCl, psql, etc on Path
* (for now) Windows x64 only
* (for now) If writing to Oracle ogr2ogr (on path) with OCI driver.  Other standard ogr2ogr drivers are included    


### Setup

Start up a virtualenv and pip install the peeps

    `setenv.bat`

If ogr2ogr with OCI driver isn't already set, QGIS is usually a good source

    `set PATH="C:\Program Files\QGIS 3.4\bin";%PATH%`
    `set GDAL_DATA="C:\Program Files\QGIS 3.4\share\gdal"`

### Test 



### Sample 