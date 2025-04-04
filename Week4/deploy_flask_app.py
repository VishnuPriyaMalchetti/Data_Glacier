# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 21:51:29 2025

@author: Avinash
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('toy_model.pkl','rb'))

@app.route('/')
def home():
        return render_template('index.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)        
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Toy Popularity Score is {}'.format(output))
    
if __name__ == "__main__":
     app.run(port=5000, debug=True)
        