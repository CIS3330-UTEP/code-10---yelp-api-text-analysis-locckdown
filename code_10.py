import pandas as pd
from yelpapi import YelpAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = 'Y0lVqprx4U-GuHAkhnDg_JKzfkDrDxDjHKno8cNOYnQHLSvS2dI7y-KtILRLIDaP20f57bQx0vW84eJll1RDsCAivXBbiB5Z1OuMkO7PFmkqHV9bNcfZOX-kud1MZXYx'
yelp_api = YelpAPI(api_key)
search_term = "sushi"
city = "El Paso, TX"
location_term = city
analyzer = SentimentIntensityAnalyzer()
df = pd.DataFrame(columns=["Name", "Alias", "Review"])

search_results = yelp_api.search_query(
        term=search_term, location=location_term,
        sort_by='rating', limit=20)

for item in search_results['businesses']:
    business_name = item['name']
    review_response = yelp_api.reviews_query(id=item['alias'])
    compound_sentiments = []
    print(f"Restaurant: {business_name}")
    for review in review_response['reviews']:
        review_text = review['text']
        print(f"Review: {review_text}")
        sentiment = analyzer.polarity_scores(review_text)
        compound_sentiments.append(sentiment['compound'])
        df = df._append({"Name": business_name, "Alias": item['alias'], "Review": review['text']}, ignore_index=True)
    
    average_sentiment_for_each = sum(compound_sentiments) / len(compound_sentiments) if compound_sentiments else 0
    print(f"Average Compound Sentiment: {average_sentiment_for_each}")
    print("\n")


