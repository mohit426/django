# Generated by Django 2.0.6 on 2018-06-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
