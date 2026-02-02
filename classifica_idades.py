def classificar_idades(pessoas):
    pessoas_classificadas = []

    for pessoa in pessoas:
        classificacao = (
            "Menor de idade"
            if pessoa["idade"] < 18
            else "Maior de idade"
        )

        pessoas_classificadas.append({
            "nome": pessoa["nome"],
            "idade": pessoa["idade"],
            "classificacao": classificacao
        })


    return pessoas_classificadas
