import json

ARQUIVO = "dados_financeiros.json"


def carregar_dados():
    with open(ARQUIVO, "r") as arquivo:
        dados = json.load(arquivo)
    return dados


def salvar(dados_para_salvar):

    with open(ARQUIVO, "w") as arquivo:
        
        json.dump(dados_para_salvar, arquivo)
    print("Dados salvos com sucesso!")


print("Lendo dados antigos...")
meus_dados = carregar_dados()
print("Dados atuais no arquivo:", meus_dados)

novo_lançamento = {"tipo": "receita", "valor": 1500, "categoria": "salario"}

meus_dados["lançamentos"].append(novo_lançamento)

print("Salvando dados...")
salvar(meus_dados)