import get_a_pet.langchain_helper as lch
import streamlit as st

st.title("Expensive pets")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Horse"))

if animal_type == "Cat":
    price_point = st.sidebar.text_area(label="How much do you have?", max_chars=15)

if animal_type == "Dog":
    price_point = st.sidebar.text_area(label="How much do you have?", max_chars=15)

if animal_type == "Horse":
    price_point = st.sidebar.text_area(label="How much do you have?", max_chars=15)

if price_point:
    response = lch.generate_expensive_breed(animal_type, price_point)
    st.text(response["pet_name"])
