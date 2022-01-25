# from flask import   render_template
from flask import Flask, jsonify , request
import json, requests, pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity  
from Cleaning_Data import ingredient_parser
import config, recommender_sys

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return "Please add some ingredients to the url to receive recipe recommendations"


@app.route('/recipe', methods=["GET"])
def recommend_recipe():
    ingredients = request.args.get('ingredients')   
    recipe = recommender_sys.RecSys(ingredients)
    
    response = {}
    count = 0
    for index, row in recipe.iterrows():
        response[count] = {
            'recipe': str(row['recipe']),
            'score': str(row['score']),
            'ingredients': str(row['ingredients']),
            'url': str(row['url'])
        }
        count += 1
    return jsonify(response)
   

if __name__ == "__main__":
    app.run()


#run in http://127.0.0.1:5000/recipe?ingredients=%20pasta%20tomato%20onion 
