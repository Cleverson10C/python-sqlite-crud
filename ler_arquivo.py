def ler_arquivo(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                try:
                    nome, idade = linha.strip().split(",")
                    dados.append({"nome": nome, "idade": int(idade)})
                except ValueError:
                    print(f"Linha inválida no arquivo {caminho_arquivo}: {linha.strip()}")
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro inesperado ao ler {caminho_arquivo}: {e}")
    return dados