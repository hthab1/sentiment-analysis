import nltk
from textblob import TextBlob
from newspaper import Article
# import ssl

# # Ignore SSL certificate verification errors
# ssl._create_default_https_context = ssl._create_unverified_context

# # Download the missing NLTK resource
# nltk.download('punkt')

# url = "https://www.9news.com.au/world/julie-seed-death-adelaide-mother-death-prompts-calls-to-fix-broken-system/6ccc476c-de96-45f4-9f2f-39506bc8181d"

# article = Article(url)

# article.download()
# article.parse()
# article.nlp()

# text = article.summary
# print(text)

with open("mytext.txt", "r") as f:
    text = f.read()

blob= TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)