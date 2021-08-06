from django.db import models

CURVA_ABC = [
    ("A", "Mais importante e de maior valor"),
    ("B", "Valor médio"),
    ("B", "Valor baixo"),
]

class Produto(models.Model):
    Nome = models.CharField('Nome do produto', max_length=194)
    Categoria = models.CharField('Categoria', max_length=30, choices=CURVA_ABC)
    Descricao = models.TextField('Descrição do produto', max_length=194, blank=True, null=True)
    QuantidadeMinima = models.IntegerField('Quantidade mínima')
    ValorUnitario = models.FloatField('Valor unitário do produto')

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['Nome']
        db_table = "produto"

    def __str__(self):
        return self.Nome

class Armazenamento(models.Model):
    Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    Quantidade = models.IntegerField('Quantidade de produto')
    DataValidade = models.DateField('Data de validade')
    ValorEstoque = models.FloatField('Valor de Estoque', blank=True, null=True)
    EstoqueAtual = models.FloatField('Quantidade disponivel no estoque', blank=True, null=True)

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        db_table = "armazenamento"

    def __str__(self):
        return self.Produto.Nome



# Cada item de estoque tem muitas informações que podem ser relevantes para tomada de decisões. Dentre as principais, destacam-se:

# • Número de referência ou número de controle do bem
# • Fabricante
# • Categoria
# • Localização
# • Validade
# • Valor do produto

# Somar em dinheiro quanto que tem de produto no estoque

