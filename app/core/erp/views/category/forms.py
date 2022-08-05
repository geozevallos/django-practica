from django.forms import ModelForm, TextInput, Textarea
from core.erp.models import Category

class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for form in self.visible_fields():
        form.field.widget.attrs['class'] = 'form-control'
        form.field.widget.attrs['autocomplete']='off'


    class Meta:
         model = Category
         fields = '__all__'
         labels = {
            'name': 'Nombre',
            'description': 'Descripción'
         }
         widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingresa un nombre'
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Ingresa una descripción',
                    'rows': 3,
                    'cols': 3,
                }
            )
         }