from django.shortcuts import render
from django.views.generic import View
from .models import Twit


class ListView(View):
	def get(self,request):
		template_name = 'lista.html'
		twits = Twit.objects.all().order_by('-fecha')
		context = {'twits':twits}
		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,slug):#cambiar slug
		template_name='detalle.html'
		#post=Post.objects.get(pk=id)
		twit=Twit.objects.get(slug=slug)
		context = {'twit':twit}
		return render(request,template_name,context)

# Create your views here.
