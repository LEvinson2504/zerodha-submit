import requests


def scrape_bse():
    url = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
    headers = {'Accept-Encoding': 'deflate'}
    res = requests.get(url, headers=headers)
    print(res.text)
    # print("Im working now")
