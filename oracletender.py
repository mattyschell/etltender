import cx_Oracle

class oraclemgr(object):

    def __init__(self
                ,schema
                ,pwd
                ,db):

        self.schema = schema
        self.db     = db

        self.setpwd(pwd)

        self.conn = cx_Oracle.connect(schema
                                     ,self.pwd
                                     ,db)

    def setpwd(self
              ,pwd = None):
    
        if pwd is not None:
            self.pwd = pwd
        
        else:
            
            import getpass
            import sys
        
            msg = 'Comrade, tell me password for {schema} on {db}: '.format(schema=self.schema
                                                                           ,db=self.db)
            pwstr = getpass.getpass(prompt=msg
                                    ,stream=sys.stderr)

            self.pwd = pwstr.rstrip()

    def cursorinit(self
                  ,sql):

        self.cur = self.conn.cursor()

        try:
            self.cur.execute(sql)
        except:
            raise RuntimeError("Raising total failure to execute {sql}".format(sql=sql))
        