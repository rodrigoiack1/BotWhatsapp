import pywhatkit as kit
import time
import datetime

def cadastrar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato (com o código do país, exemplo: +55XXXXXXXXXXX): ")
    agenda[nome] = telefone
    print(f"Contato {nome} adicionado com sucesso!")

def enviar_mensagem(agenda):
    if len(agenda) == 0:
        print("Nenhum contato cadastrado. Adicione um contato primeiro.")
        return

    print("\nContatos cadastrados:")
    for nome in agenda.keys():
        print(f"- {nome}")

    nome_contato = input("\nDigite o nome do contato para enviar a mensagem: ")
    
    if nome_contato in agenda:
        telefone_contato = agenda[nome_contato]
        print(f"\nVocê escolheu o contato: {nome_contato} - {telefone_contato}")
        mensagem = input("Digite a mensagem que deseja enviar: ")

        print("\nAguardando 10 segundos para enviar a mensagem...")
        time.sleep(10)  

        agora = datetime.datetime.now()
        hora = agora.hour
        minuto = agora.minute

        kit.sendwhatmsg(telefone_contato, mensagem, hora, minuto + 1)

        print(f"Mensagem enviada para {nome_contato}!")
    else:
        print("Nome não encontrado na agenda. Tente novamente.")

def main():
    agenda = {}

    while True:
        print("\n1. Adicionar contato")
        print("2. Enviar mensagem")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            cadastrar_contato(agenda)
        elif escolha == "2":
            enviar_mensagem(agenda)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
