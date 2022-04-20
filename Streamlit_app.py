import streamlit
import panda
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Plain Sandwich')
streamlit.text('Orange & Veg Sandwich')
streamlit.text('Paratha with Curd & Lassi')
streamlit.text('Avocado Sandwich')

streamlit.header('Build your own fruit smoothie')


my_fruit_list  = panda.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
