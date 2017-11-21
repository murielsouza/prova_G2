from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from eleicao_app.models import *
from eleicao_app.serializers import *

def resultado(request):
    retorno = "<h1> RESULTADO DAS VOTAÇÕES </h1>"
    listaVotos = Voto.objects.all()
    branco = Votos.objects.filter(em_branco=True)
    for a in listaVotos:
        if a.embranco == False:
            print("23")
    return HttpResponse(retorno)

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
