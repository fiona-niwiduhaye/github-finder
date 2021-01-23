from django import forms
from .models import Profile
from .models import Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=["user"]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []