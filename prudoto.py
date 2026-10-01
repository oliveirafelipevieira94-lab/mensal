class Produto:
    def __init__(self, descricao: str, preco_unitario: float, estoque: int):
        self.__descricao = descricao
        self.__preco_unitario = preco_unitario
        self.__estoque = estoque

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def estoque(self):
        return self.__estoque

    @preco_unitario.setter
    def preco_unitario(self, valor):
        self.__preco_unitario = valor

    def decrementar_estoque(self, quant: int) -> bool:
        if quant <= 0 or quant > self.__estoque:
            return False
        self.__estoque -= quant
        return True

    def repor_estoque(self, quant: int) -> None:
        if quant > 0:
            self.__estoque += quant

    def __str__(self):
        return f"Produto[{self.__descricao}] R$ {self.__preco_unitario:.2f} (estoque: {self.__estoque})"
