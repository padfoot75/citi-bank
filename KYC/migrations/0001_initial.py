# Generated by Django 3.1.8 on 2022-05-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('aadhar_number', models.CharField(max_length=20)),
                ('pan_number', models.CharField(max_length=20)),
                ('aadhar_photo', models.ImageField(upload_to='aadhar_images/')),
            ],
        ),
    ]
