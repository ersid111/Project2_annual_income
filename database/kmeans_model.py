
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



with open('scaler.pkl','rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():

    return "API"

@app.route('/data',methods=['GET','POST'])
def data():

    user_data = request.form

    user_age = request.form['age']
    user_annual = request.form['annual']
    user_score = request.form['score']

    
    scale_data = scaler.transform([[user_age,user_annual,user_score]])
    result = model.predict(scale_data)[0]
    print(result)

    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS kmeans(age VARCHAR(10), annual VARCHAR(10), spending_score VARCHAR(10),cluster VARCHAR(10))'
    cursor.execute(query)

    cursor.execute('INSERT INTO kmeans(age,annual,spending_score,cluster) VALUES(%s,%s,%s,%s)',(user_age,user_annual,user_score,result))

    mysql.connection.commit()
    cursor.close()





    return "Customer Cluster Done"


if __name__ == "__main__":
    app.run(host = '127.0.0.100',debug=True)