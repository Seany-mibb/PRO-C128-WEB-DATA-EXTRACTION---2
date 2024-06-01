from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

all_tables = []

browser = webdriver.Edge()

def scrape(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content, "html.parser")
    all_tables = soup.find("table", attrs={"class", "wikitable sortable jquery-tablesorter"})
    all_rows = all_tables.find_all("tr")

    listables = []

    for i in all_rows:
        try:
            table_columns = soup.find("td", text=i).strip()
            listables.append(table_columns)
        except:
            table_columns.append("Unkown")

empty_list = []

headers = ["star_name", "radius", "mass", "distance"]
new_planet_df_1 = pd.DataFrame(new_planets_data,columns = headers)
new_planet_df_1.to_csv('C-128Web_Scrapping2.csv',index=True, index_label="id")