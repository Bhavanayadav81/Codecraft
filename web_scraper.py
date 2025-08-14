import requests
from bs4 import BeautifulSoup
import csv

# Target URL (Practice site for scraping)
url = "http://books.toscrape.com/catalogue/page-1.html"

# CSV file setup
filename = "products.csv"
fields = ["Title", "Price", "Availability"]

# Open CSV file for writing
with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)

    # Loop through multiple pages
    for page in range(1, 6):  # scrape first 5 pages
        page_url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all product listings
        products = soup.find_all("article", class_="product_pod")
        
        for product in products:
            title = product.h3.a["title"]
            price = product.find("p", class_="price_color").text
            availability = product.find("p", class_="instock availability").text.strip()

            writer.writerow([title, price, availability])

print(f"✅ Scraping completed! Data saved to {filename}")
