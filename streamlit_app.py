import streamlit

streamlit.title('🍞My Parent\'s, New healthy Diner')

streamlit.header('🥣Breakfast MENU')
streamlit.text('🥗Omega 3 and Blueberry Oatmeal')
streamlit.text('🥑Avacado and smoothie')
streamlit.text('🐔Hard boiled Free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
