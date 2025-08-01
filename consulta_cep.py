import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        # Verifica se a resposta tem erro (quando CEP não existe, a API retorna {'erro': true})
        if dados.get('erro'):
            print("CEP não encontrado. Por favor, verifique o número digitado.")
            return

        # Exibe as informações solicitadas
        print(f"CEP: {dados.get('cep')}")
        print(f"Logradouro: {dados.get('logradouro')}")
        print(f"Bairro: {dados.get('bairro')}")
        print(f"Cidade: {dados.get('localidade')}")
        print(f"Estado: {dados.get('uf')}")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("Tempo de conexão esgotado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    cep_usuario = input("Digite o CEP (somente números): ").strip()
    if not cep_usuario.isdigit() or len(cep_usuario) != 8:
        print("CEP inválido! Deve conter exatamente 8 números.")
    else:
        consultar_cep(cep_usuario)
