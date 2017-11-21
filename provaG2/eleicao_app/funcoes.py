from django.shortcuts import render
from django.http import HttpResponse
from eleicao_app.models import *

def resultado(request):
    retorno = "<h1> RESULTADO DAS VOTAÇÕES </h1>"
    listaVotos = Voto.objects.all()
    listaCandidatos = Candidato.objects.all()
    branco = Voto.objects.filter(em_branco=True)
    qtd_brancos = len(branco)
    qtd_candidatos = len(listaCandidatos)
    retorno+= "<br> <br> Votos em branco: " + str(qtd_brancos) +"<br>"
    return HttpResponse(retorno)
