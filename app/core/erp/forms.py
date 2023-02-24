from datetime import datetime

from django.forms import ModelForm, TextInput, Textarea, ValidationError, Form, ModelChoiceField, Select, DateInput, CharField

from core.erp.models import Category, Product, Client

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
         exclude = ('created_by', 'updated_by',)

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




class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control'
    }))
    productos = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese una descripción'
    }))


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dni',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data