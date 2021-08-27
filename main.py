import steam_segment
import steam_prediction
import steam_recommender
import streamlit as st

PAGES = {
    "Steam Customer Segmentation": steam_segment,
    "Indie Success Prediction": steam_prediction,
    "Steam Game Recommender (This page takes time to run. Be patient!)": steam_recommender
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
