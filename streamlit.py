import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

from recommender_sys import RecSys
from Cleaning_Data import ingredient_parser

import nltk
def make_clickable(name, link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = name
    return f'<a target="_blank" href="{link}">{text}</a>'



    
    

# try:
#     nltk.data.find("corpora/wordnet")
# except LookupError:
#     nltk.download("wordnet")
def replace(text,link):
    return  st.write([text](link))
image = Image.open("Data/cook-jd-640x230.jpg")
st.image(image)
st.markdown("# *What's Cooking? :cooking:*")


st.markdown(
    "## Given a list of ingredients, what different recipes can I can make? :tomato: "
)
st.markdown(
    "For example, what recipes can you make with the ingredients ypu have ? :house: My web app  will look through over 4500 recipes to find matches for you... :mag: "
)

st.text("")

st.write("for more details and look in deep check out this [link](https://github.com/Nourshosharah/Chef_Recommendation_sys)")


ingredients = st.text_input( "Enter ingredients you would like to cook with (seperate ingredients with a comma)",
        "onion, chorizo, chicken thighs, paella rice, frozen peas, prawns",)

if st.button("Give me recommendations!"):
    # st.error(
    # 'According to our Calculations, you will not get the loan from Bank'
    # )
    col1, col2, col3 = st.beta_columns([1, 6, 1])
    with col2:
        gif_runner = st.image("Data/gitrunner.gif")
    
    recipe = RecSys(ingredients)
    gif_runner.empty()
            # recipe["url"] = recipe["url"].apply(replace(recipe["recipe"] ,recipe["url"] ))

    recipe["url"] = recipe.apply(
                lambda row: make_clickable(row["recipe"], row["url"]), axis=1
            )
        #     recipe_df["ingredients_parsed"] = recipe_df["ingredients"].apply(
        #     lambda x: ingredient_parser(x)
        # )`



    recipe_display = recipe[["recipe","ingredients","url"]]
    # recipe_display["url"] = recipe_display.apply(
    #         lambda row: make_clickable(row["recipe"], row["url"]), axis=1
    #     )
    recipe_display = recipe_display.to_html(escape=False)
    # recipes = recipe.recipe.values.tolist()
    st.write(recipe_display, unsafe_allow_html=True)
