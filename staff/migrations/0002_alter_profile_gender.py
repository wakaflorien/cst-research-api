# Generated by Django 3.2.2 on 2021-09-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=100),
        ),
    ]