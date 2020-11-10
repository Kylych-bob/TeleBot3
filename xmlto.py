import requests
import xmltodict

# from bs4 import BeautifulSoup


def get_data(url):
    responce = requests.get(
        url=url
    )
    status_code = responce.status_code
    return responce.text


def main():   
    html = get_data(url='https://www.nbkr.kg/XML/daily.xml')
    my_dict = xmltodict.parse(html)
    # print(my_dict)
    data_currency = {}
    data_currency["date"] = dict(my_dict)["CurrencyRates"]["@Date"]
    for val in dict(my_dict)["CurrencyRates"]["Currency"]:
        d = dict((y, x) for y, x in val.items())
        data_currency[d["@ISOCode"]] = d["Value"]
    print(data_currency)
    print(data_currency["USD"])
    return data_currency




if __name__ == '__main__':
    main()