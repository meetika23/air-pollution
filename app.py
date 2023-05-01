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
        model = pickle.load(open('LR_model.pkl','rb'))
        features = [int(x) for x in request.form.values()]
        return generate_output(model,features,"linearregression")
    else:
        return render_template("linearregression.html")

@app.route('/logisticregression', methods = ['GET','POST'])
def logistic_regression():
    if request.method == 'POST':
        model = pickle.load(open('LogR_model.pkl','rb'))
        features = [int(x) for x in request.form.values()]
        return generate_output(model,features,"logisticregression")
    else:
        return render_template("logisticregression.html")

@app.route('/randomforest', methods = ['GET','POST'])
def randomforest():
    if request.method == 'POST':
        model = pickle.load(open('RandF_model.pkl','rb'))
        features = [int(x) for x in request.form.values()]
        return generate_output(model,features,"randomforest")
    else:
        return render_template("randomforest.html")

@app.route('/decisiontree', methods = ['GET','POST'])
def decisiontree():
    if request.method == 'POST':
        model = pickle.load(open('DecT_model.pkl','rb'))
        features = [int(x) for x in request.form.values()]
        return generate_output(model,features,"decisiontree")
    else:
        return render_template("decisionTree.html")

def generate_output(model,features,str):
    final_values = [np.array(features)]
    prediction = model.predict(final_values)
    # print(features[0])
    if str == "linearregression":
        output = '{0:.{1}f}'.format(prediction[0],2)
        return render_template("{}.html".format(str), pred =  'Predicted AQI is {}'.format(output), so = features[0], no = features[1], rspm = features[2], spm = features[3])
    else:
        return render_template("{}.html".format(str), pred =  'Air Quality is {}'.format(prediction[0]),so = features[0], no = features[1], rspm = features[2], spm = features[3])


if __name__ == "__main__":
    app.run(debug = True)

