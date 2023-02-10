import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('🍞My Parent\'s, New healthy Diner')

streamlit.header('🥣Breakfast MENU')
streamlit.text('🥗Omega 3 and Blueberry Oatmeal')
streamlit.text('🥑Avacado and smoothie')
streamlit.text('🐔Hard boiled Free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Indexing by fruit names
my_fruit_list = my_fruit_list.set_index('Fruit')

## Let's put a pick list here so they can pick the fruit they want to include 
fruits_filter = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_filter]

# Display the table on the page. (full or filtered)
streamlit.dataframe(fruits_to_show)

#create repeatable code block (FUNCTION)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()

#don't run anything past here 
streamlit.stop()

#query META DATA of trial account
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The FRUIT LOAD LIST TABLE contains:")
streamlit.dataframe(my_data_row)

#allow user to add a fruit to list
add_new_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding ', add_new_fruit)

#initally won't work as expected
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
