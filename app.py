import streamlit as st
from streamlit_option_menu import option_menu

st.header("Learning")
st.write("Creating navigation bar")

# 1. as sidebar menu
with st.sidebar: 
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "Projects", "Contact"],
  )

if selected == "Home":
  st.title(f"You have selected {selected}")
if selected == "Projects":
  st.title(f"You have selected {selected}")
if selected == "Contact":
  st.title(f"You have selected {selected}")


# 2. as horizontal menu
with st.sidebar: 
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home", "Projects", "Contact"],
    icons = ["house", "book", "envelop"],
    menu_icon = "cast",
    default_index = 0,
    orinetation = "horizontal",
  )

if selected == "Home":
  st.title(f"You have selected {selected}")
if selected == "Projects":
  st.title(f"You have selected {selected}")
if selected == "Contact":
  st.title(f"You have selected {selected}")
