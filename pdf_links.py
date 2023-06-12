import requests
from lxml import etree

def find_elements_with_xpath(url, xpath_expression):
    try:
        # Send a GET request to the webpage
        response = requests.get(url)
        response.raise_for_status()
        print(response)

        # Parse the HTML content
        tree = etree.HTML(response.text)
        print(tree)

        # Find elements using XPath expression
        elements = tree.xpath(xpath_expression)
        print(elements)

        return elements

    except Exception as e:
        print(f"Error: {e}")
        return None

# URL of the webpage to scrape
webpage_url = "https://www.sbp.org.pk/ecodata/kibor_index.asp"

# XPath expression to find elements
xpath_expr = '//*[@id="tablediv"]/table/tbody/tr[2]/td[2]/a'

# [contains(@href, ".pdf")]


# Find elements using XPath
result_elements = find_elements_with_xpath(webpage_url, xpath_expr)

if result_elements is not None:
    print(result_elements)
    for element in result_elements:
        print(element.text)
else:
    print("Failed to find elements using XPath.")
