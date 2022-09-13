import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Kane''s Diner')
streamlit.header('Herkku-Breakfast')
streamlit.text('🥣 Kaurapuuro')
streamlit.text('🥗 Pinatti-smoothie')
streamlit.text('🐔 Keitetty kananmuna')
streamlit.text('🥑🍞 Avocado-Paahtis')

# streamlit.text('\N{flexed biceps} Breakfast of Champion Coders \N{flexed biceps}')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
