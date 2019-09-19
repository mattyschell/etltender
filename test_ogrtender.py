import unittest
import os
import sys
try:
    from osgeo import ogr, osr, gdal
except:
    sys.exit('ERROR: cannot find GDAL/ORG modules')
ogr.UseExceptions()
import ogrtender

# Jared I thank you
# https://pcjericks.github.io/py-gdalogr-cookbook

class OgrtenderTestcases(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        dir = os.path.dirname(__file__)
        self.resourcepath = os.path.join(dir
                                        ,'src'
                                        ,'test'
                                        ,'resources')

        #give us a wkt polygon around central park
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(-8235947,4978196)
        ring.AddPoint(-8234730,4977382)
        ring.AddPoint(-8232139,4982377)
        ring.AddPoint(-8233284,4982668)
        ring.AddPoint(-8235947,4978196)

        poly = ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)

        self.testpoly = poly

        #same poly, named testpoly.geojson, in test/resources
        # print (self.testpoly.ExportToJson())

    def testPostgreSqlDriver(self):

        driverName = "PostgreSQL"
        drv = ogr.GetDriverByName( driverName )
        self.assertIsNotNone(drv)


    def testOCIDriver(self):

        driverName = "OCI"
        drv = ogr.GetDriverByName( driverName )
        self.assertIsNone(drv)

    def testFileNoExist(self):

        with self.assertRaises(ValueError):
            badfile = ogrtender.fileogrmanager('src/test/resources/filenoexist.geojson')
        

    def testOgrShell(self):

        pass


#    def testvalid(self):
#
#        testgmlfile = os.path.join(self.resourcepath
#                                  ,'valid.gml')        
#
#        print('testfilepath')
#        print(testgmlfile) 
#        validgml = ogrtender.fileogrmanager(testgmlfile)
#
#        self.assertTrue(validgml.isvalid())
#        print("yeah")




if __name__ == '__main__':
    unittest.main()