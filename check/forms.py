from django import forms
from check.models import info,Gen
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Row,Column
class StudentForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Gen,widget=forms.RadioSelect,initial="male")

    class Meta:
        model=info
        fields="__all__"

    #def __init__(self,*args,**kwargs):
    #    super().__init__(*args,**kwargs)
    #    self.helper=FormHelper()
    #    self.helper.form_method='post'
    #    self.helper.add_input(Submit('save_student','Save Student'))
         #self.helper.add_input(Submit('cancel', 'cancel'))




