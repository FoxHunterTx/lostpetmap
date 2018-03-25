from flask import Flask
from flask import render_template
from flask import request
import json
import dbconfig
#if dbconfig.test:
#  from mockdbhelper import MockDBHelper as DBHelper
#else:
from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()


@app.route("/")
def home():
   lostpets = DB.get_all_lost_pet()
   lostpets = json.dumps(lostpets)
   return render_template("home.html",lostpetsdata=lostpets)


@app.route("/submitlostpet", methods=['POST'])
def submitlostpet():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = float(request.form.get("latitude"))
    longitude = float(request.form.get("longitude"))
    description = request.form.get("description")
    DB.add_pet(category,date,latitude,longitude,description)
    return home()


if __name__ == '__main__':
  app.run(port=5000,debug=True)

