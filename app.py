import streamlit as st

st.title("Hello, World!")
st.write("Welcome to your first Streamlit app.")

# add a button to take input from the user
name = st.text_input("Enter your name", "Type here ...")