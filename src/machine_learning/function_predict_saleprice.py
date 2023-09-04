import streamlit as st
import pandas as pd
import numpy as np
import joblib

def load_client_houses():
    df2 = pd.read_csv("inputs/datasets/raw/house-price/house-price/inherited_houses.csv")
    return df2

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)

def predict_client_saleprice(df2, saleprice_pipeline):

    # Drop WoodDeckSF
    df2_cleaned = df2.drop("WoodDeckSF", axis=1)

    # predict
    saleprice_prediction = saleprice_pipeline.predict(df2_cleaned)

    #statement to show the Sale price
    statement = (f"- The predicted Sale Price of the house #1 is : {saleprice_prediction[0]}\n"
                 f"- The predicted Sale Price of the house #2 is : {saleprice_prediction[1]}\n"
                 f"- The predicted Sale Price of the house #3 is : {saleprice_prediction[2]}\n"
                 f"- The predicted Sale Price of the house #4 is : {saleprice_prediction[3]}\n")

    st.write(statement)

def predict_saleprice(X_live, saleprice_pipeline):

    # Drop WoodDeckSF
    X_live_saleprice = X_live.drop("WoodDeckSF", axis=1)

    # predict
    saleprice_prediction = saleprice_pipeline.predict(X_live_saleprice)

    #statement to show the Sale price
    statement = ( f" The predicted Sale Price of the house is {saleprice_prediction}")

    st.write(statement)