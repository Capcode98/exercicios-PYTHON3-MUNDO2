
#ACHEI FACIL DMS TA MLK!

print('-' * 30)
print('Super mercado do Bonorino')
print('-' * 30)

soma = 0.0
maisDeMil = 0
nomeMaisBarato = ''
nomeProduto = input('Digite o nome do produto: ')
precoProduto = float(input('Digite o preco do produto: '))

precoProdutoAnterior = precoProduto
soma += precoProduto

if precoProduto > 1000:
    maisDeMil += 1

nomeMaisBarato = nomeProduto

continua = input('Deseja continuar? [S,N]').upper()

while continua == 'S':
    nomeProduto = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preco do produto: '))

    soma += precoProduto

    if precoProduto > 1000:
        maisDeMil += 1

    if precoProduto < precoProdutoAnterior:
        nomeMaisBarato = nomeProduto

    continua = input('Deseja continuar? [S,N]').upper()

soma = round(soma, 2)

print()
print('-' * 30)
print(f'Valor das compras: R${soma}')
print('Produtos que custam mais de mil: ', maisDeMil)
print('Produto mais barato:', nomeMaisBarato)
print('-' * 30)
