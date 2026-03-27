import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://books.toscrape.com"  # free practice site
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data
books = []
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    books.append({"Title": title, "Price": price})

# Step 4: Save to CSV
df = pd.DataFrame(books)
df.to_csv("books_dataset.csv", index=False)

print("Done! Dataset saved.")
print(df.head())