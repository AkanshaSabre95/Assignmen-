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

citations = find_citations(data)
