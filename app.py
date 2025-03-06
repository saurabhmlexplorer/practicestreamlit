import streamlit as st
from streamlit_option_menu import option_menu

st.header("Learning")
st.write("Creating navigation bar")

'''
# 1. as sidebar menu
with st.sidebar: 
  selected1 = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "Projects", "Contact"],
  )

if selected1 == "Home":
  st.title(f"You have selected {selected1}")
if selected1 == "Projects":
  st.title(f"You have selected {selected1}")
if selected1 == "Contact":
  st.title(f"You have selected {selected1}")
'''

# 2. as horizontal menu
# with st.sidebar: 
selected2 = option_menu(
  menu_title = "Main Menu",
  options = ["Home", "Projects", "Contact"],
  icons = ["house", "book", "envelop"],
  menu_icon = "cast",
  default_index = 0,
  orinetation = "horizontal",
)

if selected2 == "Home":
  st.title(f"You have selected {selected2}")
if selected2 == "Projects":
  st.title(f"You have selected {selected2}")
if selected2 == "Contact":
  st.title(f"You have selected {selected2}")
