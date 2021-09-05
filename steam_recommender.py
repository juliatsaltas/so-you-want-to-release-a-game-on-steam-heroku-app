import streamlit as st
import pandas as pd
import numpy as np

def app():

	steam = pd.read_csv('steam_clean_recommender.csv')
	pivot = pd.read_csv('steam_recommender_pivot.csv')
	pivot.set_index('game',inplace=True)

	### 1. Upload dataframe with clustered user data
	df_recommender = pd.read_csv('steam_recommender.csv')
	df_recommender.set_index('game',inplace=True)
	
	# 2. User input of game
	def user_input_features():
		search = st.text_input("Search Game Title")
		data = {'search': search}
		features = pd.DataFrame(data, index=[0])
		return features
	
	user_input = user_input_features()
	
	search = user_input['search'][0]
	count = 0
	for title in steam.loc[steam['game'].str.contains(search), 'game']:
		st.write(title)
		st.write(f"Number of Players: {pivot.T[title].count()}")
		st.write("10 closest titles:")
		st.write(round(df_recommender[title].sort_values(ascending=False)[1:11], 2))
		if count > 1:
			break
		else:
			count+=1

	    
