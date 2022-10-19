from django.shortcuts import render
from django.http import *

from app_primer_mvt.models import Familia

def listar_familia(request):
    context = {
        "familiares" : Familia.objects.all(),
    }
    return render(request, "primer_mvt/familiares.html",context)
