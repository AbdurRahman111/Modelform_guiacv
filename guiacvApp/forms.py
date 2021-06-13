from django.forms import ModelForm
from .models import form_register


class submit_form_register(ModelForm):
    class Meta:
        model = form_register
        fields = ['Name', 'Telephone1', 'Telephone2', 'Celular', 'Email', 'Website', 'Address', 'City', 'Island', 'Category', 'Sub_Category', 'Description', 'Photo1', 'Photo2', 'Photo3', 'Photo4']



