from produto import Produto
from venda import Venda


def main():
    p1 = Produto("Notebook", 3500.00, 10)
    p2 = Produto("Mouse", 80.00, 50)
    p3 = Produto("Teclado", 150.00, 30)

    print(">>> Produtos cadastrados:")
    print(p1)
    print(p2)
    print(p3)

    venda = Venda()

    print("\n>>> Adicionando itens:")
    venda.adicionar_item(p1, 1)
    venda.adicionar_item(p2, 2)
    venda.imprimir_recibo()

    print("\n>>> Removendo o mouse:")
    venda.remover_item(p2)
    venda.imprimir_recibo()

    print("\n>>> Estoque insuficiente (100 notebooks):")
    venda.adicionar_item(p1, 100)
    venda.imprimir_recibo()

    print("\n>>> Remover item inexistente (teclado):")
    venda.remover_item(p3)

    print("\n>>> Estoque final:")
    print(p1)
    print(p2)
    print(p3)


if __name__ == "__main__":
    main()