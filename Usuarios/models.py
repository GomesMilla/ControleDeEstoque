from django.db import models
from django.contrib.auth.models import( BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.urls import reverse


STATUS_GENERO = [
    ("FEMININO", "Feminino"),
    ("MASCULINO", "Masculino"),
    ("OUTRO", "Outro"),
]
ESTADO_CIVIL = [
    ("SOLTEIRO(A)", "Solteiro(a)"),
    ("CASADO(A)", "Casado(a)"),
    ("DIVORCIADO(A)", "Divorciado(a)"),
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
        usuario = self.model(
            email = email
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()
        
        return usuario
    
    def create_superuser(self,email,password):
        usuario = self.create_user(

            email = email,
            password = password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Pessoa(AbstractBaseUser,PermissionsMixin):
    Nome = models.CharField('Nome completo', max_length=194)
    Naturalidade = models.CharField('Naturalidade', max_length=80)
    Pais = models.CharField('País', max_length=194)
    Escolaridade = models.CharField('Escolaridade', max_length=30, choices=ESCOLARIDADE)
    Status = models.CharField('Genero', max_length=10, choices=STATUS_GENERO)
    email = models.EmailField('E-mail', unique=True)
    Telefone_celular = models.CharField('Número de telefone', max_length=19, unique=True)
    Cpf = models.CharField(verbose_name='CPF', max_length=14, unique=True)
    Nascimento = models.DateField('Data de nascimento', auto_now=False, auto_now_add=False, blank=True, null=True)
    EstadoCivil = models.CharField('Estado civil', max_length=40, choices=ESTADO_CIVIL)
    Profissao = models.CharField('Profissão', max_length=194)
    cep = models.CharField('CEP', max_length=11)
    estado = models.CharField('Estado',max_length=30)
    cidade = models.CharField('Cidade', max_length=194)
    bairro = models.CharField('Bairro',max_length=194)
    logradouro = models.CharField('Logradouro', max_length=194)
    Numero = models.CharField('Número da residencia', max_length=194)
    DataCadastro = models.DateTimeField('Data do cadastro', auto_now_add=True)

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True, 
    )
    is_staff  = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default= False,
    )

    is_superuser = models.BooleanField(
        verbose_name= "Usuário é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural="Pessoas"
        ordering = ['Nome']
        db_table = "Pessoa"

    def __str__(self):
        return self.Nome

class Gerente(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def get_nomePessoa(self):
        return self.Pessoa.Nome
    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"
        db_table = "Gerente"

    def __str__(self):
        return self.pessoa.nome

class Empresa(models.Model):
    Nome = models.CharField('Nome da empresa', max_length=194)
    email = models.EmailField('E-mail', unique=True)
    cep = models.CharField('CEP', max_length=194)
    Pais = models.CharField('País',max_length=194)
    estado = models.CharField('Estado', max_length=30)
    cidade = models.CharField('Cidade', max_length=194)
    bairro = models.CharField('Bairro', max_length=194)
    logradouro = models.CharField('Logradouro', max_length=194)
    Cnpj = models.CharField('CNPJ da empresa', max_length=194, unique=True)
    Telefone = models.CharField('Contato da empresa', max_length=194, blank=True, null=True)
    DataCadastro = models.DateTimeField('Data do cadastro',  auto_now_add=True, null=False)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ['Nome']
        db_table = "empresa"

    def __str__(self):
        return self.Nome


class Vendedor(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"
        db_table = "vendedor"

    def __str__(self):
        return self.pessoa.nome
