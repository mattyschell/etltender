#setenv.bat
# given an image downloaded via the grabber something like
# C:\Program Files\QGIS 3.10\bin>gdal_translate 
#                                -of GTIFF 
#                                -a_ullr 1030938.91092086 199876.558875365 1034606.35743816 196583.711508099 
#                                -a_srs D:/matt_projects_data/moer/2263.prj 
#                                D:/matt_projects_data/moer/raw_imagery/BX_1984_345_8.png
#                                D:/matt_projects_data/moer/georeferenced_imagery/BX_1984_345_8.tif
# generate ala
# select 'gdal_translate -of GTIFF -a_ullr ' || minx || ' ' || maxy || ' ' || miny || ' ' || maxx || ' '
# || '-a_srs D:/matt_projects_data/moer/2263.prj '
# || 'D:/matt_projects_data/moer/raw_imagery/' || image_name || ' '
# || 'D:/matt_projects_data/moer/georeferenced_imagery/' || replace(image_name, '.png', '.tif')
# from image_extents
# TODO
# DEAL WITH DUPES image_name 

import cx_Oracle
import os

schema = 'iluvrasters'
pwd = 'iluvdoitt247'
db = 'iluvoracle247'
imagepath = os.path.join("D:/","matt_projects_data","moer","raw_imagery")

# DO NOT PASS
connection = cx_Oracle.connect(schema, pwd, db)

cursor = connection.cursor()

cursor.execute("""
        select image_data, image_name
        from image_extents
        where id > 1 and id < 55350""")
while True:
    row = cursor.fetchone()
    
    if row is None:
        break

    print ("Got ", row)
    oneblob=row[0].read()
    imagefilepath = os.path.join(imagepath, row[1])

    print ("plunking to ", imagefilepath)
    imagefile = open(imagefilepath,'wb')
    imagefile.write(oneblob)
    imagefile.close()

cursor.close()
connection.close()
