from django import forms
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()

    def clean_user(self):
        username = self.cleaned_data['user']
        user, created = User.objects.get_or_create(username = username)
        return user