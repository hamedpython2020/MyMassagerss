# Generated by Django 4.1.1 on 2022-09-05 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(verbose_name='تاریخ تولد')),
                ('Phone_number', models.CharField(max_length=11, null=True, verbose_name='شماره مبایل')),
                ('gender', models.IntegerField(blank=True, choices=[(1, 'مرد'), (2, 'زن')], verbose_name='جنسیت')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/profile_image/', verbose_name='عکس پروفایل')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری')),
            ],
            options={
                'verbose_name': 'حساب کاربری',
                'verbose_name_plural': 'حساب کاربری',
            },
        ),
    ]
