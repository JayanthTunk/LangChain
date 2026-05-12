import langchain_helper as lch
import streamlit as st

st.title("Animal Names")

User_Animal_type = st.sidebar.selectbox("What is your pet ? ",  ("Cow", "Cat", "Horse", "Fish"))

if User_Animal_type =="Cow":
    Animal_colour = st.sidebar.text_area(label = "What colour is your cow ?", max_chars=10)

if User_Animal_type =="Cat":
    Animal_colour = st.sidebar.text_area(label = "What colour is your cat ?", max_chars=10)

if User_Animal_type =="Horse":
    Animal_colour = st.sidebar.text_area(label = "What colour is your Horse ?", max_chars=10)

if User_Animal_type =="Fish":
    Animal_colour = st.sidebar.text_area(label = "What colour is your Fish ?", max_chars=10)

if Animal_colour:
    response = lch.generate_bike_name(User_Animal_type, Animal_colour)
    st.text(response["Animal_names"])