from django.forms import ModelForm, TextInput, Textarea, ValidationError
from core.erp.models import Category, Product

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

    # Validar data
    # def clean(self):
    #     cleaned = super().clean()
    #     # if len(cleaned['name']) < 10:
    #         # self.add_error('name', 'Le faltan caracteres')
    #         # raise ValidationError('Validacion generica')
    #     return cleaned


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
        }