# Generated by Django 2.0.7 on 2019-02-08 22:16

import datetime
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
            name='MedicalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('medical_condition', models.CharField(max_length=255)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(max_length=1)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('date_updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
