from database import criar_tabela
from ler_arquivo import ler_arquivo
from classifica_idades import classificar_idades
from repositorio import inserir_pessoa
import os

def processar_pasta(pasta="entradas"):
    criar_tabela()
    
    # Filtra os arquivos.txt na pasta de entradas
    arquivos_entrada = os.listdir(pasta)
    for nome_arquivo in arquivos_entrada:
        if nome_arquivo.endswith(".txt"):
            
            # Lê as idades dos arquivos, converte para inteiros e classifica
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            idades = ler_arquivo(caminho_arquivo)
            dados = classificar_idades(idades)
            
            # Insere os dados no banco de dados
            for pessoa in dados:
                inserir_pessoa(
                pessoa["nome"], 
                pessoa["idade"], 
                pessoa["classificacao"]
            )
                
               
if __name__ == "__main__":
    processar_pasta()
