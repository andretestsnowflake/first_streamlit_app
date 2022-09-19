import streamlit
import pandas

streamlit.title('My Parents Healthy new Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#load list from csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#select fruits
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#show the table
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
import requests
# put choice into variable
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
# use variable to select data
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# bring data into table format
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display data
streamlit.dataframe(fruityvice_normalized)
