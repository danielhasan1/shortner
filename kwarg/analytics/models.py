from django.db import models

# Create your models here.
from shorten.models import kwrg


class ClickEventManager(models.Manager):
	def create_event(self,kwrgInstnace):
		if isinstance(kwrgInstnace,kwrg):
			obj , created = self.get_or_create(kwrg_url=kwrgInstnace)
			obj.count +=1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	kwrg_url = models.OneToOneField(kwrg)
	count = models.IntegerField(default = 0)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)