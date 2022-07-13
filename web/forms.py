from logging import PlaceHolder
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput

from .models import Contact


class reviewForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'sppb-form-control','type':'text','placeholder':'Your Name','id':'sppb-form-builder-field-0','name':'form-builder-item-[name*]','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'sppb-form-control','type':'email','placeholder':'Your Email','id':'sppb-form-builder-field-1','name':'form-builder-item-[email*]','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'sppb-form-control','type':'text','placeholder':'Your Phone','id':'sppb-form-builder-field-2','name':'form-builder-item-[phone*]','required':'required','autocomplete':'off',}),
            'subject': TextInput(attrs={'class':'sppb-form-control','type':'text','placeholder':'Subject','id':'sppb-form-builder-field-3','name':'form-builder-item-[subject*]','required':'required','autocomplete':'off',}),
            'message':Textarea(attrs={'class':'sppb-form-control not-resize','placeholder':'Your Message','id':'sppb-form-builder-field-4','name':'form-builder-item-[message*]','required':'required','autocomplete':'off',})
        }