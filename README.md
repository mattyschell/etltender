## ETLTender

### 

The ETLTender project is intendered to extract spatial data from some sources
(Web Feature Service, Socrata Open Data, etc) and load them tenderly to internal 
databases. Every year or two I make one of these with high hopes and quickly 
transform it into a dumpster fire of one-offs and regrets.   

### Dependencies

* Python3 with virtualenv and pip
* A client for target database(s) with SQLCl, psql, etc on Path
* Windows x64 only
* If writing to Oracle ogr2ogr (on path) with OCI driver. Other standard ogr2ogr drivers are included    


### Setup

Start up a virtualenv and pip install the peeps

```shell
> setenv.bat
```

If ogr2ogr with OCI driver isn't already set, QGIS is usually a solid source

```shell
> set PATH="C:\Program Files\QGIS 3.4\bin";%PATH%
> set GDAL_DATA="C:\Program Files\QGIS 3.4\share\gdal"
```

### Test 

```shell
> test_all.bat
```