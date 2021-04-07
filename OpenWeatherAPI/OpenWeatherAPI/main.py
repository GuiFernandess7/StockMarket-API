class Clima:

    def __init__(self, key, url, cidade):

        self.key = key
        self.url = url
        self.cidade = cidade

    def getRawdata(self):

        try:
            r = rq.get(self.url)
            self.dados = r.json()
            return self.dados

        except r.exceptions.HTTPError as err:
            raise SystemError(err)

    def accessCoordinates(self):

        coordinates = self.dados['coord']
        dadosList = []

        for v in coordinates.values():

            dadosList.append(v)

        return f'''Longitude: {dadosList[0]} / Lagitude: {dadosList[1]}'''

    def weatherDescription(self):

        descricao = self.dados['weather'][0]
        dadosList = []

        for v in descricao.values():

            dadosList.append(v)

        return f'Id: {dadosList[0]} /Condição: {dadosList[1]} /Descrição: {dadosList[2]}'

    def weatherInfo(self):

        dadosClima = self.dados['main']
        dadosList = []

        for v in dadosClima.values():

            dadosList.append(v)

        return f'''Temperatura: {dadosList[0]}/ Sensação Térmica: {dadosList[1]}/ Temperatura mínima: {dadosList[2]}
        Temperatura máxima: {dadosList[3]}/ Pressão: {dadosList[4]}/ Umidade: {dadosList[5]}'''

    def windData(self):

        dadosVento = self.dados['wind']
        dadosList = []

        for v in dadosVento.values():

            dadosList.append(v)

        return f'''Velocidade: {dadosList[0]}/ Graus: {dadosList[1]}'''


def main():

    cidade = input('Informe uma cidade para ver seu clima em tempo real: ')
    key = config.api_key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric&lang=pt_br"
    now = datetime.datetime.now()

    info = Clima(key, url, cidade)
    rawData = info.getRawdata()
    ask = int(input('''Escolha um opção para ver informações detalhadas:
    [1] - Coordenadas
    [2] - Descrição do Clima
    [3] - Clima
    [4] - Detalhes do vento
    Opção: '''))
    if ask == 1:
        print(info.accessCoordinates())
        print(now)
        time.sleep(5)
    elif ask == 2:
        print(info.weatherDescription())
        print(now)
        time.sleep(5)
    elif ask == 3:
        print(info.weatherInfo())
        print(now)
        time.sleep(5)
    elif ask == 4:
        print(info.windData())
        print(now)
        time.sleep(5)
    else:
        print('Informação Inválida')


if __name__ == '__main__':

    from OpenWeatherAPI import config
    import datetime
    import time
    import requests as rq

    main()
