
from flask import Flask,request,render_template
from flask_mysqldb import MySQL
import pickle
import numpy as np


app = Flask(__name__)


###### MYSQL Configuration 
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def index():

    return "API"

@app.route('/data',methods=['GET','POST'])
def data():

    user_data = request.form

    user_age = request.form['age']
    user_annual = request.form['annual']
    user_score = request.form['score']

    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS usercluster(age VARCHAR(10), annual VARCHAR(10), spending_score VARCHAR(10))'
    cursor.execute(query)

    cursor.execute('INSERT INTO usercluster(age,annual,spending_score) VALUES(%s,%s,%s)',(user_age,user_annual,user_score))

    mysql.connection.commit()
    cursor.close()

    return "Customer Cluster Done"


if __name__ == "__main__":
    app.run(host = '127.0.0.100',debug=True)