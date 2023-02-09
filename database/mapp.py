from flask import Flask,request,render_template
from flask_mysqldb import MySQL
import pickle
import numpy as np


app = Flask(__name__)


# MySQL Configuration
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "test1"

mysql = MySQL(app)

@app.route("/")
def default():
    return "Prediction API"


@app.route("/data",methods=["GET","POST"])
def Predict():
    user_data = request.form

    user_age = request.form["age"]
    user_annual = request.form["annual"]
    user_score = request.form["score"]

    cursor = mysql.connection.cursor()
    query = "create table if not exists usercluster (age varchar(10),annual varchar(10),spending_score varchar(10))"
    cursor.execute(query)

    cursor.execute("insert into usercluster(age,annual,spending_score) values(%s,%s,%s)",(user_age,user_annual,user_score))

    mysql.connection.commit()
    cursor.close()

    return "Customer Cluster Done"


if __name__ == "__main__":
    app.run(host = '127.0.0.100',debug=True)