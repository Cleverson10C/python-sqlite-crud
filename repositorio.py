from database import conectar

def inserir_pessoa(nome, idade, classificacao):
    
    
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO pessoas (nome, idade, classificacao)  values (?, ?, ?)''', 
        (nome, idade, classificacao)
    )

    conn.commit()
    conn.close()
    
    
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
    