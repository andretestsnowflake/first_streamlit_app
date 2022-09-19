import streamlit
import pandas
import cards
streamlit.title('POKEMON Finder')
import requests

# put choice into variable
Pokemon_name_search = streamlit.text_input('Which POKEMON you are looking for?','Charizar')
api_key="1b7fbe88-8707-4a11-bde2-b47ddcec5c10"
q="!name:Charizar"
card = Card.find('xy10-117')
Search_response = requests.get("https://api.pokemontcg.io/v2/cards/"+card)
Pokemon_data_normalized = pandas.json_normalize(Search_response.json())
streamlit.dataframe(Pokemon_data_normalized)

