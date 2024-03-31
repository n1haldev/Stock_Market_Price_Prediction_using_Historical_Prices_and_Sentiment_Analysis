from newsapi import NewsApiClient
import datetime
import csv

# add your api key here from https://newsapi.org/
newsapi = NewsApiClient(api_key='d78ed1ef62f64eb1803611cad5f6e6a9')

query = 'tata motors'
start_date = datetime.date(2023, 9, 15)
end_date = start_date + datetime.timedelta(days=1)
iters=30         # number of iterations is capped at 30 for the free version of the API

# open a csv file to write the date and titles to
with open(query+".csv", mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Date', 'Title'])

    # iterate over the dates
    for i in range(iters):
        all_articles = newsapi.get_everything(q=query,
                                              sources='google-news-in,the-hindu,the-times-of-india,cnn,australian-financial-review,bloomberg,google-news,newsweek,reuters,fortune,financial-post,bbc-news,the-washington-post,the-wall-street-journal,the-washington-times,business-insider,cbc-new,engadget',
                                              from_param=start_date,
                                              to=end_date,
                                              language='en',
                                              sort_by='relevancy',
                                              page=1)
        # print the first 3 articles for each date
        for article in all_articles['articles'][:3]:
            writer.writerow([start_date, article['title']])

        # update the dates for the next iteration
        start_date = end_date
        end_date += datetime.timedelta(days=1)

