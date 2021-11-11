from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse


STATUS_GENERO = [
    ("FEMININO", "Feminino"),
    ("MASCULINO", "Masculino"),
    ("OUTRO", "Outro"),
]

ESCOLARIDADE = [
    ("EFI", "Ensino fundamental incompleto"),
    ("EFC", "Ensino fundamental completo"),
    ("EMI", "Ensino médio incompleto"),
    ("EMC", "Ensino médio completo"),
    ("ESI", "Ensino superior incompleto"),
    ("ESC", "Ensino superior completo"),
]


class UsuarioManager(BaseUserManager):

    def create_user(self,email,password=None):
        usuario = self.model(email = email)
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()        
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(email = email, password = password)
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()
        return usuario

class Pais(models.Model):
    nome = models.CharField('Nome do país', max_length=194)
    sigla = models.CharField('Sigla do país', max_length=10)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural="Países"
        ordering = ['nome']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.nome)

class Pessoa(AbstractBaseUser,PermissionsMixin):
    nome = models.CharField('Nome completo', max_length=194)
    pais = models.ForeignKey("Pais", on_delete=models.CASCADE, related_name="PaisdoUsuario", blank=True, null=True)
    escolaridade = models.CharField('Escolaridade', max_length=30, choices=ESCOLARIDADE, blank=True, null=True)
    status = models.CharField('Genero', max_length=10, choices=STATUS_GENERO, blank=True, null=True)
    email = models.EmailField('E-mail', unique=True)
    telefoneCelular = models.CharField('Número de telefone', max_length=19, unique=True)
    cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    dataDascimento = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False, blank=True, null=True)
    cep = models.CharField('CEP', max_length=11, blank=True, null=True)
    estado = models.CharField('Estado',max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=194, blank=True, null=True)
    bairro = models.CharField('Bairro',max_length=194, blank=True, null=True)
    logradouro = models.CharField('Logradouro', max_length=194, blank=True, null=True)
    Numero = models.CharField('Número da residencia', max_length=194, blank=True, null=True)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Usuário está ativo",default=True)
    is_staff  = models.BooleanField(verbose_name="Usuário é da equipe de desenvolvimento",default= False)
    is_superuser = models.BooleanField(verbose_name= "Usuário é um superusuario",default=False)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['nome', 'telefoneCelular', 'cpf']

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural="Pessoas"
        ordering = ['nome']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.nome)

class Gerente(models.Model):
    pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaGerente")
    cadastradoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaCadastrouGerente")
    desativadoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaDesativouGerente")
    ativo = models.BooleanField("Gerente está ativo", default=True)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)

    def get_nomePessoa(self):
        return self.pessoa
    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.pessoa)

class Empresa(models.Model):
    nome = models.CharField('Nome da empresa', max_length=194)
    email = models.EmailField('E-mail', unique=True)
    cep = models.CharField('CEP', max_length=194)
    pais = models.ForeignKey("Pais", on_delete=models.CASCADE, related_name="PaisdaEmpresa")
    estado = models.CharField('Estado', max_length=30)
    cidade = models.CharField('Cidade', max_length=194)
    bairro = models.CharField('Bairro', max_length=194)
    logradouro = models.CharField('Logradouro', max_length=194)
    cnpj = models.CharField('CNPJ da empresa', max_length=194, unique=True)
    telefone = models.CharField('Contato da empresa', max_length=194, blank=True, null=True)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)
    cadastradoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaCadastrouEmpresa", blank=True, null=True)
    desativadoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaDesativouEmpresa", blank=True, null=True)
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True)    
    
    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['nome']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.nome)


class Vendedor(models.Model):
    pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaVendedora")
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE, related_name="EmpresaVendedor")
    totalVendido = models.FloatField('Valor comprado do fornecedor', blank=True, null=True)
    dataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)
    dataDesativacao = models.DateField('Data de nascimento', blank=True, null=True)
    cadastradoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaCadastrouVendedor")
    desativadoPor = models.ForeignKey("Pessoa", on_delete=models.CASCADE, related_name="PessoaDesativouVendedor")
    ativo = models.BooleanField(verbose_name="Empresa está ativa",default=True) 

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        ordering = ['pessoa']
        app_label = 'Usuarios'

    def __str__(self):
        return str(self.pessoa)


# id Group = Gerente, Vendedor e funcionário