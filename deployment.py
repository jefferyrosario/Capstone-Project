from flask import Flask, render_template, request, redirect, url_for
import csv
from joblib import load
from werkzeug import secure_filename
import pandas as pd
#load the pipeline object

pipeline = load('text_classification.joblib')

fi = 'file_to_predict.txt'

def get_prediction(csv_file):
	to_predict = pd.read_csv(csv_file)
	prediction = pipeline.predict(to_predict)
	return prediction
	

app = Flask(__name__)




@app.route('/home')

def upload_file():
   return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
	if request.method == 'POST':
		f = request.files['file']
		#f.save(secure_filename(f.filename))
		pred = get_prediction(f)
		return pred
	
#@app.route('./prediction')

def prediction():
	render_template('predict.html')

if __name__ == '__main__':
   app.run(debug = True)