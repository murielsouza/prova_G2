from django.shortcuts import render
from django.http import HttpResponse
from eleicao_app.models import *

def resultado(request):
    retorno = "<h1> RESULTADO DAS VOTAÇÕES </h1> <br>"
    listaEleicoes = Eleicao.objects.all()
    for e in listaEleicoes:
        retorno+=  " <h2> &emsp;RESULTADO ELEIÇÃO: {} </ h2> <br> <br>" .format(e.nome)
        for v in Vaga.objects.filter(eleicao = e):
            retorno+=  " <h3> &emsp;&emsp;VAGA DE: {} </ h3> <br> <br>" .format(v.nome)
            for c in Candidato.objects.filter(vaga = v):
                retorno+=  " <h4> &emsp;&emsp;&emsp;&emsp;{} : {} </ h4> <br>" .format(str(c.nome), str(len(Voto.objects.filter(candidato = c))))
        retorno+=  " <br><br><h3> &emsp;VOTOS BRANCOS: {}</ h3> <br>" .format(str(len(Voto.objects.filter(em_branco=True))))
    #qtd_brancos = len(Voto.objects.filter(em_branco=True))
    #retorno+= "<br> <br> Votos em branco: " + str(qtd_brancos) +"<br>"

    return HttpResponse(retorno)
