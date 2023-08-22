import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_project_summary import page_summary_body
from app_pages.page_saleprice_study import page_saleprice_study_body
from app_pages.page_predict_saleprice import page_predict_saleprice_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_project_performance import page_project_performance_body


app = MultiPage(app_name= "Heriting Housing Issues") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Sale Price Study", page_saleprice_study_body)
app.add_page("Sale Price Prediction", page_predict_saleprice_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Sale Price Model Performance", page_project_performance_body)

app.run() # Run the  app
