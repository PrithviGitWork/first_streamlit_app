import streamlit

streamlit.title('🍞My Parent\'s, New healthy Diner')

streamlit.header('🥣Breakfast MENU')
streamlit.text('🥗Omega 3 and Blueberry Oatmeal')
streamlit.text('🥑Avacado and smoothie')
streamlit.text('🐔Hard boiled Free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Indexing by fruit names
my_fruit_list = my_fruit_list.set_index('Fruit')

## Let's put a pick list here so they can pick the fruit they want to include 
fruits_filter = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_filter]

# Display the table on the page. (full or filtered)
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# JSON response is normalized  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# convert the result into a table
streamlit.dataframe(fruityvice_normalized)
