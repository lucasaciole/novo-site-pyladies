from django.shortcuts import render
from .models import Member


# Create your views here.
def index(request):
    members_right = list(Member.objects.order_by('name'))
    members_left = members_right[0:(len(members_right) // 2)]
    members_right = members_right[(len(members_right) // 2):(int(len(members_right)))]
    return render(request, 'myapp/index.html', {"members_left": members_left, "members_right": members_right})