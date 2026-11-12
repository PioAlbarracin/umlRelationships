class Article:
    def __init__(self, headline: str):
        self.headline = headline

    def __del__(self):
        print(f'Article object destroyed: {self.headline}')

class Publisher:
    def __init__(self, articles: list[Article] = None):
        self.articles = articles if articles else []

    def __del__(self):
        print("Publisher object destroyed")

article1 = Article("News")
article2 = Article("Feature news")

my_Publisher = Publisher([article1, article2])

del my_Publisher
