from django  import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
                    widget=forms.NumberInput(
                        attrs={
                            'class': 'js-quantity-filter-field form-number form-control',
                            'type': 'number',
                            'id': 'edit-price-96',
                            'name': 'price_96',
                            'value': 0,
                            'step': 1,
                            'min': 0,
                            'max': 20
                        }
                    )
                )
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

