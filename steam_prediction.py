import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

def app():
    st.write("""
    # Steam Success Prediction App - Indie Edition!
    Data obtained from the Steam Store raw dataset from [Kaggle](https://www.kaggle.com/nikdavis/steam-store-raw) by Nik Davis.
    
    ### Just finished making the next big hit in gaming?

    Have you ever asked yourself, "What are the chances that you can sell 20,000+ copies if you make a single-player, action-adventure game for pc and mac, release a video trailer, and have a few steam achievements?"

    This app predicts if your new game will be sucessful on Steam!

    Use the left-hand toolbar to select tags as 1 (on) or 0 (off) that are included in your game.

    Play around with a combination of features to see the probability of success of your indie game.

    In this classification prediction tool, success (1) is the probability that your game will have more than 20,000 users purchase your game.

    """)


    def user_input_features():
        single_player = st.sidebar.selectbox('Single Player',(0,1))
        multi_player = st.sidebar.selectbox('Multi Player',(0,1))
        online_multi_player = st.sidebar.selectbox('Online Multi Player',(0,1))
        local_multi_player = st.sidebar.selectbox('Local Multi Player',(0,1))
        self_published = st.sidebar.selectbox('Self Published',(0,1))
        valve_anti_cheat = st.sidebar.selectbox('Valve Anti Cheat',(0,1))
        steam_achievements = st.sidebar.selectbox('Steam Achievements',(0,1))
        steam_trading_cards = st.sidebar.selectbox('Steam Trading Cards',(0,1))
        steam_cloud = st.sidebar.selectbox('Steam Cloud',(0,1))
        full_controller_support = st.sidebar.selectbox('Full Controller Support',(0,1))
        partial_controller_support = st.sidebar.selectbox('Partial Controller Support',(0,1))
        steam_leaderboards = st.sidebar.selectbox('Steam Leaderboards',(0,1))
        dlc = st.sidebar.selectbox('Downloadable Content',(0,1))
        website = st.sidebar.selectbox('Website',(0,1))
        demos = st.sidebar.selectbox('Demos',(0,1))
        movies = st.sidebar.selectbox('Game Trailer',(0,1))
        language_count = st.sidebar.selectbox('Number of Supported Languages',(1,2,3,4,5,6,7,8))
        pc = st.sidebar.selectbox('PC Compatible',(0,1))
        mac = st.sidebar.selectbox('Mac Compatible',(0,1))
        linux = st.sidebar.selectbox('Linux Compatible',(0,1))
        action = st.sidebar.selectbox('Action',(0,1))
        casual = st.sidebar.selectbox('Casual',(0,1))
        adventure = st.sidebar.selectbox('Adventure',(0,1))
        strategy = st.sidebar.selectbox('Strategy',(0,1))
        simulation = st.sidebar.selectbox('Simulation',(0,1))
        rpg = st.sidebar.selectbox('RPG',(0,1))
        free_to_play = st.sidebar.selectbox('Free to Play',(0,1))
        racing = st.sidebar.selectbox('Racing',(0,1))
        sports = st.sidebar.selectbox('Sports',(0,1))
        violent = st.sidebar.selectbox('Violent',(0,1))
        gore = st.sidebar.selectbox('Gore',(0,1))
        sexual_content = st.sidebar.selectbox('Sexual Content',(0,1))
        nudity = st.sidebar.selectbox('Nudity',(0,1))
        education = st.sidebar.selectbox('Education',(0,1))
        early_access = st.sidebar.selectbox('Early Access',(0,1))



        data = {'single_player': single_player, 
                'multi_player' : multi_player,
                'online_multi_player' : online_multi_player,
                'local_multi_player' : local_multi_player,
                'self_published' : self_published ,
                'valve_anti_cheat' : valve_anti_cheat,
                'steam_achievements' : steam_achievements,
                'steam_trading_cards' : steam_trading_cards,
                'steam_cloud' : steam_cloud,
                'full_controller_support' : full_controller_support,
                'partial_controller_support' : partial_controller_support,
                'steam_leaderboards' : steam_leaderboards,
                'dlc': dlc,
                'website' : website,
                'demos' : demos,
                'movies' : movies,
                'language_count' : language_count,
                'pc' : pc,
                'mac' : mac,
                'linux' : linux,
                'action' : action,
                'casual' : casual,
                'adventure' : adventure,
                'strategy' : strategy,
                'simulation' : simulation,
                'rpg' : rpg,
                'free_to_play' : free_to_play,
                'racing' : racing,
                'sports' : sports,
                'violent' : violent,
                'gore' : gore,
                'sexual_content' : sexual_content,
                'nudity' : nudity,
                'education' : education,
                'early access' : early_access}

        features = pd.DataFrame(data, index=[0])
        return features
    

    # Combines user input features with entire penguins dataset
    # This will be useful for the encoding phase
    steam_raw = pd.read_csv('steam_indie_clean.csv')
    steam = steam_raw.drop(columns=['label'])
    df = steam #pd.concat([input_df,steam],axis=0) # Enabled Dec 14 2021

    # Encoding of ordinal features
    # https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering

    encode = ['single_player','multi_player',
    'online_multi_player', 'local_multi_player',
    'valve_anti_cheat', 'steam_achievements',
    'steam_trading_cards', 'steam_cloud',
    'full_controller_support', 'partial_controller_support',
    'steam_leaderboards', 'dlc', 'website',
    'demos','movies',
    'language_count',
    'pc', 'mac', 'linux', 
    'action', 'casual', 'adventure', 'strategy',
    'simulation', 'early access', 'rpg', 'free_to_play',
    'racing', 'sports', 'violent', 'gore', 'sexual_content',
    'nudity', 'education', 'self_published']

    # enabled Dec 14 2021
    for col in encode:
         dummy = pd.get_dummies(df[col], prefix=col)
         df = pd.concat([df,dummy], axis=1)
         del df[col]
    df = df[:1] # Selects only the first row (the user input data)

    # Displays the user input features
    # st.subheader('User Input features')

    # if uploaded_file is not None:
    #     st.write(df)
    # else:
    #     st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    #     st.write(df)

    # Reads in saved classification model
    load_clf = pickle.load(open('2indie_steam_clf.pkl', 'rb'))

    # Apply model to make predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)


    # st.subheader('Prediction')
    # label_success = np.array(['<20,000 downloads','20,000+ downloads'])
    # st.write(label_success[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)
