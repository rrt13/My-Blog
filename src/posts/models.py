from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class PostManager(models.Model):
	def all(self, *args, **kwargs):
		return super(PostManager,self).filter(draft=False).filter(publish__lte=timezone.now())

def upload_location(instance, filename):
	return "%s/%s" %(instance.id,filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	image = models.ImageField(upload_to=upload_location,
			null=True,
			blank=True,
			width_field = "width_field",
			height_field = "height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateTimeField(auto_now=False,auto_now_add=False)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	objects = PostManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id":self.id})

	class Meta:
		ordering = ["-timestamp","-updated"]