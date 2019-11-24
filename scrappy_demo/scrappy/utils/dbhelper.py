import pymysql
import settings

class Dbhelper:

    def geCursor(self):
        dbconnect = pymysql.connect(
            settings.DATABASES.get('default').get('HOST'),
            settings.DATABASES.get('default').get('USER'),
            settings.DATABASES.get('default').get('PASSWORD'),
            settings.DATABASES.get('default').get('NAME'))
        dbconnect.autocommit(True)
        cursor = dbconnect.cursor()
        return cursor

    def queryConfig(self, where):
        cursor = self.geCursor()
        sql = 'select max_level from scrappy_config where ' + where
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            max_level = row[0]
            return max_level

    def queryScrappyData(self, where):
        cursor = self.geCursor()
        sql = 'select * from scrappy_scrappyData where ' + where
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            max_level = row[0]
            return max_level
