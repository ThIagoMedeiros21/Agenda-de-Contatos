import os 
os.system('cls')

def criar_contatos(contato,numero):
    try:
        with open('Agenda_contatos.txt','a') as file:
            file.write(f'{contato}: {numero}\n ')
    except FileNotFoundError:
        print('O Arquivo não foi Encontrado')

def ler_contatos():
    try:
        with open('Agenda_contatos.txt','r') as file:
            print(file.read())
    except FileNotFoundError:
        print('nenhum contato foi gerado')

print(''''BEM VINDO A SUA AGENDA DE CONTATOS:
 DIGITE:
 1-Adicionar um Contato
 2-Ler um Contato
 3-Deletar um Contato
 4-Atualizar um Contato
 5-Sair
''')
while True:
    option=int(input('digite uma opção '))
    if option == 1:
        contato=input('digite o nome do contato ')
        numero=input('digite o numero do contato ')
        digitos=len(numero)
        if digitos == 8:
            digitos=str(int)
            criar_contatos(contato,numero)
        elif(digitos>8 or digitos<8):
            print('digite novamente')
            continue
    elif option==2:
        ler_contatos()
    elif option==5:
        break