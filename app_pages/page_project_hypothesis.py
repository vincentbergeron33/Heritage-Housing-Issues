import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def page_project_hypothesis_body():
    st.write("## Project Hypothesis")

    st.success(
        "1. We suspect that the overall quality will have an important impact on the Sale Price."
        " Better is the overall quality, the higher should the Sale Price be. \n"
        "\n**Correct** The correlation study shows that Overall quality is one of most correlated feature"
        " with the target Sale Price. The modeling and evalation shows that Overall quality is the most"
        " important feature to predict the Sale Price. \n"
        "\n2. We suspect that the overall condition will have an important impact on the Sale Price."
        "Better is the overall condition, the higher should the Sale Price be.\n"
        "\n**:red[Incorrect]** The correlation study shows that the Overall condition is not one of the most"
        " correlated feature and the modeling and evaluation shows that it is not on of the best features"
        " to predict the Sale Price. \n"
        "\n3. We suspect that the Remodel date will have an important impact on the Sale Price."
        " The latest is has been remodel or built, the higher should the Sale Price be.\n"
        "\n**Correct**. The correlation study shows that the Remodel date is one of most correlated"
        " feature with the target Sale Price. The modeling and evalation shows that Remodel date"
        " is one of the best features to predict the Sale Price."
    )