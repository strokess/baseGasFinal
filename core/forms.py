from django import forms

class ClientesForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    colonia = forms.CharField(label= "Colonia", required=True)
    numeroE = forms.CharField(label= "No. Exterior", required=True)
    numeroI = forms.CharField(label= "No. interior", required=False)
    cp= forms.CharField(label= "Código Postal", required=True)
    telefono = forms.CharField(label= "Telefono", required=False)

