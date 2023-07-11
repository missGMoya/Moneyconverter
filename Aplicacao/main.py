#so prs dizer q tem coisa
#Importar o  app, builder (GUI)
#criar o app
#criar a função build

#ASSIM QUE INICIA UMA APLICAÇÃO
from kivy.app import App
from kivy.lang import Builder
import requests


GUI = Builder.load_file("telona.kv")
class MeuAplicativo(App):
    def build(self): #nao estava indo pq coloquei o B maiusculo foda
        return GUI
    def on_start(self):
        self.pegar_cotacao("USD")
        self.root.ids["label1"].text = f"Dólar {self.pegar_cotacao('USD')} "
        self.root.ids["label2"].text = f"Euro {self.pegar_cotacao('EUR')}"
        self.root.ids["label3"].text = f"Bitcoin R$ {self.pegar_cotacao('BTC')}"
        self.root.ids["label4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)

        jason_requisicao= requisicao.json()
        cotacao = jason_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()
#esse comando roda o aplicativo infinitamente


