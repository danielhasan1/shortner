from django.db import models
from .utils import code_generator,create_shortcode
from .validators import validator_url, validate_dot_com, validaotr_http
from django_hosts.resolvers import reverse
# Create your models here.



class kwrg(models.Model):
	url = models.CharField(max_length=250, validators=[validator_url, validate_dot_com, validaotr_http])
	shortcode = models.CharField(max_length=15,unique=True,blank=True)
	update = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default = True)
	#empty_datetime = models.DateTimeField(auto_now=False)
	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode=="":
			self.shortcode = create_shortcode(self)
		super(kwrg,self).save(*args,**kwargs)
		


	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)


	def get_short_url(self):
		url_path = reverse("scode",kwargs={'slug':self.shortcode}, host='www',scheme='http')
		print("shprt",url_path)
		return url_path