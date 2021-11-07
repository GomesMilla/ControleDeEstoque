from django.db import models
from django.db.models.base import Model

CURVA_ABC = [
    ("A", "Mais importante e de maior valor"),
    ("B", "Valor médio"),
    ("B", "Valor baixo"),
]

class Sala(models.Model):
    nome = models.CharField("Nome da sala", max_length=200)
    predio = models.CharField("Prédio", max_length=40, null=True, blank=True)
    andar = models.IntegerField("Andar da sala", null=True, blank=True)
    descricao = models.TextField("Descrição da sala")
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    cadastradoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.CASCADE, related_name="PessoaCadastrouSala")
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True) 
    desativadoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.CASCADE, related_name="PessoaDesativouSala", blank=True, null=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)   

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['nome']
        db_table = "Sala"

    def __str__(self):
        return self.nome

class Classificacao(models.Model):
    nome = models.CharField('Nome Categoria', max_length=30)
    descricao = models.CharField("Descrição da categoria", max_length=200)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    cadastradoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaCadastrouCategoria", blank=True, null=True)
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True, blank=True, null=True) 
    desativadoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaDesativouCategoria", blank=True, null=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)  

    class Meta:
        verbose_name = "Classificação"
        verbose_name_plural = "Classificações"
        ordering = ['nome']
        db_table = "Classificacao"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField('Nome do produto', max_length=194)
    classificacao = models.ForeignKey("Classificacao", on_delete=models.PROTECT, related_name="CategoriaProduto")
    categoria = models.CharField('Categoria', max_length=30, choices=CURVA_ABC)
    gerenteResposavel = models.ForeignKey("Usuarios.Gerente", related_name="GerenteResposasavelpeloProduto", on_delete=models.PROTECT)
    descricao = models.TextField('Descrição do produto', max_length=194, blank=True, null=True)
    quantidadeMinima = models.IntegerField('Quantidade mínima')
    valorUnitario = models.FloatField('Valor unitário do produto')
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    cadastradoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaCadastrouProduto")
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True) 
    desativadoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaDesativouProduto", blank=True, null=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
        db_table = "produto"

    def __str__(self):
        return self.nome

class LocalArmazenamentoProduto(models.Model):
    sala = models.ForeignKey("Sala", related_name="SalaDeArmazenamento", on_delete=models.PROTECT)
    produto = models.ForeignKey("Produto", related_name="ProdutoArmazenado", on_delete=models.PROTECT)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    cadastradoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaCadastrouLocalArmazenamentoProduto")
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True) 
    desativadoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.PROTECT, related_name="PessoaDesativouoLocalArmazenamentoProduto", blank=True, null=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)

    class Meta:
        verbose_name = "Local Armazenamento"
        verbose_name_plural = "Locais de Armazenamento"
        ordering = ['produto']
        db_table = "LocalArmazenamento"

    def __str__(self):
        return self.sala

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valorEstoque = models.FloatField('Valor de Estoque', blank=True, null=True)
    estoqueAtual = models.FloatField('Quantidade disponivel no estoque', blank=True, null=True)
    gerenteResposavel = models.ForeignKey("Usuarios.Gerente", related_name="GerenteResponsavel", on_delete=models.PROTECT)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    cadastradoPor = models.ForeignKey("Usuarios.Pessoa", on_delete=models.CASCADE, related_name="PessoaCadastrouEstoque")

    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        db_table = "estoque"

    def __str__(self):
        return self.produto.nome



# Cada item de estoque tem muitas informações que podem ser relevantes para tomada de decisões. Dentre as principais, destacam-se:

# • Número de referência ou número de controle do bem
# • Fabricante OK
# • Categoria OK
# • Localização OK
# • Validade OK
# • Valor do produto OK 

# Somar em dinheiro quanto que tem de produto no estoque

