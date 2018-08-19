from django import forms


class User(forms.Form):
    name = forms.CharField(label='用户名', max_length=10)
    password = forms.CharField(label='密码', max_length=20,required=True)
