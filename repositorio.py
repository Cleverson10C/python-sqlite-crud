from database import conectar


def salvar_em_arquivo(nome, idade, classificacao, caminho="pessoas.txt"):
    try:
        with open(caminho, "a", encoding="utf-8") as file:
            file.write(f"{nome},{idade},{classificacao}\n")
    except Exception as e:
        print(f"Erro ao gravar em arquivo: {e}")


def inserir_pessoas(nome, idade, classificacao):
    try:
        idade = int(idade)
    except ValueError:
        print("Idade inválida. Por favor, digite um número.")
        return
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO pessoas (nome, idade, classificacao)  values (?, ?, ?)''', 
        (nome, idade, classificacao)
    )

    conn.commit()
    conn.close()

    salvar_em_arquivo(nome, idade, classificacao)
    
    
def atualizar_idade(id_pessoa, nova_idade):
    classificacao = "Menor de idade" if nova_idade < 18 else "Maior de idade"   
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE pessoas SET idade = ?, classificacao = ? WHERE id = ?", 
        (nova_idade, classificacao, id_pessoa)
    )

    conn.commit()
    conn.close()
    
    
    
def listar_maiores():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome, idade FROM pessoas WHERE classificacao = 'Maior de idade'"
    )

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def listar_menores():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT nome, idade FROM pessoas WHERE classificacao = 'Menor de idade'"
    )

    resultados = cursor.fetchall()
    conn.close()
    return resultados


def deletar_pessoa(id_pessoa):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM pessoas WHERE id = ?", (id_pessoa,)
    )

    conn.commit()
    conn.close()
    