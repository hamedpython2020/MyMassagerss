# Here we make the form for our works

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from account.models import Profile
from django import forms


#################################################

# form for creat a user bot no staf or superuser#
class Signup_form(UserCreationForm):
    pass


# make signup form'

#################################################

# form for creat a profile#
class profil_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Phone_number', 'gender', 'picture']
        pass
    years = []
    for i in range(1320, 1420):
        years.append(str(i))
        pass
    months = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد',
              4: 'تیر',     5: 'مرداد',   6: 'شهریور',
              7: 'مهر',     8: 'آبان',    9: 'آذر',
              10: 'دی',     11: 'بهمن',   12: 'اسفند'
              }
    Birth_date = forms.DateField(label='تاریخ تولد', widget=forms.SelectDateWidget(years=years, months=months))

    def clean_Phone_number(self):
        phone = self.cleaned_data['Phone_number']
        try:
            assert phone.startswith('09') or phone.startswith('+989'), 'شماره تلفن باید با 09 یا 98+ شروع شود'
            assert int(phone), 'شماره تلفن را درست وارد کنید'
        except:
            raise ValidationError('شماره تلفن قالب درستی ندارد')
        Phone_number = phone
        return Phone_number

    pass

#################################################

class name(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        pass