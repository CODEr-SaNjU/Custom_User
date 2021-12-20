# Generated by Django 4.0 on 2021-12-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customapp', '0004_remove_userprofile_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='sanju', max_length=300, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='saini', max_length=300, verbose_name='Last Name'),
        ),
    ]
