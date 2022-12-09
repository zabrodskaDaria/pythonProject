import requests
from bs4 import BeautifulSoup
import time


class Currency():
    DOLLAR_BYR = 'https://www.google.by/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA%D1%83%D1%80%D1%81&sxsrf=ALiCzsYDlnS10jVr531iVMWgIITiQ2j3sg%3A1670489316993&ei=5KSRY-KePLL5qwH65KW4CA&oq=%D0%B4%D0%BE%D0%BB%D0%BB&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgCMgoIABCxAxCDARBDMgcIABCxAxBDMgcIABCxAxBDMgQIABBDMgQIABBDMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMggILhCABBCxAzILCAAQgAQQsQMQgwE6BwgjEOoCECc6DAgAEOoCELQCEEMYAToSCC4QxwEQ0QMQ6gIQtAIQQxgBOgQIIxAnOggIABCxAxCDAToLCC4QgAQQxwEQ0QM6EQguEIAEELEDEIMBEMcBENEDOgoIABAKEAEQQxAqOgcILhDUAhBDOgoIABCABBCHAhAUOgcIABCABBAKOgkIABCABBAKEAE6DQguEIAEEMcBEK8BEAo6CAguELEDEIMBOggIABCABBCxAzoFCC4QgAQ6DgguEIAEELEDEMcBENEDOgcILhBDEOoEOgQILhBDOgsILhCABBCxAxCDAToSCC4QQxDqBBDcBBDeBBDgBBgCOgsILhCABBDHARCvAUoECEEYAEoECEYYAVDYMVjpX2DWdWgDcAF4AIABrQGIAf8FkgEDMC42mAEAoAEBsAEUwAEB2gEGCAEQARgB2gEGCAIQARgU&sclient=gws-wiz-serp'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

    current_converted_price = 0
    difference = 5

    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",","."))

    def get_currency_price(self):

        full_page = requests.get(self.DOLLAR_BYR, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll("span", {"class":"DhPYme",})
        return convert[0].text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(",","."))
        if currency >= self.current_converted_price + self.difference:
            print("Курс сильно изменился!")
        elif currency <= self.current_converted_price - self.difference:
            print("Курс упал")
        print('Сейчас курс: 1 доллар =' + str(currency))
        time.sleep(3)
        self.check_currency()

currency=Currency()
currency.check_currency()