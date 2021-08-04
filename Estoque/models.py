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

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['Nome']
        db_table = "produto"

    def __str__(self):
        return self.Nome


# Cada item de estoque tem muitas informações que podem ser relevantes para tomada de decisões. Dentre as principais, destacam-se:

# • Número de referência ou número de controle do bem
# • Fabricante
# • Categoria
# • Localização
# • Validade
# • Valor do produto

# Somar em dinheiro quanto que tem de produto no estoque

