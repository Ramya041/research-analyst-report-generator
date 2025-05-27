import requests

SERPER_API_KEY = "your_serper_api_key"

def google_search(query):
    url = "https://google.serper.dev/search"  # Correct endpoint
    headers = {"X-API-KEY": SERPER_API_KEY}
    params = {"q": query}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("✅ Serper API Request Sent")
        return response.json()
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None

search_results = google_search("Latest AI news")
print(search_results)
