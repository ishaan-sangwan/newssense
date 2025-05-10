from newsapi import NewsApiClient
from datetime import timedelta, date

def get_news(keyword):
    current_date = date.today() - timedelta(days=4)
    news = NewsApiClient(api_key='80e08f9fb934402a9c06ef29bcaa2f63')
    top_headlines = news.get_everything(
            q=keyword,
            language='en',
            sort_by='publishedAt',
            from_param=str(current_date)
            )
    return top_headlines

if __name__ == '__main__':
    print(get_news('india and pakistan'))
