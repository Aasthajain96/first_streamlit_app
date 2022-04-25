import streamlit
#Imported Panda package
import pandas

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Plain Sandwich')
streamlit.text('Orange & Veg Sandwich')
streamlit.text('Paratha with Curd & Lassi')
streamlit.text('Avocado Sandwich')

streamlit.header('Build your own fruit smoothie')

#using panda func to read csv file and storing it to my_fruit_list dataframe
my_fruit_list  = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#using set index we are converting index from numbers to fruits
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put up a list here so that they can pick up the fruit they want to include
fruits_selected = streamlit.multiselect('pickup fruits for your smoothie :',list(my_fruit_list.index),['Avocado','Strawberries'])

#picking the selected fruit from the whole fruit list ie. my_fruit_list
fruits_to_show = my_fruit_list.loc[fruits_selected]

#displaying the content of our dataframe 'my_fruit_list'
streamlit.dataframe(fruits_to_show)


import requests
from requests.exceptions import ConnectionError
#new section to display fruityvise api response
try:
   fruityvise_response =requests.get("https://fruityvise.com/api/fruit/watermelon")

except ConnectionError as e:    # This is the correct syntax
   print e
   r = "No response"
#streamlit.text(fruityvise_reponse)
