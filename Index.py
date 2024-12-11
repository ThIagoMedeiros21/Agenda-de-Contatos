import os 
os.system('cls')

def criar_contatos(contato,numero):
    try:
        with open('Agenda_contatos.txt','a') as file:
            file.write(f'{contato}: {numero}\n')
    except FileNotFoundError:
        print('O Arquivo não foi Encontrado')

def ler_contatos():
    try:
        with open('Agenda_contatos.txt','r') as file:
            print(file.read())
    except FileNotFoundError:
        print('Arquivo não encontrado')

def edit_contato ():
    try:
        ...
    except FileNotFoundError:
        print('O Arquivo ainda não foi criado')

def apagar_arquivo():
    arquivo=('Agenda_contatos.txt')
    if os.path.exists(arquivo):
        os.remove(arquivo)
        os.system("cls")
        print("Todos os contatos foram removidos")
    elif(FileNotFoundError):
        os.system("cls")
        print('Arquivo não encontrado')

while True:
    option=int(input('''BEM VINDO A SUA AGENDA DE CONTATOS:
 DIGITE:
 1-Adicionar um Contato
 2-Ler um Contato
 3-Deletar um Contato
 4-Atualizar um Contato
 5-Sair
'''))
    if option == 1:
        contato=input('digite o nome do contato ')
        numero=input('digite o numero do contato ')
        digitos=len(numero)
        if digitos == 8:
            digitos=str(int)
            criar_contatos(contato,numero)
            os.system("cls")
            print("Criado com sucesso")
        else:
            os.system("cls")
            print("Digite Novamente")
    elif option==2:
        os.system('cls')
        ler_contatos()
    elif option==3:
        while True:
            confirmar=int(input('''BEM VINDO AO MENU DE DELETE 
    Digite:
    1-Deletar toda a Agenda
    2-Deletar um Contato especifico 
    '''))
            if confirmar==1:
                fim=input("DESEJA CANCELAR TODOS OS CONTATOS?(S/n) ").lower()
                if fim == 's':
                    apagar_arquivo()
                    break
                elif fim == 'n':
                    print('Retornando...')
                    os.system('cls')
                    break
                else:
                    os.system("cls")
                    print("Digito incorreto: ")
            elif confirmar==2:
                os.system("cls")
                print('Em desenvolvimento...')
                break
            else:
                os.system('cls')
                print('Digite novamente:')
                continue
    elif option==5:
        break