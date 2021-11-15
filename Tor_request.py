from torrequest import TorRequest

with TorRequest() as tr:
    response = tr.get('https://www.barnesandnoble.com/h/books/browse')
    print(response.text)


# import requests
#
# proxies = {
#     'http': 'socks5://127.0.0.1:9050',
#     'https': 'socks5://127.0.0.1:9050'
# }
# url = 'https://www.barnesandnoble.com/h/books/browse'
# r = requests.get(url, proxies=proxies)
# print(r.headers)
