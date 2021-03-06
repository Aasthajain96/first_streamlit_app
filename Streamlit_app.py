import streamlit
#Imported Panda package
import pandas
import requests
import snowflake.connector
#we'll need to use this in our Control of flow changes.
from urllib.error import URLError

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

# ******************************************************
# Creating a Funcation called "get_fruiytvice_data"
# ******************************************************

def get_fruityvice_data(this_fruit_choice):
    #streamlit.write('The user entered',fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)

    # take the json version of the response and normalize it
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized



#New Section to Display fruityvise api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice= streamlit.text_input('What fruit would you llike information about?')
  if not fruit_choice:
    streamlit.error("Please select afruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error("ERROR AAYA",e)
    


# don't run anything past here while we troubleshoot
#streamlit.stop()

# ***********************************************************************************************
# Creating a Funcation called "get_fruit_load_list" to get a list item in fruit_load_list table
# ***********************************************************************************************

streamlit.header("View our Fruit List - Add your Favorites! ")
# Snowflake-related function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list() 
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
    

#streamlit.text(my_data_rows)

# Function and Button to Add the fruit name to submissiom
# Allow end user to add a fruit to the list
def insert_row_to_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
        return "Thanks for adding "+new_fruit
 
add_my_fruit= streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to a list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_to_snowflake(add_my_fruit)  
    my_cnx.close()
    streamlit.text(back_from_function)
    
    
    
#streamlit.write('The user entered',add_my_fruit)
