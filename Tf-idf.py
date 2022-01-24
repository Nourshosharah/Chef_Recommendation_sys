import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import os
import config



# settings_dir = os.path.dirname(__file__)
# PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
# all_recipes_clean_path = settings_dir + '\\Data\\'
# models_path = settings_dir + '\\Data\\model'
# print(models_path)



# load in parsed recipe dataset 
df_recipes = pd.read_csv(config.PARSED_PATH)
print(df_recipes.head())
df_recipes['ingredients_parsed'] = df_recipes["ingredients_parsed"].values.astype('U')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

# save the tfidf model and encodings 
with open(config.TFIDF_MODEL_PATH, "wb") as f:
    pickle.dump(tfidf, f)

with open(config.TFIDF_ENCODING_PATH, "wb") as f:
    pickle.dump(tfidf_recipe, f)

    

