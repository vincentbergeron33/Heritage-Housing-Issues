import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

from src.machine_learning.function_saleprice_study import load_filled_data
from src.machine_learning.function_saleprice_study import paralle_plot_prep

def page_saleprice_study_body():

    df1 = load_filled_data()
    df_parallel = paralle_plot_prep(df1)

    vars_to_study = ['1stFlrSF', 'GarageArea', 'GarageYrBlt', 'GrLivArea', 'MasVnrArea', 'OpenPorchSF',
                  'OverallQual', 'TotalBsmtSF', 'YearBuilt', 'YearRemodAdd']
    
    df1_eda = df1.filter(vars_to_study + ['SalePrice'])

    st.header("Sale Price Study")

# State business requirement 1

    st.subheader("Business requirement 1")
    st.info(
        "The client is interested in discovering how the house attributes correlate with the sale price. Therefore, "
        "the client expects data visualisations of the correlated variables against the sale price to show that. \n"
    )

# Checkbox: data inspection (display the number of rows and columns in the data, and display the first ten rows of the data)

    st.subheader("Dataset preview")

    if st.checkbox("Inspect first rows of the dataset"):
        st.write(
            f"* The dataset has {df1.shape[0]} rows and {df1.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df1.head(10))
    
    st.divider()

# Display the most correlated variables to Sale Price and the conclusions.

    st.subheader("Most important features correlation")

    st.info(
        f"During the Sale Price correlation study the following features shown a strong correlation with Sale Price: \n"
        f"\n{vars_to_study}"
    )

    st.success(
        "**The following conclusions were found during the Sale Price correlation study:**\n"
        "- When 1stFlrSF increase, the SalePrice tend to increase.\n"
        "- When GarageArea increase, the SalePrice tend to increase. The house without a garage (GarageArea = 0) are worth <=200 000.\n"
        "- Sale Price tend to increase when GarageYrBlt increase. The more recent the Garage is, Sale Price increase.\n"
        "- When GrLivArea increase, the SalePrice tend to increase.\n"
        "- When MasVnrArea increase, the SalePrice tend to increase slightly.\n"
        "- In general, SalePrice is well distributed whatever size is the OpenPorchSF."
        " The highest SalePrice observed are when OpenPorchSF is between 0 and 200\n"
        "- When Overallqual increase, the SalePrice tend to increase. Following the Spearman and Pearson, it most correlated feature to the target.\n"
        "- When TotalBsmtSF increase, the SalePrice tend to increase.\n"
        "- When YearBuilt increase, the SalePrice tend to increase. This trend goes more exponential from the year 1980.\n"
        "- When YearRemodAdd increase, the SalePrice tend to increase. This trend goes more exponential from the year 1980.\n"

        "\nWe can also notice from the data that SalePrice is well distributed.\n"
    )
    st.divider()

# Checkbox: Individual plots showing the correlation between Sale Price and the numerical variables.

    st.subheader("Correlation in graphics")

    if st.checkbox("Plot shown correlation between SalePrice and all Features with moderate to high correlation."):
        saleprice_correlation_with_feature(df1_eda)

    st.divider()

# Checkbox: Parallel plot showing the correlation between Sale Price and the categorical variables.

    st.subheader("Parralel plot for categorical features")

    if st.checkbox("Parralel plot with categorical features"):
        parallel_plot_categorical(df_parallel)

def saleprice_correlation_with_feature(df):
    target_var = "SalePrice"

    for col in df.drop([target_var], axis=1).columns.to_list():
        plot_numerical(df, col, target_var)

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.scatterplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()

def parallel_plot_categorical(df):

    fig = px.parallel_categories(df)
    st.plotly_chart(fig)