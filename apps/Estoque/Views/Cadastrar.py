from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required #Importando a view do Django para fazer login
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

from Usuarios.forms import PessoaForm, EmpresaForm, VendedorForm
from Usuarios.models import Pais
from django.contrib.auth.models import Group