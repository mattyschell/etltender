# mschell! 20190913

import sys
from wfstender import wfsmanager
import ogrtender

def usage():
    print (" ")
    print("   I am " + sys.argv[0])
    print("Usage: goes here")
    print("I received as input:")
    for arg in sys.argv:
        print(arg)



def main (sourceurl,
          sourcelayer,
          tempfile,
          targetconn,
          targettemplate,
          targetname,
          targetreplace='N'):

    print("in main")

    sourcewfs = wfsmanager(sourceurl)

    sourcewfs.download(sourcelayer
                      ,tempfile)





if __name__ == "__main__":

    #if len(sys.argv) != 8:
    #    usage()
    #    raise ValueError('Expected 7 inputs, see usage (may be in log')

    # python etltender.py
    # "https://dservices.arcgis.com/v09SvJE7IY8GgvSx/arcgis/services/DDC_IFRPROJECTS_PUBLIC/WFSServer"
    # "DDC_IFRPROJECTS_PUBLIC:DDC_Active_Infrastructure_Projects"
    # "C:/Temp/ddcinfra.gml"
    # C
    # D
    # E    
    # F

    sourceurl = sys.argv[1]
    sourcelayer = sys.argv[2]
    tempfile = sys.argv[3]
    targetconn = sys.argv[4]
    targettemplate = sys.argv[5]
    targetname = sys.argv[6]
    targetreplace = sys.argv[7]

    print("before main")
    
    main(sourceurl,
         sourcelayer,
         tempfile,
         targetconn,
         targettemplate,
         targetname,
         targetreplace)

    print("peace out")