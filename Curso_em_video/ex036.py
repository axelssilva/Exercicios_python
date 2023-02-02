valor = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
anos = int(input('Quantos anos pretende pagar: '))
parcela = valor/(anos*12)
if parcela > (salario*30)/100:
    print(f'Emprestimo negado, parcelas de R${parcela:.2f}')
else:
    print(f'Emprestimo aprovado')
