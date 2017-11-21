from django.contrib import admin
from eleicao_app.models import *

admin.site.register(Eleicao)
admin.site.register(Eleitor)
admin.site.register(Candidato)
admin.site.register(Vaga)
admin.site.register(Token)
admin.site.register(Voto)
