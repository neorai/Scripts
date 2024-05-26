from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import cloudscraper


nvidia_models = [
        # Serie 1000
        "GTX 1050",
        "GTX 1050 Ti",
        "GTX 1060",
        "GTX 1070",
        "GTX 1070 Ti",
        "GTX 1080",
        "GTX 1080 Ti",
        # Serie 1600
        "GTX 1650",
        "GTX 1650 Ti",
        "GTX 1660",
        "GTX 1660 Ti",
        # Serie 2000
        "RTX 2060",
        "RTX 2060 Super",
        "RTX 2070",
        "RTX 2070 Super",
        "RTX 2080",
        "RTX 2080 Super",
        "RTX 2080 Ti",
        # Serie 3000
        "RTX 3060",
        "RTX 3060 Ti",
        "RTX 3070",
        "RTX 3070 Ti",
        "RTX 3080",
        "RTX 3080 Ti",
        "RTX 3090",
        # Serie 4000 (hasta el conocimiento actual en enero de 2022)
        "RTX 4080",
        "RTX 4080 Ti",
        "RTX 4090",
    ]


data = pd.read_csv("pccomponentes.csv")


for index, row in data.iterrows():

                
    print(data.columns)
