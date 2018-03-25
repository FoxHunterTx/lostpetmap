import pymysql
import dbconfig

connection=pymysql.connect(host='35.193.66.163',
        user=dbconfig.db_user,
        passwd=dbconfig.db_password)


try:
 with connection.cursor() as cursor:
  sql="CREATE DATABASE IF NOT EXISTS lostpetmap"
  cursor.execute(sql)
  sql="""CREATE TABLE IF NOT EXISTS lostpetmap.area (
    id int NOT NULL AUTO_INCREMENT,
    latitude FLOAT(10,6),
    longitude FLOAT(10,6),
    date DATETIME,
    category VARCHAR(50),
    description VARCHAR(255),
    updated_at TIMESTAMP,
    PRIMARY KEY (id))"""
  cursor.execute(sql)
  connection.commit()
finally:
  connection.close()  
