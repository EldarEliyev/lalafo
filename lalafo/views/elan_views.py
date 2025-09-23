from django.shortcuts import render, redirect, get_object_or_404
from..models.elan import Elan
from..forms import ElanForm
from..tasks import send_created_elan_email
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from..serializers import ElanSerializer
from..models.like import Like 

class ElanViewSet(viewsets.ModelViewSet):
    queryset = Elan.objects.all()
    serializer_class = ElanSerializer

    @action(detail=True, methods=['post'])
    def toggle_elan_like(self, request, pk=None):
        elan = self.get_object()
        like = Like.objects.filter(elan=elan).first()

        if like:
            like.delete()
            message = "Unliked Elan"
        else:
            Like.objects.create(elan=elan)
            message = "Liked Successfully Elan"
        return Response({"message": message,  "like_count": elan.elan_likes.count()})

#Elan CRUD:
def elan_list(request):
    elanlar = Elan.objects.all()
    return render(request,  "elan_list.html",  {"elanlar": elanlar})

def create_elan(request):
    if request.method == "POST":
        form = ElanForm(request.POST, request.FILES)
        if form.is_valid():
            elan = form.save()
            send_created_elan_email.delay(elan.title)
            return redirect("elan_list")
    else:
        form = ElanForm()
    return render(request,  "create_elan.html",  {"form": form})

def update_elan(request, pk):
    elan = get_object_or_404(Elan, pk=pk)
    if request.method == "POST":
        form = ElanForm(request.POST, request.FILES, instance=elan)
        if form.is_valid():
            form.save()
            return redirect("elan_list")
    else:
        form = ElanForm(instance=elan)
    return render(request,  "update_elan.html",  {"form": form})


def delete_elan(request, pk):
    elan = get_object_or_404(Elan, pk=pk)
    if request.method == "POST":
        elan.delete()
        return redirect("elan_list")
    return render(request,  "delete_elan.html",  {"elan": elan})

