# from flask import Flask, render_template,request


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/data',methods = ['GET','POST'])
# def data():
#     user_data = request.form
#     print(user_data)

#     return  "Data Captured"
# if __name__ == '__main__':
#     app.run(debug=True)


######################################


# from flask import Flask, render_template,request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "default API"

# @app.route('/userdata',methods = ['GET','POST'])
# def data():

#     if request.method == 'POST':
#         data  = request.form
#         user_name = data['first_name']
#         print(user_name)
#     else:
#         data = request.form.get('first_name')
#         print(data)

#     return  "Data Captured"
# if __name__ == '__main__':
#     app.run(debug=True)



######################################## 

# from flask import Flask, render_template,request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/data',methods = ['GET','POST'])
# def data():

#     if request.method == 'POST':
#         data  = request.form
#         # user_name = data['first_name']
#         print(data)
#     else:
#         data = request.form.get('first_name')
#         print(data)

#     return  render_template('display.html',data_user=data)
# if __name__ == '__main__':
#     app.run(debug=True)


######################################
# Display data on front end 
# ###################################
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data',methods = ['GET','POST'])
def data():
    user_data = request.form
    print(user_data)

    var = "Python data Science"

    return render_template('index.html',data=user_data)
if __name__ == '__main__':
    app.run(debug=True)