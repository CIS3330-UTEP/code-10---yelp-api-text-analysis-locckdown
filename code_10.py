import pandas as pd
from yelpapi import YelpAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key = 'Y0lVqprx4U-GuHAkhnDg_JKzfkDrDxDjHKno8cNOYnQHLSvS2dI7y-KtILRLIDaP20f57bQx0vW84eJll1RDsCAivXBbiB5Z1OuMkO7PFmkqHV9bNcfZOX-kud1MZXYx'
yelp_api = YelpAPI(api_key)
search_term = "sushi"
cities = "El Paso, TX", "Horizon City, TX"
location_term = cities
analyzer = SentimentIntensityAnalyzer()
df = pd.DataFrame()
alias = ()
review_text = ()
search_results = yelp_api.search_query(
        term=search_term, location=location_term,
        sort_by='rating', limit=20)

for item in search_results('businesses'):
    review_return = yelp_api.reviews_query(id=item.get(alias))
    for review in review_return('reviews'):
        alias.append(item.get(alias))
        review_text.append(review.get('text'))
data = {"Alias": alias, "Review": review_text}
df = pd.DataFrame(pd.DataFrame.from_dict(data))

for review in df('Review'):
    print(review)
    sentiment = analyzer.polarity_scores(review)
    print(sentiment)

