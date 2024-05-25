from django.shortcuts import render



def index(request):
    menu = ['Преимущества','Фотографии']
    return render(request, 'test_site/base.html',{'menu':menu})