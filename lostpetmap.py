from flask import Flask
from flask import render_template
from flask import request

import json
import dbconfig
import datetime
import dateparser
#from dateutil import parser


if dbconfig.test:
  from mockdbhelper import MockDBHelper as DBHelper
else:
  from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

categories_form = ['cat','dog','other']


def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date,"%Y-%m-%d")
    except TypeError:
        return None



@app.route("/")
def home(error_message=None):
   lostpets = DB.get_all_lost_pet()
   lostpets = json.dumps(lostpets)
   return render_template("home.html",lostpetsdata=lostpets,categories=categories_form,error_message=error_message)


@app.route("/submitlostpet", methods=['POST'])
def submitlostpet():
    try:
        error_message = None
        category = request.form.get("category")
        if category not in categories_form:
          return home()

        #date = request.form.get("date")
        date = format_date(request.form.get("date"))
        if not date:
          return home("Invalid date. Please use yyyy-mm-dd format")
        try:
          latitude = float(request.form.get("latitude"))
          longitude = float(request.form.get("longitude"))
        except:
          error_message = "Latitude and Longitude have incorrect format"
          return home(error_message)
        description = request.form.get("description")
        DB.add_pet(category,date,latitude,longitude,description)
        return home()
    except Exception as e:
        print (e)


if __name__ == '__main__':
  app.run(port=5000,debug=True)

