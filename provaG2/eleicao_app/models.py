from django.contrib.auth.models import User
from django.db import models

class Eleicao(models.Model):
    nome = models.CharField(max_length=128)
    dataH_inicio = models.DateTimeField(blank=True, null=True)
    dataH_fim = models.DateTimeField(blank=True, null=True)
    local = models.CharField(max_length=128)

    def __str__(self):
        return self.nome + " ( " + self.local + " )"


class Vaga(models.Model):
    nome = models.CharField(max_length=128)
    eleicao = models.ForeignKey(Eleicao, null=True, blank=True)
    def __str__(self):
        return self.nome + " ( " + self.eleicao.nome + " )"

class Candidato(models.Model):
    nome = models.CharField(max_length=128)
    eleicao = models.ForeignKey(Eleicao, null=True, blank=False)
    vaga = models.ForeignKey(Vaga, null=True, blank=False)

    def __str__(self):
        return self.nome + " --candidato em:  " + self.vaga.nome


class Voto(models.Model):
    dataH_voto = models.DateTimeField(blank=True, null=True)
    candidato = models.ForeignKey(Candidato, null=True, blank=False)
    em_branco= models.BooleanField("Deseja votar em branco!?",default=False)

    def __str__(self):
        return "Voto X - "+ str(self.dataH_voto) + " --voto em:  " + self.candidato.nome

class Token(models.Model):
    codigo = models.CharField(max_length=8)
    senha = models.CharField(max_length=35)
    voto= models.BooleanField("Candidato votou!?",default=False) #controlado por administrador rs'
    #voto = models.OneToOneField(Voto, null=True, blank=True)

    def __str__(self):
        return "Tokeeen: "+self.codigo

class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=14)
    eleicao = models.ForeignKey(Eleicao, null=True, blank=False)
    token = models.OneToOneField(Token, null=True, blank=False)
    usuario = models.ForeignKey(User, null=True, blank=False)

    def __str__(self):
        return self.nome + " ( " + self.cpf + " )"
