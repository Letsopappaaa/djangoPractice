from django.db import models
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from blog.settings import *
from django.http import HttpResponse, HttpResponseRedirect, Http404

def upload_location(instance, filename, *args, **kwargs):
	full_name = ' '.join([instance.first_name, instance.last_name])
	return 'profile_pic/%s/%s' %(full_name, filename)



class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	acc_created = models.DateTimeField(auto_now_add=True)
	no_of_posts = models.IntegerField(default=0, blank=True)
	last_sign_in = models.DateTimeField(blank=True, null=True)
	facebook_link = models.URLField(max_length=100, blank=True)
	profile_pic = models.ImageField(upload_to=upload_location, blank=True)

	def __str__(self):
		a = ' '.join([self.first_name, self.last_name])
		return a


class Post(models.Model):
	choices_hashtag=(
		("oktatás", "oktatás"),
		("tudomány", "tudomány"),
		("politika", "politika"),
		("sport", "sport"),
	)

	choices_size = (
		("nagy", "nagy"),
		("kis", "kis"),
		)

	choices_title_style = (
		("kép_alatt_fekete", "kép_alatt_fekete"),
		("kép_alatt_sárga", "kép_alattsárga"),
		("kép_alatt_sima", "kép_alatt_sima"),
		("kép_felett_sárga", "kép_felett_sárga"),
		("kép_felett_fekete", "kép_felett_fekete"),
		("képen_alul_sárga", "képen_alul_sárga"),
		("képen_felül_fekete", "képen_felül_fekete"),
		)


	title = models.CharField(max_length=150)
	content = models.CharField(max_length=4000)
	image = models.ImageField(upload_to='pictures/',
		height_field="height_field",
		width_field="width_field")
	width_field = models.IntegerField(default=0)
	height_field = models.IntegerField(default=0)
	hashtag = models.CharField(max_length=50 ,choices=choices_hashtag)
	post_size = models.CharField(max_length=20, choices=choices_size, blank=True, null=True)
	title_style = models.CharField(max_length=100, choices=choices_title_style)
	author = models.ForeignKey(Author)
	upload_time = models.DateTimeField(auto_now_add=True)
	publish_time = models.DateTimeField(auto_now=True, blank=True)
	headlines = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.width_field <= 600:
			self.post_size = "kis"
		else:
			self.post_size = "nagy"
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={"id": self.id})

	def get_category_url(self):
		return reverse('categories', kwargs={"hashtag" : self.hashtag})



