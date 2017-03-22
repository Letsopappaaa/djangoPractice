from django.contrib import admin
from .models import Post, Author

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'post_size', 'upload_time', 'width_field']
	list_filter = ['post_size', 'title_style']
	class Meta:
		model = Post

	def image_img(self):
		if self.image:
			return u'<img src="%s" />' % self.image.url 
		else:
			return '(No image found)'

class AuthorModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Author


admin.site.register(Post, PostModelAdmin)
admin.site.register(Author, AuthorModelAdmin)