from django import forms


class PostForm(forms.Form):
    isBoast = forms.BooleanField(label="Is it a Boast?", initial=True, required=False)
    content = forms.CharField(label="What is your Roast or Boast", initial="Type here", max_length=280)


class DeleteForm(forms.Form):
    secret = forms.CharField(label="Secret Code", initial="", required=True, max_length=6)
