import requests

def fetch_data(api_url):
    data = []
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        if response.status_code != 200:
            break
        page_data = response.json()
        if not page_data:
            break
        data.extend(page_data)
        page += 1
    return data

api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
data = fetch_data(api_url)
