"""
Existem 5 motoboys, cada motoboy ganha uma comissão diferente por pedido coletado, e alguns motoboys possuem exclusividade com algumas lojas na qual fazem coletas.

Os motoboys não podem reclamar que ficaram sem pedidos.

Os motoboys que possuem exclusividade com as lojas, possuem prioridade.

Os motoboys podem ter exclusividade com as lojas, mas as lojas não possuem exclusividade com os motoboys.

Hoje existem 10 pedidos para serem retirados em 3 lojas.

Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, preciso ver:
Quem é o motoboy e quantos pedidos terá?
De qual loja é?
Quanto vai ganhar?

Dados do teste

Motoboys
Moto 1 - cobra R$2 reais por entrega e atende todas as lojas
Moto 2 - cobra R$2 reais por entrega e atende todas as lojas
Moto 3 - cobra R$2 reais por entrega e atende todas as lojas
Moto 4 - cobra R$2 reais por entrega e atende apenas a loja 1
Moto 5 - cobra R$3 reais por entrega e atende todas as lojas

Lojas
Loja 1 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50) e paga 5% do valor pedido por entrega fora o valor fixo. 
Loja 2 - 4 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$50, PEDIDO 4 R$50) e paga 5% do valor pedido por entrega fora o valor fixo.
Loja 3 - 3 pedidos (PEDIDO 1 R$50, PEDIDO 2 R$50, PEDIDO 3 R$100) e paga 15% do valor pedido por entrega fora o valor fixo.

O pedido possui um valor e uma loja
Um motoboy atende lojas e cobra uma taxa
Uma loja possui pedidos e paga comissao

Input: pedidos e lista de motoboys
Output: listagem de motoboys
Loja 1 - 1 pedido de 50.00 pagando 5% fora o valor fixo
1 motoboy cobra R$2 por entrega e atende a loja 1

motoboy01;2.00;
1. motoboy=motoboy04;qtdPedidos=1;loja=loja01ganho=4.50
2. motoboy=motoboy01;qtdPedidos=1;loja=loja01ganho=4.50
3. motoboy=motoboy02;qtdPedidos=1;loja=loja01ganho=4.50
4. motoboy=motoboy03;qtdPedidos=1;loja=loja02ganho=4.50
5. motoboy=motoboy05;qtdPedidos=1;loja=loja02ganho=5.50
6. motoboy=motoboy01;qtdPedidos=1;loja=loja02ganho=4.50
7. motoboy=motoboy02;qtdPedidos=1;loja=loja02ganho=4.50
8. motoboy=motoboy03;qtdPedidos=1;loja=loja03ganho=9.50
9. motoboy=motoboy05;qtdPedidos=1;loja=loja03ganho=10.50
10. motoboy=motoboy01;qtdPedidos=1;loja=loja03ganho=17.00

1. motoboy=motoboy04;qtdPedidos=1;loja=loja01;ganho=4.50
2. motoboy=motoboy01;qtdPedidos=3;loja=loja01,loja02,loja03;ganho=26.00
3. motoboy=motoboy02;qtdPedidos=2;loja=loja01,loja02;ganho=9.00
4. motoboy=motoboy03;qtdPedidos=1;loja=loja02,loja03;ganho=14.00
5. motoboy=motoboy05;qtdPedidos=1;loja=loja02,loja03;ganho=16.00


20/04/2022 Dúvidas: 
Quando eu executar o script passando apenas o motoboy ou não passando nenhum motoboy, seria apenas filtro, ou seja, se passar apenas um motoboy, somente esse motoboy atende todos os pedidos?

Como seriam os retornos?
. uma vez que precisa especificar a loja, como seria totalizada a quantidade de pedidos, bem como o valor recebido?
Ex: motoboy=motoboy01;qtdPedidos=3;loja=loja01,loja02,loja03;ganho=26.00

Existe necessidade de ter uma fila circular para rodar todos os motoboys?
"""

def pedido(loja, motoboy):
    
    pass

def solution(motoboy):
    qtd_motoboys = 5
    qtd_pedidos = 10
    qtd_lojas = 3

    #Quando eu executar o script passando apenas o motoboy ou não passando nenhum         motoboy, preciso ver:
    #Quem é o motoboy e quantos pedidos terá?
    #De qual loja é?
    #Quanto vai ganhar?
    motoboy = "moto01"
    qtd_total_pedidos = 1
    loja = "loja01"
    comissao = 50
    retorno = []
    filaMotos = todasMotos
    for pedido in pedidos:
      moto = recuperarMotoComPrioridadeNaLojaDoPedido(pedido, filaMotos)
      if moto:
        retorno.push(f"motoboy={motoboy};qtdPedidos={qtd_total_pedidos};loja={loja};ganho={comissao}")
      else:
        for moto in motoboys:
          if moto.loja == pedido.loja:
            retorno.push(f"motoboy={motoboy};qtdPedidos={qtd_total_pedidos};loja={loja};ganho={comissao}")

    return (f"motoboy={motoboy};qtdPedidos={qtd_total_pedidos};loja={loja};ganho={comissao}")



def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')

if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    expected = "motoboy=moto01;qtdPedidos=1;loja=loja01;ganho=50"
    test(solution, 1, expected)
    
