import os 
os.system('cls')

def criar_contatos(contato,numero):
    try:
        with open('Agenda_contatos.txt','a') as file:
            file.write(f'{contato}:+55{numero}\n')
    except FileNotFoundError:
        print('O Arquivo não foi Encontrado')

def ler_contatos():
    try:
        with open('Agenda_contatos.txt','r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Arquivo não encontrado')

def edit_contato(contato, contatonovo, novonum):
    try:
        with open("Agenda_contatos.txt", 'r') as file:
            linhas=file.readlines()
        encontrado=False
        with open("Agenda_contatos.txt", 'w') as file:
            for c in linhas:
                if not c.startswith(f'{contato}:'):
                    file.write(c)
                else:
                    encontrado=True
        if encontrado:
            with open("Agenda_contatos.txt", 'a') as file:
                file.write(f'{contatonovo}:+55{novonum}\n')
            os.system("cls")
            print(f"Contato '{contato}' atualizado")
        else:
            os.system("cls")
            print(f"Contato '{contato}' não encontrado.")
    except FileNotFoundError:
        os.system("cls")
        print('O Arquivo ainda não foi criado.')
def apagar_arquivo():
    arquivo=('Agenda_contatos.txt')
    if os.path.exists(arquivo):
        os.remove(arquivo)
        os.system("cls")
        print("Todos os contatos foram removidos")
    elif(FileNotFoundError):
        os.system("cls")
        print('Arquivo não encontrado')

def deletar_contato(contato):
    try:
        with open('Agenda_contatos.txt','r') as file:
            linhas=file.readlines()
        encontrado=False
        with open('Agenda_contatos.txt','w') as file:
            for i in linhas:
                if not i.startswith(f'{contato}:'):
                    file.write(i)
                else:
                    encontrado=True
        if encontrado:
            os.system("cls")
            print(f'O contato "{contato}" foi removido com sucesso.')
        else:
            os.system("cls")
            print(f'Contato "{contato}" não encontrado.')
    except FileNotFoundError:
        print('O Arquivo ainda não foi criado')

while True:
    try:
        option=int(input('''BEM VINDO A SUA AGENDA DE CONTATOS:
    DIGITE:
    1-Adicionar um Contato
    2-Ler um Contato
    3-Deletar um Contato
    4-Atualizar um Contato
    5-Sair
    '''))
        if option==1:
            try:
                contato=input('Digite o nome do contato: ')
                numero=int(input('Digite o número do contato(com dd, e o 9, sem o +55): '))
                num=str(numero)
                digitos=len(num)
                if digitos == 11:
                    criar_contatos(contato, numero)
                    os.system("cls")
                    print("Criado com sucesso")
                else:
                    os.system("cls")
                    print("Digite Novamente")
            except ValueError:
                print("Digite um inteiro")
        elif option==2:
            os.system('cls')
            ler_contatos()
        elif option==3:
            while True:
                try:
                    confirmar=int(input('''BEM VINDO AO MENU DE DELETE 
            Digite:
            1-Deletar toda a Agenda
            2-Deletar um Contato específico 
            3-SAIR
            '''))
                    if confirmar==1:
                        fim=input("DESEJA CANCELAR TODOS OS CONTATOS? (S/n): ").lower()
                        if fim == 's':
                            apagar_arquivo()
                            break
                        elif fim =='n':
                            print('Retornando...')
                            os.system('cls')
                            break
                        else:
                            os.system("cls")
                            print("Digito incorreto")
                    elif confirmar == 2:
                        os.system("cls")
                        contato=input("Digite o nome do contato a ser removido: ")
                        deletar_contato(contato)
                        break
                    elif(confirmar==3):
                        os.system("cls")
                        break
                    else:
                        os.system('cls')
                        print('Digite novamente:')
                        continue
                except ValueError:
                    os.system("cls")
                    print("Digite um inteiro")
        elif option==4:
            try:
                os.system("cls")
                contato=input("Digite o nome do contato que deseja alterar: ")
                novo_contato=input("Digite o novo nome corretamente: ")
                numero=int(input("Digite o novo número(com dd, e o 9, sem o +55): "))
                num=str(numero)
                if len(num) == 11:
                    edit_contato(contato, novo_contato, numero)
                else:
                    os.system("cls")
                    print("Digite novamente")
            except ValueError:
                os.system("cls")
                print("Digite um número inteiro")

        elif option==5:
                break
    except ValueError:
        os.system("cls")
        print("Digite um inteiro")