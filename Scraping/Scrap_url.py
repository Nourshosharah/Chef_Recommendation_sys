import requests
from bs4 import BeautifulSoup
import pandas as pd 
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
url_recipes_file_path = PROJECT_ROOT + '\\Data'

print(url_recipes_file_path)
url="https://www.jamieoliver.com/recipes/category/course/mains/"
resp = requests.get(url)
data = resp.text
soup = BeautifulSoup(data)


def all_recipes(url):
    data=requests.get(url)
    soup=BeautifulSoup(data.text)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links
 


links=all_recipes(url)

new=[]
for link in links:
    if (link.startswith("/recipes/")) & (link.__contains__("-recipes/")) &  (not link.endswith("recipes/"))  :
        new.append("https://www.jamieoliver.com" + link)
print(new[0:10])
df=pd.DataFrame({"recipe_urls":new})
print(df.head())




df.to_csv(url_recipes_file_path +"url_recipes.csv", index=False)

