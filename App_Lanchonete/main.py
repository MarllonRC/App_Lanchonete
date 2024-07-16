#Inicio descrição dos item/Cardapio
print('Bem Vindo a lanchonete do Marllon Rafael LTDA')


print('*****************CARDAPIO*****************')
print('------------------------------------------')
print('| CODIGO |       DESCRIÇÃO       | VALOR |')
print('------------------------------------------')
print('|   100  |    Cachorro Quente    |  9,00 |')
print('|   101  | Cachorro Quente Duplo | 11,00 |')
print('|   102  |        X-Egg          | 12,00 |')
print('|   103  |        X-Salada       | 12,00 |')
print('|   104  |        X-Bacon        | 14,00 |')
print('|   105  |        X-Tudo         | 17,00 |')
print('|   200  |   Refrigerante Lata   |  5,00 |')
print('|   201  |     Chá Gelado        |  4,00 |')
print('------------------------------------------')
#Fim descrição dos item/Cardapio
valor_produto = 0
#Incio formatação detabela de preços
while True:
  Codigo = input('Qual seria o código do produto desejado: ')
  Codigo = Codigo.upper ()
  if Codigo != '100' and Codigo != '101' and Codigo != '102' and Codigo != '103' and Codigo != '104' and Codigo != '105' and Codigo != '200' and Codigo != '201':
    print('Código inváldo ;-;.Tente novamente: ')
    continue


  if Codigo == '100':
    print('Voce escolheu um Cachorro Quente no valor de R$9,00')
    valor_produto = valor_produto + 9.00


  elif Codigo == '101':
    print('Voce escolheu um Cachorro Quente Duplo no valor de R$11,00')
    valor_produto = valor_produto + 11.00


  elif Codigo == '102':
    print('Voce escolheu um X-Egg no valor de R$12,00')
    valor_produto = valor_produto + 12.00


  elif Codigo == '103':
    print('Voce escolheu um X-Salada no valor de R$12,00')
    valor_produto = valor_produto + 12.00


  elif Codigo == '104':
    print('Voce escolheu um X-Bacon no valor de R$14,00')
    valor_produto = valor_produto + 14.00


  elif Codigo == '105':
    print('Voce escolheu um X-Tudo no valor de R$17,00')
    valor_produto = valor_produto + 17.00


  elif Codigo == '200':
    print('Voce escolheu um Refrigerante Lata no valor de R$5,00')
    valor_produto = valor_produto + 5.00


  elif Codigo == '201':
    print('Voce escolheu um Chá Gelado no valor de R$4,00')
    valor_produto = valor_produto + 4.00


#Fim formatação detabela de preços


#Comando para caso seja pedido outro item
  Outra_Solicitação = input("Gostaria de pedir algo a mais?:\n1 - Sim\n0 - Não\n>> ")
  Outra_Solicitação = Outra_Solicitação.upper()
  if Outra_Solicitação == "1":
    continue
#Resultado com a soma dos itens escolhidos
  else:
    print('Total a ser pago: R${:.2f}' . format(valor_produto))
    break

