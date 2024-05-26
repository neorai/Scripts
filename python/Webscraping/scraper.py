from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import cloudscraper

# returns a CloudScraper instance
scraper = cloudscraper.create_scraper()


def set_to_csv(gpu_info, csv):
    csv += ".csv"
    split_data = [item.split(";") for item in gpu_info]
    names = [item[0].strip() for item in split_data]
    prices = [float(item[1].strip()) for item in split_data]

    # Crear un DataFrame usando Pandas
    df = pd.DataFrame({"Product": names, "Price": prices})

    # Guardar en un archivo CSV
    df.to_csv(csv, index=False, sep=";")


def scrap(url):
    gpu_info = set()
    num = 1
    match url:
        case "coolmod":
            while num < 50:
                coolmod_url = f"https://www.coolmod.com/tarjetas-graficas/?pagina={num}"
                html_content = scraper.get(coolmod_url)
                soup = BeautifulSoup(html_content.text, "lxml")
                elements = soup.find_all(name="a", attrs={"data-itemname": True})
                if len(elements) == 0:
                    break
                for element in elements:
                    gpu_info.add(
                        element.get("data-itemname")
                        + ";"
                        + element.get("data-itemprice")
                    )
                sleep(1)
                print(num)
                num += 1
                set_to_csv(gpu_info, url)
            return gpu_info
        case "pccomponentes":
            while num < 50:
                if num == 1:
                    pccomponentes_url = (
                        f"https://www.pccomponentes.com/tarjetas-graficas"
                    )
                else:
                    pccomponentes_url = (
                        f"https://www.pccomponentes.com/tarjetas-graficas?page={num}"
                    )
                html_content = scraper.get(pccomponentes_url)
                soup = BeautifulSoup(html_content.text, "lxml")
                elements = soup.find_all(
                    name="a", attrs={"title": True, "data-product-price": True}
                )
                if len(elements) == 0:
                    break
                for element in elements:
                    gpu_info.add(
                        element.get("title") + ";" + element.get("data-product-price")
                    )
                sleep(1)
                print(num)
                num += 1
                set_to_csv(gpu_info, url)
            return gpu_info
        case "neobyte":
            neobyte_url = "https://www.neobyte.es/tarjetas-graficas-111?order=product.position.asc&resultsPerPage=9999999s"
            html_content = scraper.get(neobyte_url)
            soup = BeautifulSoup(html_content.text, "html.parser")
            for product in soup.find_all("div", class_="product-description"):
                title = product.find("span", class_="h3 product-title").text
                price = product.find("span", class_="product-price")["content"]
                gpu_info.add(title + ";" + price)
                set_to_csv(gpu_info, url)
            return gpu_info
        case _:
            return "error"


scrap("coolmod")
scrap("pccomponentes")
scrap("neobyte")
