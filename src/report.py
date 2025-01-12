import pandas as pd
import matplotlib.pyplot as plt
from transformation import transform_data
from extraction import extract_pokemon_data
from utils import type_colors

def save_dataframe_to_csv(df, filename):
    """Salva um DataFrame em formato CSV."""
    try:
        # Diretório fixo para salvar os relatórios
        file_path = f"reports/{filename}"
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Arquivo salvo com sucesso: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar arquivo CSV: {e}")

def save_plot_as_png(plot_function, filename):
    """Salva um gráfico gerado como uma imagem PNG."""
    try:
        # Diretório fixo para salvar o gráfico
        file_path = f"reports/{filename}"
        plot_function()
        plt.savefig(file_path, format="png", bbox_inches="tight")
        plt.close()
        print(f"Gráfico salvo com sucesso: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar gráfico PNG: {e}")

def plot_types_distribution(types_count):
    """Gera o gráfico de distribuição de Pokémons por tipo."""
    plt.figure(figsize=(12, 8))

    # Atribuindo a cor a cada barra com base no tipo do Pokémon
    bar_colors = [type_colors.get(tipo, 'gray') for tipo in types_count['Tipo']] # Usando 'gray' como padrão

    plt.bar(types_count['Tipo'], types_count['Contagem'], color=bar_colors)
    plt.title("Distribuição de Pokémons por Tipo")
    plt.xlabel("Tipo de Pokémon", fontsize=12)
    plt.ylabel("Quantidade de Pokémon", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, count in enumerate(types_count['Contagem']):
        plt.text(i, count + 1, str(count), ha='center', fontsize=10)

    plt.tight_layout()

def generate_report():
    """Gera o relatório consolidado e exporta os resultados."""
    print("Iniciando extração e transformação dos dados...")
    pokemon_df = extract_pokemon_data()

    if pokemon_df.empty:
        print("Nenhum dado foi extraído. O relatório não será gerado.")
        return

    # Transformando os dados
    pokemon_df, types_count, stats_by_type = transform_data(pokemon_df)
    stats_by_type_rounded = stats_by_type.round(2)

    # Exportando as tabelas
    save_dataframe_to_csv(pokemon_df.nlargest(5, 'Experiência Base')[['Nome', 'Experiência Base']], "top_5_experience.csv")
    save_dataframe_to_csv(stats_by_type_rounded, "stats_by_type.csv")

    # Exportando o gráfico
    save_plot_as_png(lambda: plot_types_distribution(types_count), "types_distribution.png")

if __name__ == "__main__":
    generate_report()
