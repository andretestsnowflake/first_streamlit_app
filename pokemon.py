import streamlit
import pandas

streamlit.title('POKEMON Finder')
import requests

# put choice into variable
Pokemon_name_search = streamlit.text_input('Which POKEMON you are looking for?','Charizar')

streamlit.write('The user entered ', Pokemon_name_search)
Search_response = requests.get("https://api.pokemontcg.io/v2/cards/!name:Charizar")
Pokemon_data_normalized = pandas.json_normalize(Search_response.json())
streamlit.dataframe(Pokemon_data_normalized)
streamlit.dataframe(Search_response)
