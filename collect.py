import os
import csv
from bs4 import BeautifulSoup

data_folder = "data"

products = []

for file in os.listdir(data_folder):

    if not file.endswith(".html"):
        continue

    file_path = os.path.join(data_folder, file)

    with open(file_path, encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    items = soup.select(".s-card-container")

    for item in items:

        # TITLE
        title_tag = item.select_one("h2 span")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        # LINK
        link = "N/A"
        link_tag = item.select_one("a.a-link-normal.s-no-outline")

        if link_tag and link_tag.get("href"):
            link = "https://www.amazon.in" + link_tag.get("href")

        # PRICE
        price_tag = item.select_one(".a-price-whole")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        # RATING
        rating_tag = item.select_one(".a-icon-alt")
        rating = rating_tag.get_text(strip=True).split()[0] if rating_tag else "N/A"

        print(title, price, rating)

        products.append([title, price, rating, link])


# SAVE CSV
with open("amazon_products.csv", "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow(["Title", "Price", "Rating", "Link"])

    writer.writerows(products)

print("CSV file created successfully!")