from django.shortcuts import render
from app.sait.models import Settings, Statics, Imgaes
def index(request):
    settings_all = Settings.objects.all()
    statistic_all = Statics.objects.all()
    image_all = Imgaes.objects.all()
    return render(request, "index.html", locals())