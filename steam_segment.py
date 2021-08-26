import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def app():
	st.write("""
	# Steam Segmentation Analysis

	Data obtained from the Steam Store raw dataset from [Kaggle](https://www.kaggle.com/nikdavis/steam-store-raw) by Nik Davis.
	""")

	### 1. Upload dataframe with clustered user data
	games_clusters = pd.read_csv('df_segment_cluster.csv')

	### 2. Display DataFrame
	st.subheader('Display DataFrame')
	st.write('Number of purchases per genre for each user. There are 3 clusters total.')
	df = games_clusters
	st.write(df)

	### Standardize Columns
	for col in games_clusters.columns[:-2]:
	   games_clusters[col] /= games_clusters[col].max()

	### 2. User Input
	def user_input_features():
	    pick_genre_1 = st.sidebar.selectbox('Genre 1',('Indie', 'Action', 'Casual', 'Adventure', 'Strategy', 'Simulation', 'RPG', 'Free_to_Play'))
	    pick_genre_2 = st.sidebar.selectbox('Genre 2',('Indie', 'Action', 'Casual', 'Adventure', 'Strategy', 'Simulation', 'RPG', 'Free_to_Play'))
	    pick_genre_3 = st.sidebar.selectbox('Genre 3',('Indie', 'Action', 'Casual', 'Adventure', 'Strategy', 'Simulation', 'RPG', 'Free_to_Play'))
	    data = {'Genre 1': pick_genre_1, 
	            'Genre 2': pick_genre_2,
	            'Genre 3': pick_genre_3}
	    features = pd.DataFrame(data, index=[0])
	    return features

	input_df = user_input_features()

	st.write(input_df)

	# Display 3 2D charts
	fig_1 = plt.figure(figsize=(3,3))
	plt.scatter(x=df[input_df['Genre 1'][0].lower()] , y=df[input_df['Genre 2'][0].lower()], c=df['color'])
	plt.xlabel(input_df['Genre 1'][0].lower())
	plt.xlim(0,1)
	plt.ylabel(input_df['Genre 2'][0].lower())
	plt.ylim(0, 1)
	plt.show()
	st.write(fig_1)

	fig_2 = plt.figure(figsize=(3,3))
	plt.scatter(x=df[input_df['Genre 2'][0].lower()] , y=df[input_df['Genre 3'][0].lower()], c=df['color'])
	plt.xlabel(input_df['Genre 2'][0].lower())
	plt.xlim(0, 1)
	plt.ylabel(input_df['Genre 3'][0].lower())
	plt.ylim(0, 1)
	plt.show()
	st.write(fig_2)


	fig_3 = plt.figure(figsize=(3,3))
	plt.scatter(x=df[input_df['Genre 1'][0].lower()] , y=df[input_df['Genre 3'][0].lower()], c=df['color'])
	plt.xlabel(input_df['Genre 1'][0].lower())
	plt.xlim(0, 1)
	plt.ylabel(input_df['Genre 3'][0].lower())
	plt.ylim(0, 1)
	plt.show()
	st.write(fig_3)
