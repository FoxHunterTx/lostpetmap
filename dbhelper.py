import datetime
import pymysql
import dbconfig

class DBHelper:

    def connect(self,database="lostpetmap"):
      return pymysql.connect(host='35.193.66.163',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password,
                             db=database)

    def add_pet(self,category,date,latitude,longitude,desc):
      connection = self.connect()
      try:
        query = "INSERT INTO area (category,date,latitude,longitude,description) VALUES (%s,%s,%s,%s,%s)"
        with connection.cursor() as cursor:
          cursor.execute(query,(category,date,latitude,longitude,desc))
          connection.commit()
      except Exception as e:
         print(e)
      finally:
         connection.close()

   
    def get_all_lost_pet(self):
        connection = self.connect()
        try:
            query = "SELECT latitude,longitude,date,category,description FROM area;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                named_lostpets = []
                for location in cursor:
                    named_lostpet = {
                            'latitude':location[0],
                            'longitude':location[1],
                            'date':datetime.datetime.strftime(location[2],'%Y-%m-%d'),
                            'category':location[3],
                            'description':location[4]
                            }
                    named_lostpets.append(named_lostpet)
            return named_lostpets
        finally:
            connection.close()



    def get_all_inputs(self):
      connection = self.connect()
      try:
        query = "SELECT description FROM area;"
        with connection.cursor() as cursor:
          cursor.execute(query)
        return cursor.fetchall()
      finally:
        connection.close()

    def add_input(self,data):
      connection = self.connect()
      try:
        query = "INSERT INTO area (description) VALUES (%s);"
        with connection.cursor() as cursor:
          cursor.execute(query,data)
          connection.commit()
      finally:
        connection.close()

    def clear_all(self):
      connection = self.connect()
      try:
        query = "DELETE FROM area;"
        with connection.cursor() as cursor:
          cursor.execute(query)
          connection.commit()
      finally:
         connection.close()



