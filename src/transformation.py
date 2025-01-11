import matplotlib.pyplot as plt
from extraction import extract_pokemon_data

def transform_data(pokemon_df):
    """Transforma os dados dos Pokémon e gera as categorias, gráficos e análises estatísticas."""

    # Adicionando a coluna "Categoria" com base na Experiência Base
    def categorize_experience(experience):
        if experience < 50:
            return "Fraco"
        elif 50 <= experience <= 100:
            return "Médio"
        else:
            return "Forte"

    pokemon_df['Categoria'] = pokemon_df['Experiência Base'].apply(categorize_experience)

    # Explodindo a coluna de Tipos para fazer a contagem e depois fazer algumas análises
    pokemon_df_exploded = pokemon_df.explode('Tipos')

    # Transformação de Tipos - Contagem de Pokémon por tipo
    types_count = pokemon_df_exploded['Tipos'].value_counts().reset_index()
    types_count.columns = ['Tipo', 'Contagem']
    
    # Gerando gráfico de barras para a distribuição de Pokémon por tipo com matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(types_count['Tipo'], types_count['Contagem'], color=plt.cm.viridis(range(len(types_count))))
    plt.title("Distribuição de Pokémon por Tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Quantidade de Pokémon")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    # Análise estatística - média de ataque, defesa e HP por tipo de Pokémon
    stats_by_type = pokemon_df_exploded.groupby('Tipos').agg({
        'Ataque': 'mean',
        'Defesa': 'mean',
        'HP': 'mean'
    }).reset_index()

    print("Média de Ataque, Defesa e HP por Tipo de Pokémon:")
    print(stats_by_type)

    # Os 5 Pokémon com maior Experiência Base
    top_5_experience = pokemon_df.nlargest(5, 'Experiência Base')
    print("\nTop 5 Pokémon com Maior Experiência Base:")
    print(top_5_experience[['Nome', 'Experiência Base']])

    return pokemon_df, types_count, stats_by_type

# Exemplo de uso
if __name__ == "__main__":
    # Aqui você chamaria a função 'extract_pokemon_data' para pegar os dados (não repetido neste código)
    pokemon_df = extract_pokemon_data()
    
    if not pokemon_df.empty:
        # Transformando os dados e gerando as análises
        pokemon_df, types_count, stats_by_type = transform_data(pokemon_df)
    else:
        print("Não há dados para processar.")
