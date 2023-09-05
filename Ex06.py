import csv

def cadastrar_cliente(nome, endereco, telefone, email):
    with open('clientes.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, endereco, telefone, email])
    print('Cliente cadastrado com sucesso!')

def main():
    nome = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    email = input('Digite o e-mail do cliente: ')
    cadastrar_cliente(nome, endereco, telefone, email)

if __name__ == '__main__':
    main()
