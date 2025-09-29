from django.shortcuts import render
from app.sait.models import Settings
def index(request):
    settings_all = Settings.objects.all()
    return render(request, "index.html", locals())