import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('Pekan Diner')
streamlit.header('Herkku-Breakfast')
streamlit.text('🥣 Kaurapuuro')
streamlit.text('🥗 Pinatti-smoothie')
streamlit.text('🐔 Keitetty kananmuna')
streamlit.text('🥑🍞 Avocado-Paahtis')

# streamlit.text('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New section to Api response
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# put json to df
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write df
streamlit.dataframe(fruityvice_normalized)

# xxxxxxxxxxxxxxxxxxxxxxxx
streamlit.stop()

# Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit load list:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
