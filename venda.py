from datetime import datetime
from item import ItemVenda


class Venda:
    def __init__(self):
        self.__data = datetime.now()
        self.__valor_total = 0.0
        self.__itens = []

    @property
    def data(self):
        return self.__data

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def itens(self):
        return self.__itens

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.calcular_subtotal()
        self.__valor_total = total
        return total

    def adicionar_item(self, produto, quant: int) -> None:
        if produto.decrementar_estoque(quant):
            self.__itens.append(ItemVenda(produto, quant))
            print(f"Item adicionado: {quant}x {produto.descricao}")
        else:
            print(f"Estoque insuficiente para: {produto.descricao}")
        self.calcular_total()

    def remover_item(self, produto) -> None:
        alvo = None
        for item in self.__itens:
            if item.produto is produto:
                alvo = item
                break
        if alvo is None:
            print("Item não encontrado na venda.")
            return
        self.__itens.remove(alvo)
        produto.repor_estoque(alvo.quantidade)
        print(f"Item removido: {produto.descricao}")
        self.calcular_total()

    def imprimir_recibo(self) -> None:
        print("========== VENDA ==========")
        print(f"Data: {self.__data}")
        for item in self.__itens:
            print(item)
        print(f"Total: R$ {self.__valor_total:.2f}")
        print("===========================")