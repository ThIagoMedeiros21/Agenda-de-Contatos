import os 
os.system('cls')

def criar_contatos(contato,numero):
    try:
        with open('Agenda_contatos.txt','a') as file:
            file.write(f'{contato}, {numero}')
    except FileNotFoundError:
        print('O Arquivo não foi Encontrado')

print(''''BEM VINDO A SUA AGENDA DE CONTATOS:
 DIGITE:
 1-Adicionar um Contato
 2-Ler um Contato
 3-Deletar um Contato
 4-Atualizar um Contato
''')