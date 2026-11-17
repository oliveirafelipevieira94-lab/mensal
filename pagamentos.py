from abc import ABC, abstractmethod

class Pagamento(ABC):

  def __init__(self, valor_base: float):
    self.valor_base = valor_base

  @abstractmethod
  def calcular_valor_final(self) -> float:
    pass

class PagamentoDebito(Pagamento):
  """Sem acréscimo ou desconto."""

  def calcular_valor_final(self) -> float:
    return self.valor_base


class PagamentoPix(Pagamento):
  """Desconto de 5%."""

  def calcular_valor_final(self) -> float:
    return self.valor_base * 0.95


class PagamentoDinheiro(Pagamento):
  """Desconto de 3%."""

  def calcular_valor_final(self) -> float:
    return self.valor_base * 0.97


class PagamentoCartao(Pagamento):
  """Acréscimo de 5%."""

  def calcular_valor_final(self) -> float:
    return self.valor_base * 1.05


class Venda:

  def __init__(self, codigo: int, valor_total: float, pagamento: Pagamento):
    self.codigo = codigo
    self.valor_total = valor_total
    self.pagamento = pagamento

  def finalizar_venda(self):
    valor_final = self.pagamento.calcular_valor_final()
    print(f"--- Venda #{self.codigo} Finalizada ---")
    print(f"Valor original: R$ {self.valor_total:.2f}")
    print(
        f"Modalidade: {self.pagamento.__class__.__name__.replace('Pagamento', '')}"
    )
    print(f"Valor final a pagar: R$ {valor_final:.2f}\n")


if __name__ == "__main__":
  valor_da_compra = 200.00

  pagamento_pix = PagamentoPix(valor_da_compra)
  venda1 = Venda(codigo=101, valor_total=valor_da_compra, pagamento=pagamento_pix)
  venda1.finalizar_venda()

  pagamento_dinheiro = PagamentoDinheiro(valor_da_compra)
  venda2 = Venda(
      codigo=102, valor_total=valor_da_compra, pagamento=pagamento_dinheiro
  )
  venda2.finalizar_venda()

  pagamento_cartao = PagamentoCartao(valor_da_compra)
  venda3 = Venda(
      codigo=103, valor_total=valor_da_compra, pagamento=pagamento_cartao
  )
  venda3.finalizar_venda()

  pagamento_debito = PagamentoDebito(valor_da_compra)
  venda4 = Venda(
      codigo=104, valor_total=valor_da_compra, pagamento=pagamento_debito
  )
  venda4.finalizar_venda()
