import streamlit
#Imported Panda package
import pandas
import requests
import snowflake.connector

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


#New Section to Display fruityvise api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice= streamlit.text_input('What fruit would you llike information about? ', 'kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())


# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list")

my_data_rows = my_cur.fetchall()

streamlit.header("The Fruit Load List contains: ")
streamlit.dataframe(my_data_rows)

streamlit.text(my_data_row)
