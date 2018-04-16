import configparser
import psycopg2,psycopg2.extras
import os,os.path

class pg:
    def __init__(self):
        inifile = os.path.expanduser('~') + r'/important/password/postgres.ini'
        print(inifile)
        conf = configparser.SafeConfigParser()
        conf.read(inifile)
        host = conf.get('postgres', 'host')
        port = conf.get('postgres', 'port')
        user = conf.get('postgres', 'user')
        password = conf.get('postgres', 'password')
        self.connection = psycopg2.connect("host={} port={} dbname={} user={} password={}".format(host,port,'postgis_24_sample',user,password))
        self.pg = self.connection.cursor()
        self.connection.autocommit = True
    
    def version(self):
        pg = self.pg
        pg.execute("select version()")
        for x in pg:
            print(x)
              
    def sql(self,str):
        self.pg.execute(str)
        return self.pg
        
    def geodistance(lon1, lat1, lon2, lat2)#keido,ido
        "SELECT ST_Distance(" + \
        "ST_GeometryFromText('POINT({} {})', 4326),".format(lon1,lat1) + \
        "ST_GeometryFromText('POINT({} {})', 4326)".format(lon2,lat2) + \
        ");"

if __name__ == '__main__':
    p = pg()
    p.version()
    
    