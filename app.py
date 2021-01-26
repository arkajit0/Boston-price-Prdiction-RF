
# importing the necessary dependencies
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            zn = np.sin(float(request.form['zn']))
            indus = float(request.form['indus'])
            chas = float(request.form['chas'])
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            rad = float(request.form['rad'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            lstat = float(request.form['lstat'])
            crim = (float(request.form['crim'])**(-0.1604547970760181) - 1)/(-0.1604547970760181)
            dis = np.log(float(request.form['dis']))
            age = float(request.form['age'])
            b = 1/np.sin(1000*((float(request.form['b'])-0.63)**2))
            rad_tax_nox = tax+rad+nox


            loaded_model = pickle.load(open('final_model_v9.pkl', 'rb')) #load the model
            scale = pickle.load(open('scale.pkl', 'rb'))
            pca = pickle.load(open('principal_component.pkl', 'rb'))
            # predictions using the loaded model file
            scaled_data = pca.transform(scale.transform([[indus, chas, rm, age, ptratio, lstat, crim, zn, dis, b,
                                                         rad_tax_nox]]))
            # print(scaled_data)
            prediction = loaded_model.predict(scaled_data)
            # print(prediction)
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=1000*round(prediction[0], 3))
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)