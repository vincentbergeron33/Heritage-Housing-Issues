import streamlit as st
import pandas as pd
import numpy as np
import joblib

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

def predict_saleprice(X_live, saleprice_pipeline):

    # Drop WoodDeckSF
    X_live_saleprice = X_live.drop("WoodDeckSF", axis=1)
    X_live_saleprice.count()

    # predict
    saleprice_prediction = saleprice_pipeline.predict(X_live_saleprice)

    #statement to show the Sale price
    statement = ( f" The predicted Sale Price of the house is {saleprice_prediction}")

    st.write(statement)