class ItemVenda:
    def __init__(self, produto, quantidade: int):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor_item = produto.preco_unitario

    @property
    def produto(self):
        return self.__produto

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def valor_item(self):
        return self.__valor_item

    def calcular_subtotal(self) -> float:
        return self.__quantidade * self.__valor_item

    def __str__(self):
        return f"  {self.__quantidade}x {self.__produto.descricao} = R$ {self.calcular_subtotal():.2f}"