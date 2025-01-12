import matplotlib.pyplot as plt
from extraction import extract_pokemon_data
from utils import type_colors

# Adicionando a coluna "Categoria" com base na Experiência Base
def categorize_experience(experience):
    if experience < 50:
        return "Fraco"
    elif 50 <= experience <= 100:
        return "Médio"
    else:
        return "Forte"

def get_types_count(pokemon_df):
    """Retorna a contagem de Pokémon por tipo."""
    return pokemon_df['Tipos'].value_counts().reset_index()

def get_stats_by_type(pokemon_df):
    """Calcula a média de ataque, defesa e HP por tipo."""
    return pokemon_df.groupby('Tipos').agg({
        'Ataque': 'mean',
        'Defesa': 'mean',
        'HP': 'mean'
    }).reset_index()

def get_top_5_experience(pokemon_df):
    """Retorna os 5 Pokémon com maior experiência base."""
    return pokemon_df.nlargest(5, 'Experiência Base')[['Nome', 'Experiência Base']]


def transform_data(pokemon_df):
    """Transforma os dados dos Pokémon e gera as categorias, gráficos e análises estatísticas."""

    pokemon_df['Categoria'] = pokemon_df['Experiência Base'].apply(categorize_experience)

    pokemon_df_exploded = pokemon_df.explode('Tipos')

    # Transformação de Tipos - Contagem de Pokémon por tipo
    types_count = get_types_count(pokemon_df_exploded)
    types_count.columns = ['Tipo', 'Contagem']

    # Análise estatística - média de ataque, defesa e HP por tipo de Pokémon
    stats_by_type = get_stats_by_type(pokemon_df_exploded)

    return pokemon_df, types_count, stats_by_type
