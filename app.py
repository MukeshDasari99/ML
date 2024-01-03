from flask import Flask, render_template,request
from args import *
import pickle
import numpy as np
with open('Model.pkl', 'rb') as f:
      model = pickle.load(f)
with open('Scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def index():
    # print(request.method)
    # print(request.form)
    if request.method=='POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bathrooms']
        location=request.form['Location']
        Sft=request.form['Sft']
        status=request.form['Status']
        facing=request.form['Facing']
        type=request.form['Type']
        input_array=np.array([[bedrooms,bathrooms,location,Sft,status,facing,type]])
        input_df=scaler.transform(input_array)
        prediction=model.predict(input_df)[0]
        print(prediction)
        return render_template('index.html',Location=Location,Status=Status,Type=Type,Facing=Facing,prediction=prediction)
    else:
        return render_template('index.html',Location=Location,Status=Status,Type=Type,Facing=Facing)
@app.route('/second')
def second():
    return 'I am in Second Page'
@app.route('/third')
def third():
    return 'I am in Third Page'
if __name__=='__main__':
    app.run()   
#app.run(use_reloader=True,debug=True) use the use_reloader,debug while only in development processs
