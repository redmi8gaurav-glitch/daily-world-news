import requests
import os
from datetime import datetime, timedelta

API_KEY = os.getenv('NEWS_API_KEY')
EMAIL = os.getenv('EMAIL')

# Get current time in IST
now = datetime.utcnow() + timedelta(hours=5, minutes=30)
start_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
end_time = now

# Convert to UTC for API
start_utc = (start_time - timedelta(hours=5, minutes=30)).isoformat().split('T')[0]
end_utc = (end_time - timedelta(hours=5, minutes=30)).isoformat().split('T')[0]

# Fetch news
url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'world news',
    'sortBy': 'publishedAt',
    'language': 'en',
    'from': start_utc,
    'to': end_utc,
    'apiKey': API_KEY,
    'pageSize': 10
}

print("=" * 80)
print("WORLD NEWS FETCH")
print("=" * 80)
print(f"Time Range: {start_time.strftime('%Y-%m-%d %H:%M IST')} to {end_time.strftime('%Y-%m-%d %H:%M IST')}")
print(f"Email: {EMAIL}")
print("=" * 80)

response = requests.get(url, params=params)
data = response.json()

if data.get('status') == 'ok':
    articles = data.get('articles', [])
    print(f"\n✓ Successfully fetched {len(articles)} articles\n")
    
    for idx, article in enumerate(articles[:10], 1):
        print(f"{idx}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Date: {article['publishedAt'][:10]}")
        print(f"   URL: {article['url']}\n")
else:
    error_msg = data.get('message', 'Unknown error')
    print(f"\n✗ Error: {error_msg}\n")

print("=" * 80)
