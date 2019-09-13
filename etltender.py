# mschell! 20190913

import sys
import wfstender
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
          targetconn,
          targettemplate,
          targetname,
          targetreplace='N'):

    print("in main")




if __name__ == "__main__":

    #if len(sys.argv) != 8:
    #    usage()
    #    raise ValueError('Expected 7 inputs, see usage (may be in log')

    sourceurl = sys.argv[1]
    sourcelayer = sys.argv[2]
    targetconn = sys.argv[3]
    targettemplate = sys.argv[4]
    targetname = sys.argv[5]
    targetreplace = sys.argv[6]

    print("before main")
    
    main(sourceurl,
         sourcelayer,
         targetconn,
         targettemplate,
         targetname,
         targetreplace)

    print("peace out")