#from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   # return HttpResponse('<h1>Главная страница(старая)</h1>'
   #                     '<p>Ура.</p>'
   #                     '<br>'
   #                     '<ol>'
   #                     '<li>Раз</li>'
   #                     '<li>Два</li>'
   #                     '<li>Три</li>'
   #                     '</ol>')

   context = {'text': 'Содержимое из контекста'}
   return render(request, 'index.html', context)





