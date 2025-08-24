from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_name(self):
        name = self.cleaned_data['name']
        lower_name = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_name:
                raise forms.ValidationError(f"Название не должно содержать слово '{word}'.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        lower_desc = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_desc:
                raise forms.ValidationError(f"Описание не должно содержать слово '{word}'.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price