import requests

# Function to extract data from Alpha Vantage API
def extract_data():
    api_key = ''
    symbol = 'AAPL'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data


# Test the extract_data function
if __name__ == "__main__":
    data = extract_data()
    print(data)
