# Generated by Django 3.2.3 on 2021-10-23 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chem_e_cross', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_chem_e_cross',
            name='alternate_phone_number',
        ),
        migrations.RemoveField(
            model_name='user_chem_e_cross',
            name='permanent_address',
        ),
    ]
