from django import forms 
from .models import Pacijent, Zakazivanje, Pacijent_Memo, Pacijent_File
from bootstrap_datepicker_plus import DatePickerInput,DateTimePickerInput,TimePickerInput
from datetime import *

class addPacijentForm(forms.ModelForm): 

    class Meta:
        model = Pacijent
        fields = ['ime','prezime','telefon','email']
        labels = {'ime':'Ime ','prezime':'Prezime ','email':"e-mail "}
        widgets = {
            'ime': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ime pacijenta'}),
            'prezime': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Prezime pacijenta'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Broj telefona'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ZakazivanjeqForm(forms.ModelForm): 

    class Meta:
        model = Zakazivanje
        #time_start = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
        fields = ['ime_prezime','date','time_start','time_end','dr','text']
        labels = {'ime_prezime':'Odabrati pacijenta ',}
        widgets = {
            'ime_prezime':forms.Select(attrs={'class': 'form-control','placeholder':'Select Year'}),
            'date': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Odabrati datum'},),
            'time_start': forms.TimeInput(attrs={'class': 'form-control','placeholder': 'Počinje termin'}),
            'time_end': forms.TimeInput(attrs={'class': 'form-control','placeholder': 'Završava termin'}),
            'dr':forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Unesi opis'}),
        }

class Pacijent_MemoForm(forms.ModelForm):
    
    class Meta:
        model = Pacijent_Memo
        fields = ('memo_pacijent','idpacijenta')
        widgets = {
            'memo_pacijent': forms.Textarea(attrs={'class':'form-control','placeholder':'Unesi belešku'}),
            'idpacijenta':forms.Select(attrs={'class': 'form-control'}),
        }


class Pacijent_FileForm(forms.ModelForm):
    
    class Meta:
        model = Pacijent_File
        fields = ('imepacijenta','opis','fajl')
        labels ={'imepacijenta':'Odabrati pacijenta'}
        widgets = {
            'imepacijenta':forms.Select(attrs={'class': 'form-control','placeholder':'Select Year'}),
            'opis': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Dodaj opis fajla'}),
        #     'telefon': forms.forms.FileField(attrs={'class': 'form-control'}),
            
         }