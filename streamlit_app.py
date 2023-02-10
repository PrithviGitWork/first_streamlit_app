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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# JSON response is normalized  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

import snowflake.connector
# convert the result into a table
streamlit.dataframe(fruityvice_normalized)

#query META DATA of trial account
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
