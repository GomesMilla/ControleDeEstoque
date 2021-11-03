from django.db import models

# dataValidade = models.DateField("Data de validade do produto", auto_now_add=False)


class Movimentacao(models.Model):
    TIPO_TRANSACAO_CHOICE = [
        ("E", "Entrada"),
        ("S", "Saída"),
    ]
    
    tipoTransacao = models.CharField("Tipo de transação!", max_length=3, choices=TIPO_TRANSACAO_CHOICE)
    empresaVendendora = models.ForeignKey("Usuarios.Empresa", related_name="EmpresaVendedora", on_delete=models.PROTECT)
    vendendor = models.ForeignKey("Usuarios.Vendedor", related_name="VendedorDoProduto", on_delete=models.PROTECT)
    produto = models.ForeignKey("Estoque.Produto", related_name="ProdutodaMovimentacao", on_delete=models.PROTECT)
    qtdProdutos = models.FloatField("Quantidade de produtos movimentados")
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    resposavel = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaCadastrouProduto")
    
    class Meta:
        verbose_name = "Movimentação"
        verbose_name_plural = "Movimentações"
        db_table = "movimentacao"

    def __str__(self):
        return self.produto
