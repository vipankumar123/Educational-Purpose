# Full Website Scrapping
# pip install requests beautifulsoup4 urllib3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time


def get_internal_links(base_url):
    try:
        respose = requests.get(base_url, timeout=10)
        respose.raise_for_status()
        soup = BeautifulSoup(respose.text, "html.parser")

        links = set()
        for link in soup.find_all("a", href=True):
            full_url = urljoin(base_url, link['href'])
            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                links.add(full_url)
        return links

    except Exception as e:
        print("error is: ", e)
        return set()
    
def scrape_page_text(url):
    try:
        respose = requests.get(url, timeout=10)
        respose.raise_for_status()
        soup = BeautifulSoup(respose.text, "html.parser")

        # Extract text content
        page_text = soup.get_text(separator='\n', strip=True)

        return page_text
    except Exception as e:
        print("error is: ", e)
        return ""

base_url = "https://thegymlife.com/"

all_links = get_internal_links(base_url)

print(f"total links found :  {len(all_links)}")
print(f"total links found :  {(all_links)}")


scraped_data = []
for idx, link in enumerate(all_links):
    print(f"[{idx+1}]/{len(all_links)} scrapping: {link}")
    page_text = scrape_page_text(link)

    scraped_data.append(f"Url: {link}\n\n {page_text}\n{'='*80}\n")

    time.sleep(1)

with open("gym.txt", "w", encoding="utf-8") as file:
    file.writelines(scraped_data)

print("scrapping completed!!")

