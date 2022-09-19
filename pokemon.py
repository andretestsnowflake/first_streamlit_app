import streamlit
import pandas

streamlit.title('POKEMON Finder')
import requests

# put choice into variable
Pokemon_name_search = streamlit.text_input('Which POKEMON you are looking for?','Charizar')

q="!name:Charizar"
Search_response = requests.get("https://api.pokemontcg.io/v2/cards/"+q)
Pokemon_data_normalized = pandas.json_normalize(Search_response.json())
streamlit.dataframe(Pokemon_data_normalized)

