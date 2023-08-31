import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from src.machine_learning.function_saleprice_study import load_filled_data
from src.machine_learning.function_predict_saleprice import load_pkl_file, predict_saleprice
# Set of widgets inputs, which relates to the prospect profile. Each set of inputs is related to a given ML task to predict the Sale Price.
# "Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts the prospect Sale Price.

def page_predict_saleprice_body():

    version = 'v1'
    saleprice_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/clf_pipeline.pkl")

    st.write("## Predict Sale Price")

    st.info(
        "**Business Requirement 2:** Regressor Machine Learning Model \n"
        "- We want to predict the Sale Price.\n"
        "- To predict Sale Price, we want to use a Regressor Machine learning Model or change the ML task to "
        "classification if the regressor model doesn't achieve the minimum R2 score. \n"
        "- We want to achieve achieve a minimum R2 score of 0.75 on both Train and Test sets. \n"
        "- We want to understand the most important features."
    )

    X_live = DrawInputsWidgets()

    if st.button("Predict House Sale Price"):
        predict_saleprice(X_live, saleprice_pipeline)



def DrawInputsWidgets():

    # load dataset
    df1 = load_filled_data()
    percentageMin, percentageMax = 0.4, 2.0

# we create input widgets only for 6 features
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    col11, col12, col13, col14, col15 = st.columns(5)
    col16, col17, col18, col19, col20 = st.columns(5)
    col21, col22, col23 = st.columns(3)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # {'OnlineBackup', 'PaymentMethod', 'Contract', 'MonthlyCharges', 'PhoneService', 'InternetService'}
    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col2:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col3:
        feature = "BedroomAbvGr"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col4:
        feature = "BsmtExposure"
        st_widget = st.selectbox(
            label=feature,
            options=df1[feature].unique()
        )
    X_live[feature] = st_widget

    with col5:
        feature = "BsmtFinType1"
        st_widget = st.selectbox(
            label=feature,
            options=df1[feature].unique()
        )
    X_live[feature] = st_widget

    with col6:
        feature = "BsmtFinSF1"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col7:
        feature = "BsmtUnfSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col8:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col9:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col10:
        feature = "GarageFinish"
        st_widget = st.selectbox(
            label=feature,
            options=df1[feature].unique()
        )
    X_live[feature] = st_widget

    with col11:
        feature = "GarageYrBlt"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col12:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col13:
        feature = "KitchenQual"
        st_widget = st.selectbox(
            label=feature,
            options=df1[feature].unique()
        )
    X_live[feature] = st_widget

    with col14:
        feature = "LotArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col15:
        feature = "LotFrontage"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col16:
        feature = "MasVnrArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col17:
        feature = "EnclosedPorch"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col18:
        feature = "OpenPorchSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col19:
        feature = "OverallCond"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col20:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col21:
        feature = "WoodDeckSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col22:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget

    with col23:
        feature = "YearRemodAdd"
        st_widget = st.number_input(
            label=feature,
            min_value=df1[feature].min()*percentageMin,
            max_value=df1[feature].max()*percentageMax,
            value=df1[feature].median()
        )
    X_live[feature] = st_widget


    st.write(X_live)

    return X_live