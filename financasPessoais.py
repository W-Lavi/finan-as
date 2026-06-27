import json
import os

ARQUIVO = "dados_financeiros.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"lançamentos": []}
    with open(ARQUIVO, "r") as arquivo:
        dados = json.load(arquivo)
    return dados


def salvar(dados_para_salvar):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados_para_salvar, arquivo, indent=4)
    print("Dados salvos com sucesso!")


def pedir_tipo():
    tipo = input("Digite o tipo (receita/despesa): ")
    return tipo


def pedir_valor():
    valor = float(input("Digite o valor: "))
    return valor


def registrar_lancamento(dados_do_sistema):
    print("\n--- NOVO LANÇAMENTO ---")
    tipo = pedir_tipo()
    valor = pedir_valor()
    categoria = input("Digite a categoria: ")

    novo = {"tipo": tipo, "valor": valor, "categoria": categoria}

    dados_do_sistema["lançamentos"].append(novo)


def exibir_extrato(dados_do_sistema):
    print("\n--- EXTRATO ATUAL ---")
    lista = dados_do_sistema["lançamentos"]
    for item in lista:
        print(
            "Tipo:",
            item["tipo"],
            "| Categoria:",
            item["categoria"],
            "| Valor: R$",
            item["valor"],
        )
    print("----------------------")


def calcular_saldo(dados_do_sistema):
    lista = dados_do_sistema["lançamentos"]
    saldo_total = 0.0

    for item in lista:
        if item["tipo"] == "receita":
            saldo_total = saldo_total + item["valor"]
        elif item["tipo"] == "despesa":
            saldo_total = saldo_total - item["valor"]

    print("SALDO TOTAL: R$", saldo_total)
    print("----------------------\n")


meus_dados = carregar_dados()

exibir_extrato(meus_dados)
calcular_saldo(meus_dados)

registrar_lancamento(meus_dados)

print("Salvando dados...")
salvar(meus_dados)