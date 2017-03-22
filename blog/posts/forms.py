from .models import Post
from django import forms

class PostForm(forms.ModelForm):
	publish_time = forms.DateTimeField()

	class Meta:
		model = Post
		fields = [
		"title",
		"content",
		"image",
		]

