import logging
from extraction import extract_pokemon_data
from transformation import transform_data
from report import generate_report
from logging_config import configure_logging

configure_logging()

def run_pipeline():
    """Função principal que executa o pipeline completo."""
    logging.info("Iniciando o pipeline.")
    try:
        # Etapa 1: Extração dos Dados
        logging.info("Iniciando a extracao dos dados dos Pokemons...")
        pokemon_df = extract_pokemon_data()
        if pokemon_df.empty:
            logging.error("Nenhum dado foi extraido. Pipeline interrompido.")
            return
        
        logging.info(f"Dados extraidos com sucesso! Total de {len(pokemon_df)} Pokemons.")

        # Etapa 2: Transformação e Categorização
        logging.info("Iniciando a transformacao e categorizacao dos dados...")
        pokemon_df, types_count, stats_by_type = transform_data(pokemon_df)
        logging.info("Transformacao e categorizacao concluidas com sucesso.")

        # Etapa 3: Geração e Exportação do Relatório
        logging.info("Gerando e exportando o relatorio final...")
        generate_report(pokemon_df, types_count, stats_by_type)
        logging.info("Relatorio gerado e exportado com sucesso.")

    except Exception as e:
        logging.error(f"Erro inesperado no pipeline: {e}")
        raise  # Re-raise the exception to ensure the process fails

    logging.info("Pipeline concluído com sucesso.")

if __name__ == "__main__":
    run_pipeline()