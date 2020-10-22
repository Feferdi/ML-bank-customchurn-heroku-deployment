# -*- coding: utf-8 -*-
"""
Created on Thursday October 09 02:20:31 2020
@author: K. Feferdi
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("rfmodel.pkl","rb")
rfmodel=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_custom_churn(age,duration,quarterly_indicator,loan):
    
    """Let's Analyse Custom Churn 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: age
        in: query
        type: number
        required: true
      - name: duration
        in: query
        type: number
        required: true
      - name: quarterly_indicator
        in: query
        type: number
        required: true
      - name: loan
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=rfmode.predict([[age,duration,quarterly_indicator,loan]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Custom Churn")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Custom Churn ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age","Type Here")
    duration = st.text_input("Duration","Type Here")
    quarterly_indicator = st.text_input("quarterly_indicator","Type Here")
    loan = st.text_input("Loan","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_custom_churn(age,duration,quarterly_indicator,loan)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()    