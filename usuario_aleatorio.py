import requests

def obter_usuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        # Extrair os dados do usuário
        usuario = dados.get('results')[0]  # pegar o primeiro usuário
        nome = usuario.get('name')
        nome_completo = f"{nome.get('title')} {nome.get('first')} {nome.get('last')}"
        email = usuario.get('email')
        pais = usuario.get('location').get('country')

        print(f"Nome completo: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão. Verifique sua internet.")
    except requests.exceptions.Timeout:
        print("Tempo de conexão esgotado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    obter_usuario()
