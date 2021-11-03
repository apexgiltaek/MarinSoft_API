from django.forms import ModelSerializer
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        field = '__all__'