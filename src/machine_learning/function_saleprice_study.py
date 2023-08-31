import streamlit as st
import pandas as pd
import numpy as np
import joblib
from feature_engine.discretisation import ArbitraryDiscretiser

@st.cache_data
def load_filled_data():
    df1 = pd.read_csv("outputs/datasets/filled/HousePriceRecordFilled.csv")
    return df1

def paralle_plot_prep(df1):

    variables_categorical = ['BsmtExposure', 'BsmtFinType1', 'GarageFinish', 'KitchenQual']

    df_parallel = df1.filter(variables_categorical + ['SalePrice'])

    sale_price_map = [-np.Inf, 100000, 200000, 300000, 400000, 500000, np.Inf]
    disc = ArbitraryDiscretiser(binning_dict={'SalePrice': sale_price_map})
    df_parallel = disc.fit_transform(df_parallel)

    n_classes = len(sale_price_map) - 1
    classes_ranges = disc.binner_dict_['SalePrice'][1:-1]

    labels_map = {}
    for n in range(0, n_classes):
        if n == 0:
            labels_map[n] = f"<{classes_ranges[0]}"
        elif n == n_classes-1:
            labels_map[n] = f"+{classes_ranges[-1]}"
        else:
            labels_map[n] = f"{classes_ranges[n-1]} to {classes_ranges[n]}"
    
    df_parallel['SalePrice'] = df_parallel['SalePrice'].replace(labels_map)

    return df_parallel
