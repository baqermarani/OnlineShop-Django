from django import forms



class CartAddForm(forms.Form):
    """
    Form for adding items to the cart.
    """
    quantity = forms.IntegerField(
        min_value=1,
        max_value=100,
        initial=1
    )

class CoupoanApplayForm(forms.Form):
    """
    Form for applying coupons.
    """
    code = forms.CharField(
        label='Coupon code',
    )