from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

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

def find_citations(data):
    citations = []
    for item in data:
        response_text = item['response']
        sources = item['sources']
        cited_sources = []
        for source in sources:
            if source['context'] in response_text:
                cited_sources.append(source)
        citations.append({
            'response': response_text,
            'citations': cited_sources
        })
    return citations

def index(request):
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)
    citations = find_citations(data)
    return render(request, 'index.html', {'citations': citations})

def api_citations(request):
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)
    citations = find_citations(data)
    return JsonResponse(citations, safe=False)