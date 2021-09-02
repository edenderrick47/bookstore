from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Kilimani', 'Kilimani'),
		('Loresho', 'Loresho'),
		('Westlands', 'Westlands '),
	)

	DISCRICT_CHOICES = (
		('Langata', 'Langata'), 
		('Nairobi West', 'Nairobi West'),
		('Eastleigh', 'Eastleigh'),
	)

	PAYMENT_METHOD_CHOICES = (
		('MPESA', 'MPESA'),
		('PAYPAL','Paypal')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
