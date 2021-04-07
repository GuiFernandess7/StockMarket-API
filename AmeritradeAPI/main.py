class Ameritrade:

    def __init__(self, symbol, requestType, your_Key):

        self.url = 'https://api.tdameritrade.com/v1/instruments'
        self.symbol = symbol
        self.requestType = requestType
        self.your_Key = your_Key

    def get_Data(self):

        info = {'apikey': self.your_Key,
                'symbol': self.symbol,
                'projection': self.requestType}

        response = rq.get(self.url, params=info)
        data = response.json()

        return data


def main():

    a = Ameritrade('GOOG', 'fundamental', key)
    print(a.get_Data())


if __name__ == '__main__':

    import requests as rq
    from config import key

    main()
