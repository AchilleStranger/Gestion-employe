from django import forms
from.models import Employe    
class EmployeForm(forms.ModelForm):
    class Meta:
        model=Employe
        fields=["nom", "email", "poste", "salaire","date_de_naissance","lieu_de_residence"]
        widgets={
            'nom':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'Nom'

            }),
            'email':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'Email'

            }),
            'poste':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'Poste'

            }),
            'salaire':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'Salaire'

            }),
            'date_de_naissance':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'date_de_naissance'

            }),
            'lieu_de_residence':forms.TextInput(attrs={
                'class' : "input w-full",
                'placeholder':'lieu_de_residence'

            }),
            
            
        }
