from rest_framework import routers, serializers, viewsets
from eleicao_app.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class EleicaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = '__all__'

class CandidatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

class EleitorSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Eleitor
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        e = User.objects.create(**user_data)
        e = Eleitor.objects.create(usuario = e, **validated_data)
        return e

class VagaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'

class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'

class VotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'

#class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
#    retorno = "<h1> RESULTADO DAS VOTAÇÕES </h1>"
#    listaVotos = Voto.objects.all()
#    branco = Votos.objects.filter(em_branco=True)
#    for a in listaVotos:
#        if a.embranco == False:
#            print("23")
#    return HttpResponse(retorno)
