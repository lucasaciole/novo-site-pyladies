from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    members = Member.objects.all()
    return render(request, 'myapp/index.html', {"members": list(members)})