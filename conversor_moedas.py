import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Código da moeda inválido ou dados não encontrados.")
            return

        cotacao = dados[chave]
        valor_atual = cotacao['bid']
        valor_max = cotacao['high']
        valor_min = cotacao['low']
        timestamp = int(cotacao['timestamp'])

        # Converter timestamp para data/hora legível
        data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print(f"Cotação do {moeda} em relação ao Real (BRL):")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Valor máximo do dia: R$ {valor_max}")
        print(f"Valor mínimo do dia: R$ {valor_min}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("Tempo de conexão esgotado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    moeda_usuario = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper().strip()
    if len(moeda_usuario) != 3 or not moeda_usuario.isalpha():
        print("Código da moeda inválido! Deve conter 3 letras.")
    else:
        consultar_cotacao(moeda_usuario)
