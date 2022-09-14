import streamlit
import pandas


streamlit.title('Kane''s Diner')
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
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
