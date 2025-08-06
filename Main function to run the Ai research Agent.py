agent = AIResearchAgent(api_key, service_url)

# Example operations
paper_text = "Full text of the research paper goes here."
summary = agent.generate_summary(paper_text)
print("Summary:", summary)

current_topic = "Machine Learning"
recommendations = agent.recommend_papers(current_topic)
print("Recommended Papers:", recommendations)

paper_id = "12345"
citation_analysis = agent.analyze_citations(paper_id)
print("Citation Analysis:", citation_analysis)

query = "Recent advancements in AI"
search_results = agent.perform_semantic_search(query)
print("Search Results:", search_results)