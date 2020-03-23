from django.apps import AppConfig


class PostForm(forms.ModelForm):
    class Meta:
        model=post
