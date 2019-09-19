from owslib.wfs import WebFeatureService

class wfsmanager(object):

    def __init__(self,
                 wfsurl,
                 wfsversion='2.0.0'):

        # mywfs = WebFeatureService(url='https://dservices.arcgis.com/v09SvJE7IY8GgvSx/arcgis/services/DDC_ACTIVEPROJECTS_PUBLIC/WFSServer',
        #                           version=2.0.0)
        
        self.wfs = WebFeatureService(url=wfsurl 
                                    ,version=wfsversion)

    def download(self
                ,wfstypename
                ,outtargetfile=None):

        # response = mywfs.getfeature(typename='DDC_ACTIVEPROJECTS_PUBLIC:DDC_Active_Infrastructure_Projects')
        # out = open("C:/temp/ddcproj2.gml",mode='w')
        # out.write(str(response.read(),'utf-8'))

        #next try to replace em dash with hyphen
        # out.write(str(response.read(),'utf-8').replace(u'\u2014', '-', inplace=True))

        outf = open(outtargetfile
                   ,mode='w')

        outf.write(self.launderchars(str(self.wfs.getfeature(typename=wfstypename).read(),'utf-8')))

        outf.close() 

    def launderchars(self,
                     dirtychars):

        # special chars get into source WFS via copy and paste from Word and etc
        # we will disallow to spare us from problems in oldskool
        # formats headed toward unknown destinations (like iso-8859-1)
        # em dash —  replace with three hyphens
        # en dash –  replace with two hyphens
    
        return dirtychars.replace(u'\u2014', '---').replace(u'\u2013','--') 