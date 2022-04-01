from urllib import response
import requests

class Requests_:
    def __init__(self) -> None:
        pass
    def retorna_dados_cep(self, cep):
        response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        print(response.status_code) # 200
        print(response.text)
        # print(type(response.text)) # <class 'str'>
        print(response.json())
        # print(type(response.json())) # <class 'dict'>

        dados_cep = response.json()
        print(dados_cep["localidade"], dados_cep["ddd"])
        return dados_cep

    def retorna_dados_pokemon(self, nome_pokemon):
        response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(nome_pokemon))
        dados_pokemon = response.json()
        return dados_pokemon
    
    def retorna_response(self, url):
        response = requests.get(url)
        return response.text 

if __name__ == '__main__':
    requests_ = Requests_()

    requests_.retorna_dados_cep("18870712")

    print("\n\n")

    dados_pokemon = requests_.retorna_dados_pokemon("bulbasaur")
    print(dados_pokemon["sprites"]["other"]["dream_world"]["front_default"])
    dados_pokemon = requests_.retorna_dados_pokemon("pikachu")
    print(dados_pokemon["sprites"]["other"]["dream_world"]["front_default"])
    dados_pokemon = requests_.retorna_dados_pokemon("pichu")
    print(dados_pokemon["sprites"]["other"]["dream_world"]["front_default"])
    dados_pokemon = requests_.retorna_dados_pokemon("charizard")
    print(dados_pokemon["sprites"]["other"]["dream_world"]["front_default"])
    print(dados_pokemon["sprites"]["front_shiny"])

    print("\n\n")

    response = requests_.retorna_response("https://globallabs.academy/")
    # response = requests_.retorna_response("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/6.png")
    print(response)