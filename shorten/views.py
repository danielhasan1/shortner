from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.views import View
from .models import kwrg
from . forms import SubmitURLForm
from analytics.models import ClickEvent
# Create your views here.


def about_view(request,*args,**kwargs):
	return render(request,"shorten/about.html")
		

class HomeView(View):
	def get(self,request,*args,**kwargs):
		the_form = SubmitURLForm()
		context = {
		"title":"kwarg.co",
		"form": the_form
		}
		return render(request,"shorten/index.html",context)
		#if request.method=="POST":
	def post(self,request,*args,**kwargs):
		#some_dict = {}
		#some_dict.get('url',"")
		form = SubmitURLForm(request.POST)
		context = {
		"title":"kwarg.co",
		"form": form
		}
		template = "shorten/index.html"
		if form.is_valid():
			new_url = form.cleaned_data.get("url")

			obj, created = kwrg.objects.get_or_create(url=new_url)

			context = {
			"object": obj,
			"created":created,
			}
			if created:
				template = "shorten/already-exits.html"
			else:
				template = "shorten/already-exits.html"
			#return render(request,template,context)
		return render(request,template,context)


		
	


class kwrgCBview(View):
	def get(self,request,slug=None,*args,**kwargs):
		qs = kwrg.objects.filter(shortcode__iexact=slug)
		if qs.count() != 1 and not qs.exists():
			raise Http404

		obj = qs.first()

		ClickEvent.objects.create_event(obj)

		#get_object_or_404(kwrg,shortcode=slug)
		return HttpResponseRedirect(obj.url)