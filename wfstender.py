from owslib.wfs import WebFeatureService
import sys

class wfsmanager(object):

    def __init__(self,
                 wfsurl,
                 wfsversion='2.0.0'):

        # mywfs = WebFeatureService(url='https://dservices.arcgis.com/v09SvJE7IY8GgvSx/arcgis/services/DDC_ACTIVEPROJECTS_PUBLIC/WFSServer',
        #                           version=2.0.0)
        
        self.wfsurl = wfsurl
        self.wfs = WebFeatureService(url=self.wfsurl 
                                    ,version=wfsversion)

    def download(self
                ,wfstypename
                ,outtargetfile=None):

        outf = open(outtargetfile
                   ,mode='w')

        try:
            outf.write(self.launderchars(str(self.wfs.getfeature(typename=wfstypename).read(),'utf-8')))
        except TypeError as e:
            errno = e.args
            print("Error writing to file: Type error({0})".format(errno))
            print("Verify that the service {0} up and layer {1} is available".format(self.wfsurl
                                                                                    ,wfstypename))
            raise
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

        outf.close() 

    def launderchars(self,
                     dirtychars):

        # special chars get into source WFS via copy and paste from Word and etc
        # we will disallow to spare us from problems in oldskool
        # formats headed toward unknown destinations (like iso-8859-1)
        # or ,Beyonce help us, webmap 

        # yeah, this is gonna come back to haunt me when required tildes 
        # and accents get mixed in
        # maybe target should have an allowable dirt level and be cleaned there
        # But for now we are gml bound

        #scarychars = ",".join(i for i in dirtychars if ord(i)>128)
        #print ("heres the poop")
        #print (scarychars)

        # em dash —  replace with three hyphens
        # en dash –  replace with two hyphens
        # left single quotation mark - replace with single quotation mark
        # right single quotation makr - replace with single quotation mark
        # c-cedilla as in facade - replace with c like America damnit
    
        #return dirtychars.replace(u'\u2014', '---').replace(u'\u2013','--') 
        dirtychars.replace(u'\u2014', '---') \
                  .replace(u'\u2013','--') \
                  .replace(u'\u2018',"'") \
                  .replace(u'\u2019',"'") \
                  .replace(u'\u00E7','c')
        
        # everything else to trash for now

        return "".join(i for i in dirtychars if ord(i) < 128) 