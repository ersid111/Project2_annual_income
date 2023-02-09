####################################
# USING POSTMAN APP
###################################


# import pickle
# from flask import Flask, render_template,request
# import numpy as np
# from sklearn.utils import resample

# app = Flask(__name__)

# with open('scaler.pkl','rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# with open('model.pkl','rb') as model_file:
#     model = pickle.load(model_file)

# @app.route('/')
# def index():
#     return "Default API"


# @app.route('/predict',methods= ['GET','POST'])
# def predict():

#     data = request.form
#     print(data)
    
#     user_data = np.zeros(3)
#     user_data[0] = data['age']
#     user_data[1] = data['annul'] 
#     user_data[2] = data['score']

#     scaled_user_data = scaler.transform([user_data])
#     # scaled_user_data= scaled_user_data.reshape(1,3)
#     cluster = model.predict(scaled_user_data)
#     print(cluster)

#     return "Result Prediction"

# if __name__ == '__main__':
#     app.run(debug=True)


####################################
# USING Front End 
###################################

# import pickle
# from flask import Flask, render_template,request
# import numpy as np
# from sklearn.utils import resample

# app = Flask(__name__)

# with open('scaler.pkl','rb') as scaler_file:
#     scaler = pickle.load(scaler_file)

# with open('model.pkl','rb') as model_file:
#     model = pickle.load(model_file)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/predict',methods= ['GET','POST'])
# def predict():

#     data = request.form
#     print(data)
    
#     user_data = np.zeros(3)
#     user_data[0] = data['age']
#     user_data[1] = data['annul'] 
#     user_data[2] = data['score']

#     scaled_user_data = scaler.transform([user_data])
#     # scaled_user_data= scaled_user_data.reshape(1,3)
#     cluster = model.predict(scaled_user_data)
#     print(cluster)
#     result = cluster[0]

#     if result == 0:
#         result = "Customer is from Premium"

#     return render_template('result.html',customer_cluster=result)

# if __name__ == '__main__':
#     app.run(debug=True)



########################################


import pickle
from flask import Flask, render_template,request
import numpy as np
from sklearn.utils import resample

app = Flask(__name__)

with open('scaler.pkl','rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('model.pkl','rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods= ['GET','POST'])
def predict():

    # data = request.form
    # print(data)
    
    user_data = np.zeros(3)
    user_data[0] = request.form['age']
    user_data[1] = request.form['annul'] 
    user_data[2] = request.form['score']

    scaled_user_data = scaler.transform([user_data])
    # scaled_user_data= scaled_user_data.reshape(1,3)
    cluster = model.predict(scaled_user_data)
    print(cluster)
    result = cluster[0]

    if result == 0:
        result = "Customer is from Premium"

    return render_template('result.html',customer_cluster=result)

if __name__ == '__main__':
    app.run(debug=True)