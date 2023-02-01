from flask import Flask,render_template,request,redirect,url_for
import pickle
import numpy as np
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/linearregression', methods = ['GET','POST'])
def linear_regression():
    if request.method == 'POST':
        LR_model = pickle.load(open('LR_model.pkl','rb'))
        features = [int(x) for x in request.form.values()]
        final_values = [np.array(features)]
        prediction = LR_model.predict(final_values)
        # print(prediction)
        output = '{0:.{1}f}'.format(prediction[0],2)
        return render_template("linearregression.html", pred =  'Predicted AQI is {}'.format(output) )
    else:
        return render_template("linearregression.html")

   
    
    
    

if __name__ == "__main__":
    app.run(debug = True)

