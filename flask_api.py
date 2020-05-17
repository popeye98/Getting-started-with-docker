from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome all"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    #http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=4
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():

    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run()