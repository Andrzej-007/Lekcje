from django.shortcuts import render
from django.views.generic import View


class ShowData(View):
    def get(self, request):
        return render(request, 'test_44.html', locals())

class ShowLink(View):
    def get(self,request):
        return render(request, 'jesien_2020.html', locals())




