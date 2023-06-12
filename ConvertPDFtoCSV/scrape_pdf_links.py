import requests
from bs4 import BeautifulSoup

def scrape_pdf_links(url):
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags with href attribute containing ".pdf"
        pdf_links = soup.find_all('a', href=lambda href: href and href.endswith('.pdf'))

        # Extract the href attribute value from each anchor tag
        pdf_urls = [link['href'] for link in pdf_links]

        return pdf_urls

    except Exception as e:
        print(f"Error: {e}")
        return None

# URL of the webpage to scrape
webpage_url = "https://www.sbp.org.pk/ecodata/kibor_index.asp"

# Scrape PDF links
pdf_links = scrape_pdf_links(webpage_url)

if pdf_links is not None:
    for pdf_url in pdf_links:
        print(pdf_url)
else:
    print("Failed to scrape PDF links.")
