from django.forms import ModelForm
from django import forms
from Siswa.models import Siswa

class FormSiswa(ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control'}),
            'kelas' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'keterangan_id' : forms.Select({'class':'form-control'}),
        }
