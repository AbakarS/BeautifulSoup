import json
import requests
from bs4 import BeautifulSoup
import pandas as pd



 # Pour mieix extraire les citations, l'autheur et les tags on va effectuer une boucle
def extract_data(div_citations):
        
        # Stocker la premiere citation. Comme nous voulons recuperer le texte
        # en utilisant la méthiode get_text() sur les éléments
        
        nom=div_citations.find("h3").get_text()
        prix=div_citations.find("span", {"class":"price"}).get_text()
        prix=prix[1:len(prix)]
       
        #print(citations, author, tags)
        # Nous voulons associer des éléments. Donc, pour associer des éléments en pYTHON
        # l'élément le plus simple c'est le dictionnaire 
        data= {
        "nom":nom,
        "prix" : prix,
        

        }

        return data


def getquotes(pageURL):
    page=requests.get(pageURL)
    parsedPag_Url=BeautifulSoup(page.content, "lxml")
    citations_urls=parsedPag_Url.find_all("div", {"class":"collection_desc clearfix"})
    if len(citations_urls)>0:
        citations_list = [extract_data(citation) for citation in citations_urls]
        return citations_list
    else:
        return None



data = getquotes('http://formation-data.com/?product_cat=women')
for i in range(2,100):
    print(i)
    
    page_url = f'http://formation-data.com/?product_cat=women&paged={i}'
    current_page_quotes = getquotes(page_url)
    if current_page_quotes is not None:
        data = data + current_page_quotes
    else:
        break

data_pd=pd.DataFrame(data)

#print(data_pd.head(20))

data_pd.to_csv("C:/Users/HP/OneDrive/Bureau/Web_Scraping/cours_extract_price_complet.csv")