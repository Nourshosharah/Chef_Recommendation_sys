import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle 
import os




settings_dir = os.path.dirname(__file__)
print(settings_dir)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
print(PROJECT_ROOT)
all_recipes_clean_path = settings_dir + '\\Data\\'
models_path = settings_dir + '\\Data\\model'
print(models_path)



# load in parsed recipe dataset 
df_recipes = pd.read_csv(all_recipes_clean_path+"df_parsed.csv")
print(df_recipes.head())
df_recipes['ingredients_parsed'] = df_recipes["ingredients_parsed"].values.astype('U')

# TF-IDF feature extractor 
tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

# save the tfidf model and encodings 
with open(models_path +"tfidf.pkl", "wb") as f:
    pickle.dump(tfidf, f)

with open(models_path + "tfidf_encodings.pkl", "wb") as f:
    pickle.dump(tfidf_recipe, f)

    

