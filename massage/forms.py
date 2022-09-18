from django import forms

from massage.models import Post


class newpost(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['prof', 'views', 'like']
        pass
    pass
