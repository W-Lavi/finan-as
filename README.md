 Controle Financeiro Simples (ou o começo de um)

Este é um programa em Python para gerenciamento de finanças pessoais (receitas e despesas), feito de forma simples e estruturado em funções.

O que o código faz:
O programa roda direto pelo terminal e executa os seguintes passos:
1. **Carrega os dados:** Lê as informações salvas no arquivo dados_financeiros.json. Se o arquivo não existir, o programa cria um novo.
2. **Mostra o Extrato:** Lista na tela todos os lançamentos que já foram salvos anteriormente.
3. **Calcula o Saldo:** Soma as receitas, subtrai as despesas e mostra o valor final na tela.
4. **Registra Novo Lançamento:** Pede para o usuário digitar o tipo (receita/despesa), o valor e a categoria de uma nova movimentação.
5. **Salva os dados:** Guarda tudo de volta no arquivo de forma organizada.

 Como testar?
1. Salve o código em um arquivo chamado main.py.
2. Abra o terminal na mesma pasta do arquivo.
3. Execute o comando:
   
   python main.py
