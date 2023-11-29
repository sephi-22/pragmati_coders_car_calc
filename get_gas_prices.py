import requests
from bs4 import BeautifulSoup

# Assuming your HTML content is stored in the 'html_content' variable
def scrape_for_gas_prices(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/101.0.4951.54 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'https://google.com',
        'DNT': '1',
        'Accept-Language': 'en-GB,en;q=0.5'
    }
    url = "https://gasprices.aaa.com/state-gas-price-averages/"
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the table containing gas prices
        gas_table = soup.find('table', {'id': 'sortable'})

    # Find the rows within the table body
        rows = gas_table.find('tbody').find_all('tr')

    # Dictionary to store gas prices for all states
        gas_prices = {}

    # Loop through the rows to find and store gas prices for each state
        for row in rows:
        # Extract the state name
            state = row.find('td').text.strip()

        # Extract prices for each fuel type
            regular_price = row.find('td', {'class': 'regular'}).text.strip()[1:]
            mid_grade_price = row.find('td', {'class': 'mid_grade'}).text.strip()[1:]
            premium_price = row.find('td', {'class': 'premium'}).text.strip()[1:]
            diesel_price = row.find('td', {'class': 'diesel'}).text.strip()[1:]

        # Create a sub-dictionary for the state
            state_prices = {
                'regular': regular_price,
                'mid_grade': mid_grade_price,
                'premium': premium_price,
                'diesel': diesel_price
            }

        # Store the sub-dictionary in the main dictionary
            gas_prices[state] = state_prices
    return gas_prices