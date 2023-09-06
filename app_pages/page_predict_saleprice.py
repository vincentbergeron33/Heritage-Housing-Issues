import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# To make it clean, we use a different files for all functions.
# Therefore we import them in this file.

from src.machine_learning.function_saleprice_study import load_filled_data
from src.machine_learning.function_predict_saleprice import load_pkl_file, predict_saleprice, load_client_houses, predict_client_saleprice

# Body that is shown in the app

def page_predict_saleprice_body():

# We load the data using function from function_predict_saleprice
    df2 = load_client_houses()

    version = 'v1'
    saleprice_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/clf_pipeline.pkl")

    st.header("Predict Sale Price")

    st.subheader("Business Requirement 2")

    st.info(
        "- We want to predict the Sale Price and share the information with the client.\n"
        "- To predict Sale Price, we use a Regressor with a minimum R2 score of 0.75. \n"
        "- We predict the Sale Price of the 4 client's houses. \n"
        "- We create a tool to predict any house which can be easily use by the client by entering the data manually."
    )

    st.divider()
# We show the database of the client house

    st.subheader("Dataset of client's houses preview ")

    if st.checkbox("Show client house data"):
        st.write(df2.head(4))

    st.divider()

# Predict the Sale Price of the client's houses and return a statement, function is developed in function_predict_saleprice

    st.subheader("Predicted Sale Price for client's houses")

    if st.checkbox("Predicted Sale Price of the client's houses"):
        predict_client_saleprice(df2, saleprice_pipeline)

    st.divider()

# We get the data from where we want to predict the Sale price from the input of function DrawImputWidgets

    X_live = DrawInputsWidgets()

# We predict the Sale Price of the input using the function developed in function_predict_saleprice

    st.subheader("Predict House Sale Price Tool")

    if st.button("Predict House Sale Price"):
        predict_saleprice(X_live, saleprice_pipeline)


# The below function is taken from Walkthrough project 2 of the Code Institute course
# It shows an input which is tailored for each feature.

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