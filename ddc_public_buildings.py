import os
from wfstender import wfsmanager
from ogrtender import fileogrmanager


#typename='DDC_ACTIVEPROJECTS_PUBLIC:DDC_Active_Infrastructure_Projects'
typename='DDC_ACTIVEPROJECTS_PUBLIC:DDC_Active_Public_Buildings_Projects'
wfsurl = 'https://dservices.arcgis.com/v09SvJE7IY8GgvSx/arcgis/services/DDC_ACTIVEPROJECTS_PUBLIC/WFSServer'

tempfile = os.path.join(os.environ['TEMP'],'ddc_public_buildings.gml')
print ('downloading to ' + tempfile)

mywfs = wfsmanager(wfsurl
                  ,'2.0.0')

mywfs.download(typename
              ,tempfile)

#myogrfile = fileogrmanager(tempfile)
#doesnt exist how did I do this before
#print (myogrfile.isvalid())

print ("done friend")
