from django.db import models

def upload_location(instance, filename, *args, **kwargs):
	full_name = ' '.join([instance.first_name, instance.last_name])
	return 'profile_pic/%s/%s' %(full_name, filename)

def upload_location_comment_img(instance, filename, *args, **kwargs):
	full_name = ' '.join([instance.first_name, instance.last_name])
	return 'comment_pic/%s/%s' %(full_name, filename)

class account(models.Model):
	"""docstring for account"""

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	acc_created = models.DateTimeField(auto_now_add=True)
	no_of_comments = models.IntegerField(default=0, blank=True)
	last_sign_in = models.DateTimeField(blank=True, null=True)
	facebook_link = models.URLField(max_length=100, blank=True)
	profile_pic = models.ImageField(upload_to=upload_location, blank=True)
	total_upvotes = models.IntegerField(default=0, unique=True)

	def __str__(self):
		a = ' '.join([self.first_name, self.last_name])
		return a

class comments(models.Model):
	"""docstring for comments"""

	account_name = models.ForeignObject(account, on_delete=models.CASCADE, from_fields=['upvotes'], to_fields=['total_upvotes'])
	content = models.TextField()
	img = models.ImageField(upload_to=upload_location_comment_img, blank=True)
	upvotes = models.IntegerField(default=0)

	def __str__(self):
		return self.account_name