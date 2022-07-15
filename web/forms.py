from logging import PlaceHolder
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput

from .models import Contact


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