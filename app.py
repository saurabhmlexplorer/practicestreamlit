import streamlit as st
from streamlit_option_menu import option_menu

st.header("Learning")
st.write("Creating navigation bar")

'''
# Sidebar menu (Commented out)
with st.sidebar: 
    selected1 = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
    )

if selected1 == "Home":
    st.title(f"You have selected {selected1}")
if selected1 == "Projects":
    st.title(f"You have selected {selected1}")
if selected1 == "Contact":
    st.title(f"You have selected {selected1}")
'''

# Horizontal menu
selected2 = option_menu(
    menu_title="Main Menu",
    options=["Home", "Projects", "Contact"],
    icons=["house", "book", "envelope"],  # Fixed icon name
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",  # Fixed spelling
)

if selected2 == "Home":
    st.title(f"You have selected {selected2}")
if selected2 == "Projects":
    st.title(f"You have selected {selected2}")
if selected2 == "Contact":
    st.title(f"You have selected {selected2}")
