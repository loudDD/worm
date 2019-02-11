from requests_html import HTMLSession

session = HTMLSession()

r = session.get("https://news.cnblogs.com/n/recommend")

#通过css找到新闻标签
news = r.html.find('h2.news_entry > a')
for new in news:
    print(new.text)
    print(new.absolute_links)