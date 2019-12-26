import unittest
try:
    import cx_Oracle
except:
    sys.exit('ERROR: cannot import cx_Oracle')
import oracletender


class OracletenderTestcases(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.myconn = oracletender.oraclemgr('MSCHELL'
                                             ,None
                                             ,'GEOCDEV.DOITT.NYCNET')

    def testDummy(self):

        sql = """SELECT dummy from dual"""
        self.myconn.cursorinit(sql)
        
        while True:

            row = self.myconn.cur.fetchone()

            if row is None:
                break

            self.assertEqual(row[0], 'X')

    def testDummySquared(self):

        sql = """SELECT dummy, dummy from dual
                 UNION ALL
                 SELECT dummy, dummy from dual"""
        self.myconn.cursorinit(sql)
        
        while True:

            row = self.myconn.cur.fetchone()

            if row is None:
                break

            self.assertEqual(row[0], 'X')
            self.assertEqual(row[1], 'X')

if __name__ == '__main__':
    unittest.main()