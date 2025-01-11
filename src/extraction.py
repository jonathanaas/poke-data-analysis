import pandas as pd
import requests
import logging

# URL base da PokeAPI
BASE_URL = "https://pokeapi.co/api/v2"

def fetch_pokemon_list(limit=100, offset=0):
    """Busca a lista de Pokémons da PokeAPI com base no limite e offset."""

    endpoint = f"{BASE_URL}/pokemon?limit={limit}&offset={offset}"
    
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        return response.json()["results"]
    except Exception as e:
        logging.error(f"Erro durante a requisição: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def fetch_pokemon_details(pokemon_url):
    """Busca os detalhes de um Pokémon dado a URL de seu recurso na API."""
    try:
        response = requests.get(pokemon_url)
        response.raise_for_status()  # Levanta um erro se a resposta não for 200
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar detalhes de Pokémon: {e}")
        return None

def extract_pokemon_data():
    """
    Extrai os dados dos Pokémons da PokeAPI e retorna um DataFrame com as colunas especificadas.
    """
    pokemon_data = []
    logging.info("Iniciando a extração dos dados dos Pokémons...")
    
    pokemon_list = fetch_pokemon_list()

    if not pokemon_list:
        logging.error("Nenhum Pokémon encontrado.")
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver Pokémon
    
    for pokemon in pokemon_list:
        details = fetch_pokemon_details(pokemon["url"])
        if details:
            # Extrair os dados necessários
            pokemon_data.append({
                "ID": details["id"],
                "Nome": details["name"].title(),
                "Experiência Base": details.get("base_experience", 0),
                "Tipos": [t["type"]["name"].title() for t in details["types"]],
                "HP": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "hp"), 0),
                "Ataque": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "attack"), 0),
                "Defesa": next((stat["base_stat"] for stat in details["stats"] if stat["stat"]["name"] == "defense"), 0),
            })
        else:
            logging.warning(f"Detalhes do Pokémon {pokemon['name']} não encontrados.")

    if pokemon_data:
        pokemon_df = pd.DataFrame(pokemon_data)
        logging.info(f"Extração concluída com sucesso! {len(pokemon_df)} Pokémon encontrados.")
        return pokemon_df
    else:
        logging.error("Nenhum dado de Pokémon extraído.")
        return pd.DataFrame()
    

if __name__ == "__main__":
    df = extract_pokemon_data()
    if not df.empty:
        print(df.head())  # Exibe as primeiras linhas do DataFrame se os dados foram extraídos com sucesso
    else:
        print("Nenhum dado foi extraído.")

