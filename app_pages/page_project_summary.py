import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def page_summary_body():
    st.header("Project Summary")

    st.subheader("Project Terms & Jargon")
    st.info(
        f"- Database is all the data that has been gathered by the client which include the **:blue[Features]** and the **:green[Target]**. \n"
        f"- **:blue[Features]** are all the variable above except the **SalePrice**. They are use to predict the **:green[Target]** which is SalePrice. \n"
        f"- **:green[Target]** is **SalePrice**. The **:green[Target]** is the variable we want to predict by using the **:blue[Features]**. \n"
        f"- **:violet[Best Features]** are the **:blue[Features]** which explain in high percentage the database. \n"
        f"- **:red[R2]** is the score a Machine Learning Regressor pipeline gets by predicting the target from the features. **:red[R2]** is between 0 and 1, the close to 1, the more precised if is the ML pipeline."
    )
    st.subheader("Describe Project Dataset")

    st.info(
        "The dataset is sourced from Kaggle. The dataset has almost 1.5 thousand rows and represents housing records from Ames,"
        "Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its"
        "respective sale price for houses built between 1872 and 2010.")
    
    st.warning("For more information on the dataset, please refer to the README file.")

    st.subheader("Business Requirements")

    st.success(
        "we are requested by the client, who has received an inheritance from a deceased great-grandfather located"
        "in Ames, Iowa, to help in maximising the sales price for the inherited properties. \n"
        "\n Although the client has an excellent understanding of property prices in her own state and residential area, she fears that"
        "basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable"
        "and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa,"
        "and will provide us with that. \n"

        "\n **Business requirement 1:** The client is interested in discovering how the house attributes correlate with the sale price. Therefore, "
        "the client expects data visualisations of the correlated variables against the sale price to show that. \n"
        "\n **Business requirement 2:** The client is interested in predicting the house sale price from her four inherited houses and any other house"
        "in Ames, Iowa."
    )