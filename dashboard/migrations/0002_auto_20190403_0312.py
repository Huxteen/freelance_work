# Generated by Django 2.0.7 on 2019-04-03 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalreport',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='MedicalReport',
        ),
    ]