# -*- coding: UTF-8 -*-
from django import forms
from django.forms import extras
from django.forms.models import formset_factory
from django.forms import widgets
from django.contrib.auth.models import User
from bdgqpt.models import CaoZuoPiao, UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder,Tab,Div,Field,InlineRadios
from datetimewidget.widgets import DateTimeWidget
from dal import autocomplete







class CaoZuoPiaoForm_yuling(forms.ModelForm):
    nipiaoren=forms.ModelChoiceField(queryset=UserProfile.objects.all(),widget=autocomplete.ModelSelect2(url='bdgqpt:name-autocomplete'),label='拟票人' )
    class Meta:
        model = CaoZuoPiao
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CaoZuoPiaoForm_yuling, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal test'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.layout=Layout(
            'nipiaoren',
            ButtonHolder(Submit('submit','保存')),
            )

class CaoZuoPiaoForm_zhengling(forms.ModelForm):
    nipiaoren=forms.ModelChoiceField(queryset=UserProfile.objects.all(),widget=autocomplete.ModelSelect2(url='bdgqpt:name-autocomplete'),label='拟票人')

    class Meta:
        model = CaoZuoPiao
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(CaoZuoPiaoForm_zhengling, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout=Layout(
            'nipiaoren',
            ButtonHolder(Submit('submit','保存')),
            )


class CaoZuoPiaoForm_update(forms.ModelForm):   
    nipiaoren=forms.ModelChoiceField(queryset=UserProfile.objects.all(),widget=autocomplete.ModelSelect2(url='bdgqpt:name-autocomplete'),label='拟票人')
    class Meta:
        model = CaoZuoPiao
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(CaoZuoPiaoForm_update, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout=Layout(
            'nipiaoren',
            ButtonHolder(Submit('submit','保存')),
            )

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','password','last_name','first_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone_number',)



