from datetime import datetime
from django.shortcuts import render

def index(request):

    date = datetime.today()


    return render(request, 'basedjango/index.html', context={"date": date})
