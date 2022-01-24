import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os
import pandas as pd


settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
url_recipes_file_path = PROJECT_ROOT + '\\Data\\url_recipes.csv'
all_recipes_file_path = PROJECT_ROOT + '\\Data\\'



#scrap all ingrediendts and recipes names 
def get_recipe_details(url):
    data=requests.get(url).text
    soup=BeautifulSoup(data) 
    ingredients_list = [] 
    for li in soup.select('.ingred-list li'):
        ingred = ' '.join(li.text.split())
        ingredients_list.append(ingred)
    ingredients=ingredients_list
    recipe_name=soup.find('h1').text.strip()
    return {
            'recipe_name':recipe_name,
            'ingrediendts':[ingredients]}

url_recipes=pd.read_csv(url_recipes_file_path)
# loop over url_recipes_file_path dataset to scrap ingrediendts and recipes names
df= pd.DataFrame()
for i in range(0,len(url_recipes['recipe_urls'])):
    print(i)
    url=url_recipes["recipe_urls"][i]
    new_df = pd.DataFrame(get_recipe_details(url),index=[0])
    df = pd.concat([df,new_df],ignore_index=True)



#put in all in one dataset
attribs = ['recipe_name', 'ingredients']
df['recipe_urls'] = url_recipes['recipe_urls']
columns = ['recipe_urls'] + attribs
df = df[columns]

all_recipes_df = df
all_recipes_df.to_csv(all_recipes_file_path+"all_recipes_df.csv", index=False)











