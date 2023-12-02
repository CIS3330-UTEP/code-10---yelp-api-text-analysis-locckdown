import pandas as pd
from yelpapi import YelpAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = 'Y0lVqprx4U-GuHAkhnDg_JKzfkDrDxDjHKno8cNOYnQHLSvS2dI7y-KtILRLIDaP20f57bQx0vW84eJll1RDsCAivXBbiB5Z1OuMkO7PFmkqHV9bNcfZOX-kud1MZXYx'
yelp_api = YelpAPI(api_key)
search_term = "sushi"
cities = "El Paso, TX"
location_term = cities
analyzer = SentimentIntensityAnalyzer()
df = pd.DataFrame(columns=["Alias", "Review"])

search_results = yelp_api.search_query(
        term=search_term, location=location_term,
        sort_by='rating', limit=20)

for item in search_results['businesses']:
    review_response = yelp_api.reviews_query(id=item['alias'])
    for review in review_response['reviews']:
        df = df._append({"Alias": item['alias'], "Review": review['text']}, ignore_index=True)

for index, row in df.iterrows():
    name = row['Name']
    review = row['Review']
    print(f"Restaurant: {name}")
    print(f"Review: {review}")
    sentiment = analyzer.polarity_scores(review)
    print(f"Sentiment: {sentiment}")

