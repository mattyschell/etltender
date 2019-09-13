from owslib.wfs import WebFeatureService

class wfsmanager(object):

    def __init__(self,
                 wfsurl,
                 wfsversion):

        # mywfs = WebFeatureService(url='https://dservices.arcgis.com/v09SvJE7IY8GgvSx/arcgis/services/DDC_ACTIVEPROJECTS_PUBLIC/WFSServer',
        #                           version=2.0.0)
        
        self.wfs = WebFeatureService(url=wfsurl 
                                    ,version=wfsversion)

    def download(self
                ,wfstypename
                ,outtargetfile):

        # response = mywfs.getfeature(typename='DDC_ACTIVEPROJECTS_PUBLIC:DDC_Active_Infrastructure_Projects')
        # out = open("C:/temp/ddcproj2.gml",mode='w')
        # out.write(str(response.read(),'utf-8'))

        #next try to replace em dash with hyphen
        # out.write(str(response.read(),'utf-8').replace(u'\u2014', '-', inplace=True))

        outf = open(outtargetfile)
        outf.write(str(self.wfs.getfeature(typename=wfstypename).read()
                  ,'utf-8'))
        outf.close()
    