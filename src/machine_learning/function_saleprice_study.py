import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache_data
def load_filled_data():
    df1 = pd.read_csv("outputs/datasets/filled/HousePriceRecordFilled.csv")
    return df1

