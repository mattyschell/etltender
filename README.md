## ETLTender

### 

The ETLTender project is intendered to extract spatial data from some sources
(Web Feature Service, Socrata Open Data, etc) and load them to internal 
databases.  

### Dependencies

* Python3 with virtualenv and pip
* ogr2ogr (on path)
* client for target database(s) and SQLCl, psql, etc on Path

### Setup

Start up a virtualenv something like

    `virtualenv %USERPROFILE%\.virtualenv\etltender`
    `%USERPROFILE%\.virtualenv\etltender\Scripts\activate.bat`

Install dependencies

    `pip install -r requirements.txt`


### Test 



### Sample 