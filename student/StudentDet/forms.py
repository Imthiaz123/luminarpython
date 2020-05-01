from django.forms import ModelForm
from StudentDet.models import student
from django import forms

class studentCreationForm(ModelForm):

    confirmpassword=forms.CharField(max_length=150)

    class Meta:
        model=student
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

        fields=['roll','name','course','address','username','password','confirmpassword']


class StudentupdateForm(ModelForm):

    class Meta:
        model=student
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }

        fields = ['roll','name', 'course', 'address', 'password']

    def __init__(self, *args, **kwargs):
        super(StudentupdateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['roll'].widget.attrs['readonly'] = True
