# Generated by Django 3.1.9 on 2021-09-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formplugin',
            name='action_backend',
            field=models.CharField(choices=[('email_only', 'Email only'), ('none', 'None'), ('default', 'Default')], default='default', max_length=15, verbose_name='Action backend'),
        ),
    ]
