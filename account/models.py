from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب کاربری'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری')
    birth_date = models.DateField('تاریخ تولد', null=False)
    Phone_number = models.CharField('شماره موبایل', max_length=11, null=True)
    Male = 1
    Female = 2
    Gender_Choices = ((Male, 'مرد'), (Female, 'زن'))
    gender = models.IntegerField('جنسیت', choices=Gender_Choices, null=False, blank=True)
    picture = models.ImageField('عکس پروفایل', upload_to='users/profile_image/', null=True, blank=True)

    def __str__(self):
        return "کاربر {}".format(self.user.username)
