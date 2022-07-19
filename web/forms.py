from logging import PlaceHolder
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput

from .models import *

class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields= ['name','email','phone','subject','message',]
        widgets= {
            'name': TextInput(attrs={'class':'sppb-form-control','placeholder':'Your Name','id':'sppb-form-builder-field-0','name':'name','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'sppb-form-control','placeholder':'Your Email','id':'sppb-form-builder-field-1','name':'email','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'sppb-form-control','placeholder':'Your Phone','id':'sppb-form-builder-field-2','name':'phone','required':'required','autocomplete':'off',}),
            'subject': TextInput(attrs={'class':'sppb-form-control','placeholder':'Subject','id':'sppb-form-builder-field-3','name':'subject','required':'required','autocomplete':'off',}),
            'message':Textarea(attrs={'class':'sppb-form-control not-resize','placeholder':'Your Message','id':'sppb-form-builder-field-4','name':'message','required':'required','autocomplete':'off',})
        }


class enquiry_form(forms.ModelForm):
    
    class Meta:
        model = Enquiry
        fields= ['name','phone','product_name','quantity']
        widgets= {
            'name': TextInput(attrs={'class':'form-control','placeholder':'Your Name','name':'name','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'form-control','placeholder':'Your Phone','name':'phone','required':'required','autocomplete':'off',}),
            'product_name': TextInput(attrs={'class':'form-control','placeholder':'product_name','name':'product_name','required':'required','autocomplete':'off',}),
            'quantity': TextInput(attrs={'class':'form-control','placeholder':'quantity','name':'quantity','required':'required','autocomplete':'off',}),
        }