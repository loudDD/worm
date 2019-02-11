from requests_html import HTMLSession


session = HTMLSession()
r = session.get("https://python.org")

all_link = r.html.links
for link in all_link:
    print(link)

all_abs_link =r.html.absolute_links
print(all_abs_link)