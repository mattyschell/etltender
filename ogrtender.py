from subprocess import Popen, PIPE
import os
from osgeo import ogr
ogr.UseExceptions()

class ogrmanager(object):

    def __init__(self):

        pass

class fileogrmanager(ogrmanager):

    def __init__(self
                ,pathtofile):

        if os.path.isfile(pathtofile):

            self.source = pathtofile

        else:

            raise ValueError('%s doesnt exist' % (pathtofile))

    #def write(self,
    #         ,format
    #         ,pathtofile):

    #writing record by record?  Is that sensible?
    #    
    #    outdriver = ogr.GetDriverByName('format')
        

class ociogrmanager(ogrmanager):

    def __init__(self
                ,vectordataset):


        self.source = vectordataset

        ogrmanager.__init__(self
                           ,vectordataset)
    
    def isvalid(self):

        pop = Popen([self.ogrinfo], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        result, errormsg = pop.communicate()
        print('res' + result)
        print('error' + errormsg)
        poprc = pop.returncode
        print('ret' + poprc)

        return True
        

