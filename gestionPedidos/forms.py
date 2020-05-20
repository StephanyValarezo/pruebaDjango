from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()

class FormularioPrueba1(forms.Form):

    nombre=forms.CharField()
    estado=forms.BooleanField(required=False)

class FormularioPrueba2(forms.Form):

    nombre=forms.CharField()