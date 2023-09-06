import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from src.machine_learning.function_predict_saleprice import load_pkl_file
from src.machine_learning.function_ml_performance import regression_performance, regression_evaluation
def page_project_performance_body():

# load data 
    version = "v1"

    best_pipeline = load_pkl_file(
        f'outputs/ml_pipeline/predict_SalePrice/{version}/clf_pipeline.pkl')

    best_features = plt.imread(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/features_importance.png")

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_SalePrice/{version}/y_test.csv").values

    st.header("Project Performance")

    st.info(
        "The type of the ML pipeline is Regressor and as required in the Bussiness requirement #2, it havs a R2"
        " greater then 0.75. To achieve the required R2, a PCA is required."
    )

    st.divider()

# show pipeline steps, use of st.code here for a better visualisation

    st.subheader("Ml Pipeline")

    st.write("Only one ML Pileline is required as the target wasn't imbalance.")
    st.code(best_pipeline)

    st.divider()

# Show best features

    st.subheader("Best features")

    st.write("The most important features constitute of 4 features. Unfortunately, with only those features, "
             "we can not achieve a R2 of 0.75. As shown in the ML Pipeline a PCA is required to achieve a R2" 
             " greater then 0.75, meaning we need to input all feature to get the required precision of the Sale Price.\n"
             "\n However, those 4 features will have an important impact on the Sale Price and the client"
             "can upgrade those feature to improve the Sale Price of his houses.")
    st.image(best_features)

    st.divider()

# show ML pipeline performance

    st.subheader("ML Pipeline performance")

    regression_performance(X_train, y_train, X_test, y_test,best_pipeline)
             