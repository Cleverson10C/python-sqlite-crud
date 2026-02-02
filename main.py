from database import criar_tabela
from ler_arquivo import ler_arquivo
from classifica_idades import classificar_idades
from repositorio import (
    inserir_pessoa,
    atualizar_idade,
    listar_maiores,
    listar_menores,
    deletar_pessoa
)
import os


def importar_arquivos(pasta="entradas"):
    try:
        if not os.path.exists(pasta):
            print(f"Pasta '{pasta}' não encontrada.")
            return

        arquivos = os.listdir(pasta)

        for nome_arquivo in arquivos:
            if nome_arquivo.endswith(".txt"):
                caminho = os.path.join(pasta, nome_arquivo)

                pessoas = ler_arquivo(caminho)
                pessoas_classificadas = classificar_idades(pessoas)

                for pessoa in pessoas_classificadas:
                    inserir_pessoa(
                        pessoa["nome"],
                        pessoa["idade"],
                        pessoa["classificacao"]
                    )

        print("Importação concluída com sucesso!")

    except Exception as e:
        print(f"Erro ao importar arquivos: {e}")


def menu():
    while True:
        try:
            print("\n=== MENU ===")
            print("1 - Importar pessoas do arquivo TXT")
            print("2 - Listar maiores de idade")
            print("3 - Listar menores de idade")
            print("4 - Atualizar idade")
            print("5 - Deletar pessoa")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                importar_arquivos()

            elif opcao == "2":
                for nome, idade in listar_maiores():
                    print(f"{nome} - {idade} anos")

            elif opcao == "3":
                for nome, idade in listar_menores():
                    print(f"{nome} - {idade} anos")

            elif opcao == "4":
                id_pessoa = int(input("Digite o ID da pessoa: "))
                nova_idade = int(input("Digite a nova idade: "))
                atualizar_idade(id_pessoa, nova_idade)
                print("Idade atualizada com sucesso!")

            elif opcao == "5":
                id_pessoa = int(input("Digite o ID da pessoa a ser deletada: "))
                deletar_pessoa(id_pessoa)
                print("Pessoa deletada com sucesso!")

            elif opcao == "0":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Erro: digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    criar_tabela()
    menu()