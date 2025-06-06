import os, time

# Lista inicial de pessoas que precisam de atenção.
# Cada pessoa é um dicionário com seus dados.
pessoas_em_risco = [
    {"nome": "Maria", "idade": 82, "tipo": "Idosa", "prioridade": 'alta', "bairro": "Centro"},
    {"nome": "João", "idade": 5, "tipo": "Criança", "prioridade": 'média', "bairro": "Vila Nova"},
    {"nome": "Carlos", "idade": 47, "tipo": "PCD", "prioridade": 'alta', "bairro": "Jardim Azul"},
    {"nome": "Luciana", "idade": 70, "tipo": "Idosa", "prioridade": 'baixa', "bairro": "Centro"},
]
# Função simples para limpar a tela do terminal.
def limpar_tela():
    os.system('cls')

# Função principal que mostra o menu e lida com as escolhas do usuário.
def exibir_menu():
    while True: # Loop para manter o menu ativo até o usuário decidir sair.
        limpar_tela()
        print("\n=== SAVEUS - Monitoramento de Pessoas em Risco ===\n")
        print("1 - Listar todas as pessoas em risco")
        print("2 - Enviar alertas de prioridade ALTA")
        print("3 - Enviar alertas de prioridade MÉDIA")
        print("4 - Enviar alertas de prioridade BAIXA")
        print("5 - Sair do sistema\n")
        try:
            selecao_str = input("Escolha uma opção (1-5): ")
            if not selecao_str:
                print("Nenhuma opção digitada. Tente novamente.")
                time.sleep(2)
                continue
            selecao = int(selecao_str)
        except ValueError:
            # Se o usuário digitar algo que não seja um número.
            print("Entrada inválida. Por favor, digite um número.")
            time.sleep(2)
            continue

        match selecao: # Estrutura para tratar as diferentes opções do menu.
            case 1:
                listar_pessoas_risco()
            case 2:
                enviar_alertas('alta')
            case 3:
                enviar_alertas('média')
            case 4:
                enviar_alertas('baixa')
            case 5:
                if encerrar_programa(): # Se o usuário confirmar a saída.
                    break
            case _:
                print("Opção inválida. Tente novamente.")
                time.sleep(2)

# Mostra todas as pessoas cadastradas na lista.
def listar_pessoas_risco():
    limpar_tela()
    contador = 1
    print("\n👥 Lista de Pessoas em Risco:\n")

    for pessoa in pessoas_em_risco:
        # Formata e exibe os dados de cada pessoa.
        print(f'{contador}. Nome: {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['tipo']}, prioridade {pessoa['prioridade']} - bairro: {pessoa['bairro']}')
        contador += 1

    # Pausa para o usuário poder ler antes de voltar ao menu.
    input("\nPressione Enter para voltar ao menu...")

# Envia "alertas" (imprime na tela) para pessoas de uma prioridade específica.
def enviar_alertas(prioridade):
    limpar_tela()
    print(f'🚨 Enviando alertas para pessoas com prioridade {prioridade.upper()}\n')
    contador = 0
    pessoa_encontrada = False

    # Procura na lista por pessoas com a prioridade informada.
    for pessoa in pessoas_em_risco:
        if prioridade == pessoa['prioridade']:
            pessoa_encontrada = True
            contador += 1
            print(f'{contador}. Nome: {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['tipo']}, prioridade {pessoa['prioridade']} - bairro: {pessoa['bairro']}\n')

    if not pessoa_encontrada: # Se ninguém for encontrado com essa prioridade.
        print('⚠️ Nenhuma pessoa encontrada com essa prioridade.')

    input("\nPressione Enter para voltar ao menu...")

# Pergunta ao usuário se ele realmente quer sair do programa.
def encerrar_programa():
    limpar_tela()
    while True: # Loop para garantir uma entrada válida (S ou N)
        selecao = input("Você tem certeza de que deseja encerrar o programa? (S/N):").upper()

        if selecao == "S":
            limpar_tela()
            print("Encerrando o programa. Até logo!")
            time.sleep(3)
            limpar_tela()
            return True # Sinaliza que o programa deve fechar.
        elif selecao == "N":
            return False # Sinaliza para não fechar e voltar ao menu.
        else:
            print("Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não.")
            time.sleep(2)
            limpar_tela() # Limpa a tela antes de perguntar novamente

# Ponto de entrada do script: só executa se o arquivo for rodado diretamente.
if __name__ == "__main__":
    exibir_menu()