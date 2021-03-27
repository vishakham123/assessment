from django import forms
from django.utils.translation import pgettext_lazy
from django.utils import timezone
from django.apps.registry import apps

User = apps.get_model('user', 'User')

class CustomerForm(forms.ModelForm):
    GENDER_TYPE = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    gender = forms.ChoiceField(required=False, choices=GENDER_TYPE)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if self.instance:
            print("-------------rr-------------->")
            print(self.instance.birth_date)
            self.fields['birth_date'].initial = self.instance.birth_date
            


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('birth_date'):
            if cleaned_data.get("birth_date") == timezone.now().date():
                raise forms.ValidationError({'birth_date': ["Birth Date can not be today's date",]})
            if cleaned_data.get("birth_date") > timezone.now().date():
                raise forms.ValidationError({'birth_date': ["Birth Date can not be greater than today's date",]})



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        labels = {
            'first_name': pgettext_lazy(
                'Customer form: First name field', 'First Name'),
            'last_name': pgettext_lazy(
                'Customer form: Last name field', 'Last Name'),
            'birth_date': pgettext_lazy(
                'Customer form: birth date field', 'Date of Birth'),
            'gender': pgettext_lazy(
                'Customer form: gender field', 'Gender')
        }