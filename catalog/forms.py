from django import forms

from .models import Category, Service

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'status']
        labels = {'name': 'Nombre', 'description': 'Descripción', 'status': 'Estado'}
        widget = {'description':forms.TextInput, 'status':forms.CheckboxInput}
         
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['status'].widget.attrs.update({'class':'form-check-input'})